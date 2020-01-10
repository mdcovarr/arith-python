#!/usr/bin/env python
"""
    Child of the Expression class representing an int expression
"""
from Expression import Expression


class Int(Expression):
    def __init__(self, tokens):
        Expression.__init__(self, tokens)
