#!/usr/bin/env python
"""
    Class used to read the input expression and create tokens
"""
from ast_token import ASTToken


class InputReader(object):
    """
    Class used to read in expression and create tokens if expression is valid
    """
    def __init__(self):
        """
        Default constructor for the InputReader Class
        """
        self.expression = ''
        self.current_token_type = ASTToken.NONE
        self.current_position = 0
        self.current_char = ''
        self.tokens = []
        self.integers_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        self.operators_list = ['+', '*', '-']
        self.sub_string = ''

    def get_expression(self):
        """
        Function used to get the current expression from the user
        :return None:
        """
        self.expression = raw_input("Enter expression to be parsed: ")

    def set_expression(self, expression):
        """
        Setter function used to set the expression member variable
        :param expression:
        :return None:
        """
        self.expression = expression

    def get_tokens(self):
        """
        Getter function used to get the tokens parsed
        :return:
        """
        return self.tokens

    def reset_reader(self):
        """
        Function user to reset reader to default settings
        :return None:
        """
        self.expression = ''
        self.current_token_type = ASTToken.NONE
        self.sub_string = ''
        self.tokens = []
        self.current_position = 0

    def update_current_token_type(self, token_value):
        """
        Function used to update the current token type seen
        :param token_value: token type value
        :return None:
        """
        if token_value == '+':
            self.current_token_type = ASTToken.PLUS
        elif token_value == '-':
            self.current_token_type = ASTToken.MINUS
        elif token_value == '*':
            self.current_token_type = ASTToken.MULT
        else:
            self.current_token_type = ASTToken.INTEGER

    def check_integer(self, current_char):
        """
        Function used to check the validity of the next char being an integer. Checks are
        based on what the current token type is
        :param current_char:
        :return None:
        """
        if self.current_token_type is ASTToken.NONE or self.current_token_type is ASTToken.INTEGER:
            # append char to the running integer value being formed
            self.sub_string += current_char
        else:
            # need to create a token for the operator
            self.tokens.append(self.sub_string)
            self.sub_string = ''
            self.sub_string += current_char

        self.update_current_token_type(current_char)

    def check_operator(self, current_char):
        """
        Function used to check the validity of the next char being an operator. Checks are
        based on what the current token type is
        :param current_char:
        :return None:
        """
        if self.current_token_type is ASTToken.NONE:
            self.sub_string += current_char
        else:
            self.tokens.append(self.sub_string)
            self.sub_string = ''
            self.sub_string += current_char

        # need to change this to the correct operator
        self.update_current_token_type(current_char)

    def decrypt_expression(self):
        """
        Function used to decrypt the expression passed and create tokens
        :return: True if valid characters only, False otherwise
        """
        while self.current_position < len(self.expression):
            current_char = self.expression[self.current_position]

            if current_char in self.integers_list:
                self.check_integer(current_char)
            elif current_char in self.operators_list:
                self.check_operator(current_char)
            elif current_char == ' ':
                self.current_position += 1
                continue
            else:
                print('Error invalid character!')
                return False

            self.current_position += 1

        if self.sub_string != '':
            self.tokens.append(self.sub_string)
            self.sub_string = ''

        return True
