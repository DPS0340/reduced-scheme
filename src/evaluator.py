from typing import List, Union
from environment import Environment
from expression import Expression
from symbol import Symbol


class Evaluator:
    def __init__(self, environment=Environment()) -> None:
        self.environment: Environment = environment

    def run(self, exp: Expression) -> Expression:
        if exp.isList():
            for i in range(1, len(exp.contains)):
                if exp.contains[i].isList():
                    exp.contains[i] = self.run(exp.contains[i])
            op_code = exp.contains[0].contains.value
            operand = map(lambda x: x.contains.value, exp.contains[1:])
            if not operand:
                raise ValueError(
                    "Unexpected error during function call: no operands")
            op_func = self.environment.get(op_code)
            if not op_func:
                raise ValueError(
                    "Unexpected error during function call: function symbol not found")
            return Expression(Symbol(op_func(*operand)))
        else:
            return exp
