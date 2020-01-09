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

    def parse(self):
        """
        Function which takes a string and attempts to return an abstract syntax
        tree if valid input to arith language
        """
        # first need to parse
        self.tokens = self.expression.split()


    def run(self):
        """
        Function used to run the program, which prompts user to enter an expression
        and returns a abstract syntax tree if input is valid for the arith language
        :return None:
        """
        while True:
            try:
                self.expression = raw_input("Enter expression to be parsed: ")
                self.parse()
            except KeyboardInterrupt:
                print("\nGracefully shutting down...")
                try:
                    sys.exit(0)
                except SystemExit:
                    os._exit(0)
