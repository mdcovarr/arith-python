#!/usr/bin/python
"""
    Script capable of reading expressions in the arith language and
    returning a abstract syntax tree.
"""
from arith import Arith

def main():
    """
        Main enterence of the program.
    """
    app = Arith()

    app.run()

if __name__ == '__main__':
    main()
