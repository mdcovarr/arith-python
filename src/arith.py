#!/usr/bin/python
"""
    Helper class used to run the arith software
"""
import sys
import os
from input_reader import InputReader
from parser import Parser
from ast_integer import ASTInteger
from ast_operator import ASTOperator


class Arith:
    """
        Arith class used to run the arith expression tokening language
    """
    def __init__(self):
        """
        Default constructor for the Arith helper class
        """
        self.reader = InputReader()
        self.parser = None
        self.nodes = []

    def create_nodes(self, tokens):
        self.nodes = []

        for token in tokens:
            if token == '*' or token == '+':
                current_node = ASTOperator('', '', token)
            else:
                current_node = ASTInteger(token)
            self.nodes.append(current_node)

    def create_tree(self):
        pass

    def parse(self):
        """
        Function which takes a string and attempts to return an abstract syntax
        tree if valid input to arith language
        """
        self.create_nodes(self.reader.get_tokens())

    def run(self):
        """
        Function used to run the program, which prompts user to enter an expression
        and returns a abstract syntax tree if input is valid for the arith language
        :return None:
        """
        while True:
            try:
                self.reader.get_expression()
                self.reader.decrypt_expression()
                self.create_nodes(self.reader.get_tokens())
                self.parser = Parser(self.nodes)
                self.parser.parse()
                self.parser.print_ast()
            except KeyboardInterrupt:
                print("\nGracefully shutting down...")
                try:
                    sys.exit(0)
                except SystemExit:
                    os._exit(0)

            self.reader.reset_reader()
