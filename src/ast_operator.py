#!/usr/bin/env python
"""
    Abstract child class for the operator nodes in the Abstract Syntax Tree
"""
from ast_node import ASTNode
from ast_token import ASTToken


class ASTOperator(ASTNode):
    """
    Class inheriting from the ASTNode to keep track of the operator nodes within
    the Abstract Syntax Tree
    """
    def __init__(self, left_child, right_child, operator):
        """
        Default constructor
        :param right_child:
        :param left_child:
        :param operator:
        """
        self.left_child = left_child
        self.right_child = right_child
        self.value = operator

        if operator == '+':
            self.type = ASTToken.PLUS
        elif operator == '-':
            self.type = ASTToken.MINUS
        elif operator == '*':
            self.type = ASTToken.MULT
