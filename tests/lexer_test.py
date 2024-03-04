from unittest import TestCase
from typing import List
from lp.my_token import Token, TokenType
from lp.lexer import  Lexer
class LexerTest(TestCase):

    def test_illegal(self) -> None:
        source: str = "¡¿@"
        lexer : Lexer = Lexer(source)

        tokens: List[Token]= []
        for i in range(len(source)):
            tokens.append(lexer.next_token())

        expected_tokens: List[Token] = [
            Token(TokenType.ILLEGAL, '¡'),
            Token(TokenType.ILLEGAL, '¿'),
            Token(TokenType.ILLEGAL, '@'),
        ]

        self.assertEqual(tokens, expected_tokens)



    def test_one_character_operator(self) -> None:
        source: str = '=+'
        lexer : Lexer = Lexer(source)

        tokens: List[Token]= []
        for i in range(len(source)):
            tokens.append(lexer.next_token())

        expected_tokens: List[Token] = [
            Token(TokenType.ASSIGN, '='),
            Token(TokenType.PLUS, '+'),
            
        ]

        self.assertEqual(tokens, expected_tokens)

    def test_eof(self) -> None:
        source: str = '+'
        lexer : Lexer = Lexer(source)

        tokens: List[Token]= []
        for i in range(len(source)+1):
            tokens.append(lexer.next_token())

        expected_tokens: List[Token] = [
            Token(TokenType.PLUS, '+'),
            Token(TokenType.EOF, ''),    
        ]

        self.assertEqual(tokens, expected_tokens)

    def test_delimiters(self) -> None:
        source = '(){},;'
        lexer: Lexer = Lexer(source)

        tokens: List[Token] = []
        for i in range(len(source)):
            tokens.append(lexer.next_token())

        expected_tokens: List[Token] = [
            Token(TokenType.LPAREN, '('),
            Token(TokenType.RPAREN, ')'),
            Token(TokenType.LBRACE, '{'),
            Token(TokenType.RBRACE, '}'),
            Token(TokenType.COMMA, ','),
            Token(TokenType.SEMICOLON, ';'),
        ]

        self.assertEquals(tokens, expected_tokens)

    def test_assignment(self) -> None:
        source: str = 'var cinco = 5'
        lexer: Lexer = Lexer(source)
        tokens: List[Token] = []
        for i in range(4):
            tokens.append(lexer.next_token())
        expected_tokens: List[Token] = [
            Token(TokenType.LET, 'var'),
            Token(TokenType.IDENT, 'cinco'),
            Token(TokenType.ASSIGN, '='),
            Token(TokenType.INT, '5'), 
        ]
        
        self.assertEquals(tokens, expected_tokens)

