# arith-python
Implementation of the arith language in python

## Table of Contents
[Clone Repository](#Clone-repository)

[Software Requirements](#Software-requirements)

[Documentation](#Software-documentation)

[Build Project](#Build-project)

[Test Software](#Test-software)


# Clone repository
You need to clone recursively due to `arith-python` containing
a submodule named `cse210A-asgtest`
```
git clone --recursive https://github.com/mdcovarr/arith-python.git
```

# Development Enviornment
Software was developed on `CentOS 7`


# Software requirements
Required software in order to run **arith-python** software
## Install Python 3
```
sudo yum -y install python36
```
## Install Pip 3
```
sudo yum -y install python3-pip
```

## Install PyInstaller
```
sudo pip3 install pyinstaller
```

# Directories
**arith-python/cse210A-asgtest**
* Directory of the Teaching Assistants Testing Software

**arith-python/src**
* Soruce code of implementation


# Software documentation
## Classs **Arith** (arith.py)
Class used by the main to run software.


## Class **InputReader** (input_reader.py)
Class used to read from stdin. Once string is read,
we validate that there are only valid characters
in the input. Else we throw an Exception. If all characters
are valid, then we create tokens of input

Example
```
stdin: '9 * 9 + !'
stdout: Error Invalid Character!
```

Example
```
stdin: 4 * 8 + 11
tokens = ['4', '*', '8', '+', '11']
```


## Class **Parser** (parser.py)
Class used to validate the format of the expression, like
not having the expression end with an operator e.g., '+',
'-', '*'. And making sure that there are no expressions
with invalid format of operators e.g., '9 * - - - 9'. If
expression is invalid, an Exception is thrown and the
Abstract Syntax Tree is not formed. However, the expression is validate the Parser class creates the
Abstract Syntax Tree.


## Class **Interpreter** (interpreter.py)
Class used to interpret the Abstract Syntax Tree and
return the result of the expression.


## Parent Class **ASTNode** (ast_node.py)
Abstract class representing a node in the Abstract
Syntac Tree (AST).

#### Child Class **ASTInteger** (ast_integer.py)
Class representing an integer node in the AST.


#### Child Class **ASTOperator** (ast_operator.py)
Class representing an operator node in the AST. An
operator such as '+', '-' or '*'.


## Class **ASTToken** (ast_token.py)
Enum class representing all valid tokens
```
class ASTToken(enum.Enum):
    NONE = 1
    INTEGER = 2
    PLUS = 3
    MINUS = 4
    MULT = 5

```


## Class **Expression** (expression.py)
Class to encapsulate the expression to be added to the
currently built AST. Expression object encapsulates
a ASTOperator and a ASTInteger.


# Build project
### Installing pyinstaller
If you have installed **pip3** and **python** you can install pyinstaller with command:
```
sudo make init
```


### Build **arith** executable
executable will be created at **arith-python/arith**.
To make arith executable run command:
```
make arith
```


# Test software
Once you have built the **arith** executable to test **arith** executable with the
cse210A-nsgtest repository tests run command:
```
make test
```
