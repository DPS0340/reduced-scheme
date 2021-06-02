from __future__ import annotations
from symbol import Symbol
from typing import List, Union


class Expression:
    def __init__(self, given: Union[List[Expression], Symbol]) -> None:
        self.contains = given

    def isList(self):
        return type(self.contains) is list
