# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
import pathlib
import enum
import concurrent.futures
from dataclasses import dataclass, field

# Athena Packages

# Local Imports
from AthenaLib.constants.types import PATHLIKE
from AthenaLib.logging._logger import AthenaLogger, LoggerLevels
import AthenaLib.logging.logger_sqlite_functions as LSF

# ----------------------------------------------------------------------------------------------------------------------
# - Support Code -
# ----------------------------------------------------------------------------------------------------------------------
CF_PPE = concurrent.futures.ProcessPoolExecutor

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
@dataclass(slots=True)
class AthenaSqliteLogger(AthenaLogger):
    sqlite_path:pathlib.Path
    table_to_use:str

    enable_track: bool = True
    enable_debug: bool = True
    enable_warning: bool = True
    enable_error: bool = True

    # non init
    _pool_executor: CF_PPE = field(init=False, default_factory=lambda:CF_PPE(max_workers=1))

    # ------------------------------------------------------------------------------------------------------------------
    # - Logger functions that write to the database -
    # ------------------------------------------------------------------------------------------------------------------
    def shutdown(self):
        self._pool_executor.shutdown()

    def create_tables(self):
        self._pool_executor.submit(
            LSF.create_tables,
            sqlite_path=self.sqlite_path,
            queries=[
                f"""# noinspection SqlNoDataSourceInspectionForFile
                CREATE TABLE IF NOT EXISTS `{self.table_to_use}` (
                    `id` INTEGER PRIMARY KEY,
                    `time` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
                    `lvl` TEXT NOT NULL,
                    `section` TEXT,
                    `txt` TEXT
                );
                """,
            ]
        )

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