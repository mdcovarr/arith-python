#!/usr/bin/env python
"""
    Abstract parent class for the expressions possible for the arith language
"""


class Expression:
    def __init__(self, tokens):
        if tokens.left:
            self.left = tokens.left
        if tokens.right:
            self.right = tokens.right
        if tokens.oper:
            self.oper = tokens.oper
        if tokens.value:
            self.value = tokens.value
