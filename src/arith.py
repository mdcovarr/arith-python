#!/usr/bin/python
"""
    Helper function used to run the arith software
"""
import sys
import os

class Arith:
    """
        Arith class used to run the arith expression tokening language
    """
    def __init__(self):
        """
        Default constructor for the Arith helper class
        """
        self.expression = ""
        self.tokens = []
        self.valid_tokens = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ' ', '-', '+', '*']

    def parse(self):
        """
        Function which takes a string and attempts to return an abstract syntax
        tree if valid input to arith language
        """
        # 1st validate the expression
        self.validate_expression()

        # 2st need to parse
        self.tokens = self.expression.split()

    def validate_expression(self):
        """
        Function used to validate the expression as valid syntax
        :return is_valid: boolean that is true if expression is valid, false else
        """
        is_valid = False
        for character in self.expression:
            if character not in self.valid_tokens:
                return is_valid

        is_valid = True
        return is_valid

    def run(self):
        """
        Function used to run the program, which prompts user to enter an expression
        and returns a abstract syntax tree if input is valid for the arith language
        :return None:
        """
        while True:
            try:
                self.expression = raw_input("Enter expression to be parsed: ")
                if self.validate_expression():
                    self.parse()
                else:
                    print("'{0} is an invalid expression'".format(self.expression))
            except KeyboardInterrupt:
                print("\nGracefully shutting down...")
                try:
                    sys.exit(0)
                except SystemExit:
                    os._exit(0)
