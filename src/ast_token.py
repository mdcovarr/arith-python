"""
    enum class to keep track of the token types
"""
import enum


class ASTToken(enum.Enum):
    """
    Class to keep trace of the Token types
    """
    NONE = 1
    INTEGER = 2
    PLUS = 3
    MINUS = 4
    MULT = 5
