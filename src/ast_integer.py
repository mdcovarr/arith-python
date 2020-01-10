#!/usr/bin/env python
"""
    Abstract child class for the integer nodes in the Abstract Syntax Tree
"""
from ast_node import ASTNode
from token import Token


class ASTInteger(ASTNode):
    """
    Class inheriting from the ASTNode to keep track of the integer nodes within
    the Abstract Syntax Tree
    """
    def __init__(self, value):
        """
        Default constructor
        :param value:
        """
        self.value = value
        self.type = Token.INTEGER
