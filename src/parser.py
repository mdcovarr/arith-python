#!/usr/bin/python
"""
    Helper class used to create a Abstract Syntax Tree
    from a list of ASTNodes
"""
from ast_token import ASTToken
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
        self.current_node = self.nodes.pop(0)
        self.ast = self.current_node

    def get_next_node(self):
        if len(self.nodes) > 0:
            self.current_node = self.nodes.pop(0)
        else:
            self.current_node = None

    def fix_precedence(self, sub_tree):
        """
        Function used to fix precedence in the AST when attempting
        to add a sub_tree to the AST
        :param sub_tree:
        :return None:
        """
        sub_tree.operator.left_child = self.ast.right_child
        self.ast.right_child = sub_tree.operator

    def add_sub_tree(self, sub_tree):
        """
        Function to add a sub tree representing an operator and a
        right side expression that will be added to the AST
        :param sub_tree:
        :return None:
        """
        sub_tree.operator.right_child = sub_tree.right

        if self.ast.value == '+' and sub_tree.operator.value == '*':
            self.fix_precedence(sub_tree)
        else:
            sub_tree.operator.left_child = self.ast
            self.ast = sub_tree.operator

    def create_ast(self):
        """
        Function used to create the AST
        :return ASTNode: ASTNode representing the root node
        """
        expression = Expression()

        while len(self.nodes) > 0:
            self.get_next_node()
            if self.current_node.type is ASTToken.OPERATOR:
                expression.operator = self.current_node
                self.get_next_node()
                expression.right = self.current_node
                self.add_sub_tree(expression)
            else:
                print('Error there are two integers in a row')
        return self.ast

    def parse(self):
        """
        Function to handle the parsing and creation of the
        Abstract Syntax Tree
        :return ASTNode: the ASTNode that is the root of the AST
        """
        return self.create_ast()

    def print_ast(self):
        queue = []
        queue.append(self.ast)

        while len(queue) > 0:
            current_node = queue.pop(0)

            if hasattr(current_node, 'left_child'):
                queue.append(current_node.left_child)
            if hasattr(current_node, 'right_child'):
                queue.append(current_node.right_child)

            print('{}'.format(current_node.value))
