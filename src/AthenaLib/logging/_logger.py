# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
from abc import ABC, abstractmethod
import enum
import concurrent.futures

# Athena Packages

# Local Imports

# ----------------------------------------------------------------------------------------------------------------------
# - Support Code -
# ----------------------------------------------------------------------------------------------------------------------
error_type = lambda obj: f"the following did not inherit from expected AthenaLoggerType: {obj}"
error_logger = lambda obj: f"the following did not inherit from expected AthenaLogger: {obj}"

class LoggerLevels(enum.StrEnum):
    DEBUG = enum.auto()
    WARN = enum.auto()
    ERROR = enum.auto()

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
class AthenaLogger(ABC):
    _pool_executor:concurrent.futures.ProcessPoolExecutor

    # ------------------------------------------------------------------------------------------------------------------
    # - Abstract Features that need to be implemented -
    # ------------------------------------------------------------------------------------------------------------------
    @abstractmethod
    def log(self, level:LoggerLevels, section:str|enum.StrEnum, text:str|None):
        pass

    def log_debug(self, section:str|enum.StrEnum, text:str|None=None):
        self.log(level=LoggerLevels.DEBUG, section=section, text=text)

    def log_warning(self, section:str|enum.StrEnum, text:str|None=None):
        self.log(level=LoggerLevels.WARN, section=section, text=text)

    def log_error(self, section:str|enum.StrEnum, text:str|None=None):
        self.log(level=LoggerLevels.ERROR, section=section, text=text)



