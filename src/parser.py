#!/usr/bin/python
"""
    Helper class used to create a Abstract Syntax Tree
    from a list of ASTNodes
"""
from token import Token
from expression import Expression


class Parser(object):
    """
    Class used to create Abstract Syntax Tree
    """
    def __init__(self, nodes):
        """
        Default constructor
        :param nodes: nodes representing integers and operators
        """
        self.nodes = nodes
        self.current_node = self.nodes.pop()
        self.ast = self.current_node

    def get_next_node(self):
        if len(self.nodes) > 0:
            self.current_node = self.nodes.pop()
        else:
            self.current_node = None

    def fix_precedence(self, sub_tree):
        """
        Function used to fix precedence in the AST when attempting
        to add a sub_tree to the AST
        :param sub_tree:
        :return None:
        """
        sub_tree.operator.left = self.ast.right
        self.ast.right = sub_tree.operator

    def add_sub_tree(self, sub_tree):
        """
        Function to add a sub tree representing an operator and a
        right side expression that will be added to the AST
        :param sub_tree:
        :return None:
        """
        if self.ast.value == '+' and sub_tree.operator.value == '*':
            self.fix_precedence(sub_tree)
        else:
            sub_tree.operator.left = self.ast
            self.ast = sub_tree.operator

    def create_ast(self):
        """
        Function used to create the AST
        :return ASTNode: ASTNode representing the root node
        """
        expression = Expression()

        while len(self.nodes) > 0:
            self.get_next_node()
            if self.current_node.type is Token.OPERATOR:
                expression.operator = self.current_node
                self.get_next_node()
                expression.right = self.current_node
                self.add_sub_tree(expression)

    def parse(self):
        """
        Function to handle the parsing and creation of the
        Abstract Syntax Tree
        :return None:
        """
        return self.create_ast()