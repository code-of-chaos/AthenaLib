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
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
@dataclass(slots=True)
class AthenaSqliteLogger(AthenaLogger):
    sqlite_path:pathlib.Path = pathlib.Path("data/logger.irc")
    table_to_use:str = "logging"

    # ------------------------------------------------------------------------------------------------------------------
    # - Context manager for ease of use -
    # ------------------------------------------------------------------------------------------------------------------
    def __enter__(self):
        # Makes sure the table will exist
        self._pool_executor.submit(
            LSF.db_create,
            path=self.sqlite_path,
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

        # After the table has been created
        #   Go through the buffer
        super(AthenaSqliteLogger, self).__enter__()

    # ------------------------------------------------------------------------------------------------------------------
    # - Logger functions that write to the database -
    # ------------------------------------------------------------------------------------------------------------------
    def log(self, level:LoggerLevels, section:str|enum.StrEnum, text:str|None):
        # If the logger itself hasn't been entered yet,
        #   Store the log to the buffer, and execute at a later date
        if not self._logger_entered:
            self._buffer.append((level, section, text))
            return

        # Let the pool execute the call to the database
        self._pool_executor.submit(
            LSF.execute_log,
            path=self.sqlite_path,
            level=level,
            section=section,
            text=text,
            table_to_use=self.table_to_use,
            commit=True
        )