# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
import pathlib
import enum
import concurrent.futures

# Athena Packages

# Local Imports
from AthenaLib.constants.types import PATHLIKE
from AthenaLib.logging._logger import AthenaLogger, LoggerLevels
import AthenaLib.logging.logger_sqlite_functions as LSF

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
class AthenaSqliteLogger(AthenaLogger):
    sqlite_path:pathlib.Path
    table_to_use:str

    def __init__(self, sqlite_path:PATHLIKE = "data/logger.sqlite", table_to_use:str = None):
        self.sqlite_path = pathlib.Path(sqlite_path)
        self.table_to_use = table_to_use

        # noinspection SqlNoDataSourceInspection
        self._pool_executor = concurrent.futures.ProcessPoolExecutor(
            max_workers=1,
            initializer=LSF.create_tables,
            initargs=(
                self.sqlite_path,
                [
                    f"""
                    CREATE TABLE IF NOT EXISTS `{table_to_use}` (
                        `id` INTEGER PRIMARY KEY,
                        `time` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
                        `lvl` TEXT NOT NULL,
                        `section` TEXT,
                        `txt` TEXT
                    );
                    """,
                ]
            )
        )

    # ------------------------------------------------------------------------------------------------------------------
    # - Logger functions that write to the database -
    # ------------------------------------------------------------------------------------------------------------------
    def shutdown(self):
        self._pool_executor.shutdown()

    def log(self, level:LoggerLevels, section:str|enum.StrEnum, text:str|None):
        self._pool_executor.submit(
            LSF.execute_log,
            sqlite_path=self.sqlite_path,
            level=level,
            section=section,
            text=text,
            table_to_use=self.table_to_use,
            commit=True
        )