#!/usr/bin/python
"""
    Helper class used to keep track of an expression
    left_value, operator, right_value
"""


class Expression(object):
    """
    Class used to keep track of an expression
    """
    def __init__(self):
        self.operator = None
        self.right = None

    def is_complete(self):
        if self.operator and self.right:
            return True
        return False
