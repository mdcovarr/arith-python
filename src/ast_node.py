#!/usr/bin/env python
"""
    Abstract parent class for the nodes in the Abstract Syntax Tree
"""


class ASTNode(object):
    def __init__(self):
        self.left = None
        self.right = None
