from typing import List, Union
from evaluator import Evaluator
from __future__ import annotations


class Expression:
    def __init__(self, given: Union[List[Expression], float], evaluator=Evaluator()) -> None:
        self.evaluator = evaluator
        self.contains = given

    def isJust(self):
        return not type(self.contains) is List

    def evaluate(self):
        return self.evaluator
