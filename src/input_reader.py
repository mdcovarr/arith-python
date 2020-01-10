#!/usr/bin/env python
"""
    Class used to read the input expression and create tokens
"""
import enum


class Token(enum.Enum):
    """
    Class to keep trace of the Token types
    """
    NONE = 1
    INTEGER = 2
    OPERATOR = 3


class InputReader:
    """
    Class used to read in expression and create tokens if expression is valid
    """
    def __init__(self):
        """
        Default constructor for the InputReader Class
        """
        self.expression = ''
        self.current_token_type = Token.NONE
        self.current_position = 0
        self.tokens = []
        self.integers_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '-']
        self.operators_list = ['+', '*']
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
        self.current_token_type = Token.NONE
        self.sub_string = ''
        self.tokens = []

    def check_integer(self, current_char):
        """
        Function used to check the validity of the next char being an integer. Checks are
        based on what the current token type is
        :param current_char:
        :return None:
        """
        if self.current_token_type is Token.NONE or self.current_token_type is Token.INTEGER:
            # append char to the running integer value being formed
            self.sub_string += current_char
        elif self.current_token_type is Token.OPERATOR:
            # need to create a token for the operator
            self.tokens.append(self.sub_string)
            self.sub_string = ''
            self.sub_string += current_char

        self.current_token_type = Token.INTEGER

    def check_operator(self, current_char):
        """
        Function used to check the validity of the next char being an operator. Checks are
        based on what the current token type is
        :param current_char:
        :return None:
        """
        if self.current_token_type is Token.NONE:
            # needs to error since we cannot start an expression with an operator
            print('Error expression cannot start with an operator')
        elif self.current_token_type is Token.OPERATOR:
            # needs to error since we cannot have two operators in a row
            print('Error, an operator cannot be followed by an operator')
        elif self.current_token_type is Token.INTEGER:
            # need to create a token for the integer
            self.tokens.append(self.sub_string)
            self.sub_string = ''
            self.sub_string += current_char

        self.current_token_type = Token.OPERATOR

    def add_integer_token(self, current_integer):
        """
        Function used to add an integer token to the list of tokens
        :param current_integer:
        :return None:
        """
        self.tokens.append(current_integer)
        self.sub_string = ''
        self.current_token_type = Token.INTEGER

    def decrypt_expression(self):
        """
        Function used to decrypt the expression passed and create tokens
        :return None:
        """
        current_char = ''

        for i in range(len(self.expression)):
            self.current_position = i
            current_char = self.expression[i]

            if current_char in self.integers_list:
                self.check_integer(current_char)
            if current_char in self.operators_list:
                self.check_operator(current_char)
            if current_char == ' ':
                continue

        if self.sub_string in self.operators_list:
            print('Error cannot end expression with an operator')
        else:
            self.add_integer_token(self.sub_string)

