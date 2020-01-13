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
        self.current_node = None
        self.ast = None

    def error(self, error_message):
        """
        Function used to raise Exception with error message
        :param error_message: error message
        :return None:
        """
        raise Exception(error_message)

    def get_ast_root(self):
        """
        Function used to get the root of the ast
        :return ASTNode: root of the AST
        """
        return self.ast

    def get_next_node(self):
        """
        Function used to get the next node in the list of nodes created
        from expression
        :return None:
        """
        if len(self.nodes) > 0:
            self.current_node = self.nodes.pop(0)
        else:
            self.current_node = None

    def is_first_node_valid(self):
        """
        Function to check if initial value of expression is valid
        :return: True if valid start of expression, False otherwise
        """

        if len(self.nodes) >= 2:
            if self.nodes[0].type is ASTToken.MINUS and self.nodes[1].type is ASTToken.INTEGER:
                return True
            elif self.nodes[0].type is ASTToken.INTEGER:
                return True
            else:
                return False
        else:
            if self.nodes[0].type is ASTToken.INTEGER:
                return True
            else:
                return False

    def is_last_node_valid(self):
        """
        Function to check if ending node is valid
        :return: True if last node valid, False otherwise
        """
        end_index = len(self.nodes) - 1

        if self.nodes[end_index].type is ASTToken.INTEGER:
            return True

        return False

    def has_valid_operators(self):
        """
        Function used to check that there are no more than 2 operators
        in a row. And if there are two operators the second needs to be a
        minus since it can be used as a negative sign
        :return: True if operators in expression are valid, False otherwise
        """
        i = 0
        j = 1
        seen_two_opers = False

        while j < len(self.nodes):
            if (self.nodes[i].type is ASTToken.PLUS) or (self.nodes[i].type is ASTToken.MINUS) or (self.nodes[i].type is ASTToken.MULT):
                if seen_two_opers:
                    if not self.nodes[j].type is ASTToken.INTEGER:
                        return False
                else:
                    if not (self.nodes[j].type is ASTToken.INTEGER or self.nodes[j].type is ASTToken.MINUS):
                        return False

                if self.nodes[j].type is ASTToken.MINUS:
                    seen_two_opers = True
                else:
                    seen_two_opers = False

            i += 1
            j += 1
        return True

    def create_negative_numbers(self):
        """
        Function used to create negative numbers as a single node
        :return None:
        """
        i = 0
        j = 1

        while j < len(self.nodes):
            if ((self.nodes[i].type is ASTToken.PLUS or self.nodes[i].type is ASTToken.MINUS
                    or self.nodes[i].type is ASTToken.MULT) and self.nodes[j].type is ASTToken.MINUS):
                k = j + 1
                self.nodes[k].value = '{0}{1}'.format(self.nodes[j].value, self.nodes[k].value)
                self.nodes.pop(j)
            elif i == 0 and self.nodes[j].type is ASTToken.INTEGER:
                self.nodes[j].value = '{0}{1}'.format(self.nodes[i].value, self.nodes[j].value)
                self.nodes.pop(i)
            else:
                i += 1
                j += 1

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

        if (self.ast.value == '+' or self.ast.value == '-') and sub_tree.operator.value == '*':
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
        self.get_next_node()
        self.ast = self.current_node

        while len(self.nodes) > 0:
            self.get_next_node()
            if (self.current_node.type is ASTToken.PLUS or self.current_node.type is ASTToken.MINUS
                    or self.current_node.type is ASTToken.MULT):
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
        if not self.is_first_node_valid():
            self.error('Error: Invalid way to start expression')

        if not self.is_last_node_valid():
            self.error('Error: Invalid way to end expression')

        if not self.has_valid_operators():
            self.error('Error: Invalid operator sequences')

        self.create_negative_numbers()

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
