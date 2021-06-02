from operator import *
from functools import reduce

default_environment_table = {
    '+': lambda *params: reduce(lambda a, b: add(a, b), params),
    '-': lambda *params: reduce(lambda a, b: sub(a, b), params),
    '*': lambda *params: reduce(lambda a, b: mul(a, b), params),
    '/': lambda *params: reduce(lambda a, b: truediv(a, b), params)
}

separators = ["\r", "\n", "\t", " "]
