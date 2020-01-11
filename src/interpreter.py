#!/usr/bin/python
"""
    Helper class used to traverse the Abstract Syntax Tree and
    return the appropriate value of the AST
"""


class Interpreter(object):
    """
    Class to determine solution from the AST
    """
    def __init__(self, ast):
        """
        Default constructor
        """
        self.ast = ast

    def traverse_ast(self):
        """
        Function used to traverse the AST in a post-order DFT
        :return:
        """
        return self.visit_node(self.ast)

    def visit_node(self, node):
        """
        Function used to recursively visit AST nodes
        :param node:
        :return: Evaluated expression at current node
        """
        if not hasattr(node, 'left_child') and not hasattr(node, 'right_child'):
            return eval(node.value)

        if node.value == '+':
            return eval('{0} + {1}'.format(self.visit_node(node.left_child), self.visit_node(node.right_child)))
        elif node.value == '*':
            return eval('{0} * {1}'.format(self.visit_node(node.left_child), self.visit_node(node.right_child)))
