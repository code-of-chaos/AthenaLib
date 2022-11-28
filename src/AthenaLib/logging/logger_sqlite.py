# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
import pathlib
import enum
from dataclasses import dataclass
from typing import Callable

# Athena Packages

# Local Imports
from AthenaLib.logging._logger import AthenaLogger, LoggerLevels
import AthenaLib.logging.logger_sqlite_functions as LSF

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
@dataclass(slots=True)
class AthenaSqliteLogger(AthenaLogger):
    sqlite_path:pathlib.Path = pathlib.Path("data/logger.irc")
    table_to_use:str = "logging"
    cast_to_str:Callable = str

    def __post_init__(self):
        if not self.sqlite_path.exists():
            raise FileNotFoundError(self.sqlite_path)

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
    def log(self, level: LoggerLevels, section: str | enum.StrEnum, data: str | None):
        # If the logger itself hasn't been entered yet,
        #   Store the log to the buffer, and execute at a later date
        if not self._logger_entered:
            self._buffer.append((level, section, self.cast_to_str(data)))
            return

        # Let the pool execute the call to the database
        self._pool_executor.submit(
            LSF.execute_log,
            path=self.sqlite_path,
            level=level,
            section=section,
            data=self.cast_to_str(data),
            table_to_use=self.table_to_use,
            commit=True
        )