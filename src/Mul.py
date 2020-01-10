#!/usr/bin/env python
"""
    Child of the Expression class representing an multiplication expression
"""
from Expression import Expression


class Mul(Expression):
    def __init__(self, tokens):
        Expression.__init__(self, tokens)
