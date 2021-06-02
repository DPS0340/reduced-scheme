from typing import List, Optional
from symbol import Symbol
from expression import Expression


class Parser:
    def __init__(self) -> None:
        pass

    def tokenize(self, line: str) -> list:
        # from https://norvig.com/lispy.html
        return line.replace('(', ' ( ').replace(')', ' ) ').split()

    def parse_go(self, args: List[str]) -> Expression:
        # from https://norvig.com/lispy.html
        if not args:
            raise ValueError(
                "Unexpected error during parse: No arguments found")
        c = args.pop(0)
        if c == "(":
            result = Expression([])
            while args[0] != ')':
                result.contains.append(self.parse_go(args))
            args.pop(0)
            return result
        elif c == ")":
            raise SyntaxError(
                f"Unexpected error during parse: redundant ) found")
        else:
            return Expression(Symbol(c))

    def parse(self, line: str) -> Optional[Expression]:
        return self.parse_go(self.tokenize(line))
