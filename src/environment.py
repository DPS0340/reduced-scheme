from types import FunctionType
from typing import Optional
import constants


class Environment:
    def __init__(self, table=constants.default_environment_table) -> None:
        self.table: dict = table

    def get(self, command: str) -> Optional[FunctionType]:
        return self.table.get(command)
