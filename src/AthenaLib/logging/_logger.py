# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
from abc import ABC, abstractmethod
from typing import ClassVar
import enum
import contextlib

# Athena Packages

# Local Imports

# ----------------------------------------------------------------------------------------------------------------------
# - Support Code -
# ----------------------------------------------------------------------------------------------------------------------
error_type = lambda obj: f"the following did not inherit from expected AthenaLoggerType: {obj}"
error_logger = lambda obj: f"the following did not inherit from expected AthenaLogger: {obj}"

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
class AthenaLogger(ABC):
    _loggers:ClassVar[dict[enum.StrEnum: AthenaLogger]] = {}
    enabled:bool

    # ------------------------------------------------------------------------------------------------------------------
    # - Features already able to be defined by AthenaLogger -
    # ------------------------------------------------------------------------------------------------------------------
    @classmethod
    def get_logger(cls, logger_type:enum.StrEnum):
        return cls._loggers[logger_type]

    @classmethod
    def set_logger(cls, logger_type:enum.StrEnum, logger:AthenaLogger):
        # Given loggers are defined in development mode,
        #   Don't need to check for this in production mode
        assert isinstance(logger, AthenaLogger), error_logger(logger)
        # ---

        cls._loggers[logger_type] = logger

    @contextlib.contextmanager
    def if_enabled(self):
        if self.enabled:
            yield None

    # ------------------------------------------------------------------------------------------------------------------
    # - Abstract Features that need to be implmented -
    # ------------------------------------------------------------------------------------------------------------------
    @abstractmethod
    def __init__(self, *args, **kwargs):
        pass

    @abstractmethod
    async def _db_connect(self):
        """
        Async Context manager to easily connect to the database
        Commits all changes to the db, before closing the connection
        """


