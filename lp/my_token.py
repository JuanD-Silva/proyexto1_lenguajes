from enum import (
    auto,
    Enum,
    unique,
)
from typing import NamedTuple, Dict


@unique
class TokenType(Enum):
    ASSIGN = auto()
    COMMA = auto()
    ELSE = auto()
    EOF = auto()
    EQ = auto()
    EXC = auto()
    DIV = auto()
    FALSE = auto()
    FUNCTION = auto()
    GT = auto()
    IDENT = auto()
    IF = auto()
    ILLEGAL = auto()
    INT = auto()
    LBRACE = auto()
    LET = auto()
    LPAREN = auto()
    LT = auto()
    MINUS = auto()
    MULT = auto()
    NEGATION = auto()
    NOT_EQ =auto()
    PLUS = auto()
    RBRACE = auto()
    RETURN = auto()
    RPAREN = auto()
    SEMICOLON = auto()
    TRUE = auto()


class Token(NamedTuple):
    token_type: TokenType
    literal: str

    def __str__(self) -> str:
        return f'Type: {self.token_type}, Literal: {self.literal}'
    

def lookup_token_type(literal: str) -> TokenType:
    keywords: Dict[str,TokenType] = {
        'False': TokenType.FALSE,
        'def': TokenType.FUNCTION,
        'return': TokenType.RETURN,
        'if':TokenType.IF,
        'else': TokenType.ELSE,
        'elsif': TokenType.ELSE,
        'True':TokenType.TRUE,
        'var': TokenType.LET
    }

    return keywords.get(literal, TokenType.IDENT)