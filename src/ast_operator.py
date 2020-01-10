#!/usr/bin/env python
"""
    Abstract child class for the operator nodes in the Abstract Syntax Tree
"""
from ast_node import ASTNode


class ASTOperator(ASTNode):
    """
    Class inheriting from the ASTNode to keep track of the operator nodes within
    the Abstract Syntax Tree
    """
    def __init__(self, right_expression, left_expression, operator):
        """
        Default constructor
        :param right_expression:
        :param left_expression:
        :param operator:
        """
        self.right_exp = right_expression
        self.left_exp = left_expression
        self.oper = operator
        super(ASTOperator, self).__init__()
