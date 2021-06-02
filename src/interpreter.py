from evaluator import Evaluator
from parser import Parser
from symbol import Symbol


class Interpreter:
    def __init__(self, evaluator=Evaluator(), parser=Parser()) -> None:
        self.evaluator = evaluator
        self.parser = parser

    def eval(self, line: str) -> Symbol:
        exp = self.parser.parse(line)
        return self.evaluator.run(exp).contains
