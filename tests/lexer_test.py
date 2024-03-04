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
        source: str = '=+/-*<>!'
        lexer : Lexer = Lexer(source)

        tokens: List[Token]= []
        for i in range(len(source)):
            tokens.append(lexer.next_token())

        expected_tokens: List[Token] = [
            Token(TokenType.ASSIGN, '='),
            Token(TokenType.PLUS, '+'),
            Token(TokenType.DIV, '/'),
            Token(TokenType.MINUS, '-'),
            Token(TokenType.MULT, '*'),
            Token(TokenType.LT, '<'),
            Token(TokenType.GT, '>'),
            Token(TokenType.NEGATION, '!'),
            
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
        
        self.assertEquals(tokens , expected_tokens)

    def test_function_declaration(self)-> None:
        source: str = '''
            def suma(x,y) {
                x + y
            };
    '''
        lexer: Lexer = Lexer(source)    
        tokens: List[Token] = []
        for i in range(13):
            tokens.append(lexer.next_token())
        expected_tokens: List[Token] = [
            Token(TokenType.FUNCTION, 'def'),
            Token(TokenType.IDENT, 'suma'),
            Token(TokenType.LPAREN, '('),
            Token(TokenType.IDENT, 'x'),
            Token(TokenType.COMMA, ','),
            Token(TokenType.IDENT, 'y'),
            Token(TokenType.RPAREN, ')'),
            Token(TokenType.LBRACE, '{'),
            Token(TokenType.IDENT, 'x'),
            Token(TokenType.PLUS, '+'),
            Token(TokenType.IDENT, 'y'),
            Token(TokenType.RBRACE, '}'),
            Token(TokenType.SEMICOLON, ';'),  
        ]

        self.assertEquals(tokens, expected_tokens)

    def test_control_statement(self)-> None:
        source: str = '''
            if(5<10){
                return True
            } else {
                return False
            }
        '''

        lexer: Lexer = Lexer(source)    
        tokens: List[Token] = []
        for i in range(15):
            tokens.append(lexer.next_token())
        expected_tokens: List[Token] = [
            Token(TokenType.IF, 'if'),
            Token(TokenType.LPAREN, '('),
            Token(TokenType.INT, '5'),
            Token(TokenType.LT, '<'),
            Token(TokenType.INT, '10'),
            Token(TokenType.RPAREN, ')'),
            Token(TokenType.LBRACE, '{'),
            Token(TokenType.RETURN, 'return'),
            Token(TokenType.TRUE, 'True'),
            Token(TokenType.RBRACE, '}'),
            Token(TokenType.ELSE, 'else'),
            Token(TokenType.LBRACE, '{'),
            Token(TokenType.RETURN, 'return'),
            Token(TokenType.FALSE, 'False'),
            Token(TokenType.RBRACE, '}'),  
        ]

        self.assertEquals(tokens, expected_tokens)

    def test_two_character_operator(self)-> None:
        source: str = '''
            10==10;
            10 != 9;
        '''
        lexer: Lexer = Lexer(source)

        tokens: List[Token] = []
        for i in range(8):
            tokens.append(lexer.next_token())
        
        expected_tokens: List[Token] = [
            Token(TokenType.INT, '10'),
            Token(TokenType.EQ, '=='),
            Token(TokenType.INT, '10'),
            Token(TokenType.SEMICOLON, ';'),
            Token(TokenType.INT, '10'),
            Token(TokenType.NOT_EQ, '!='),
            Token(TokenType.INT, '9'),
            Token(TokenType.SEMICOLON, ';'),
        ]

        self.assertEqual(tokens, expected_tokens)
        