#!/usr/bin/env python
"""
    Child of the Expression class representing an Add expression
"""
from Expression import Expression


class Add(Expression):
    def __init__(self, tokens):
        Expression.__init__(self, tokens)
