# lexer.py

# Global Dictionary of all valid Token Types
TOKEN_TYPES = {
    # Keywords
    "int"       : "int",
    "return"    : "return",
    "switch"    : "switch",
    "float"     : "float",
    "while"     : "while",
    "else"      : "else",
    "case"      : "case",
    "char"      : "char",
    "for"       : "for",
    "goto"      : "goto",
    "unsigned"  : "unsigned",
    "main"      : "main",
    "break"     : "break",
    "continue"  : "continue",
    "void"      : "void",

    # Identifiers and Numbers
    "identifier": "identifier",
    "number"    : "number",

    # Operators
    "comment"       : r"//", # r".." indicates a raw string to avoid escape sequences being detected
    "leftParen"     : r"\(",
    "rightParen"    : r"\)",
    "leftBracket"   : r"\[",
    "rightBracket"  : r"\]",
    "leftBrace"     : r"\{",
    "rightBrace"    : r"\}",
    "dot"           : r"\.",
    "plus"          : r"\+",
    "minus"         : r"\-",
    "multiply"      : r"\*",
    "divide"        : r"\/",
    "modulus"       : r"%",
    "lessThan"      : r"<",
    "greaterThan"   : r">",
    "assignment"    : r"=",
    "semicolon"     : r";",
    "comma"         : r",",
    "increment"     : r"\+\+",
    "decrement"     : r"\-\-",
    "lessThanEq"    : r"<=",
    "greaterThanEq" : r">=",
    "logicEqual"    : r"==",
    "logicAnd"      : r"&&",
    "logicOr"       : r"\|\|",
    "logicNot"      : r"!",
    "bitAnd"        : r"&",
    "bitOr"         : r"\|",
}


class Token:
    """
    Represents a lexical token.
    A somewhat abstract lexical classification of a valid group of characters.
    ie. identifier, comment, main, if, leftParen, rightParen...
    """
    def __init__(self, token_type="", token_details=""):
        self.token_type    = token_type
        self.token_details = token_details
########################################################################################################################

class Lexer:
    """
    Represents a lexical analyzer.

    Attributes:
        _source_code (str):
        _token_stream (list):
    """

    def __init__(self, source_code=""):
        """
        Initializes a Lexer instance.
        """
        self.__source_code = source_code
        self._tokenStream = []

    # F
    def set_source_code(self, sourceCode=""):
        """
        Sets atrribute _source_code
        """
        self.sourceCode = sourceCode


    def input_file(self, fileName=""):
        """
        Reads a user specified text file, assigns it to _source_code.
        """
    def run_lexer(self) -> None:
        """
        Creates a token stream from the source code. The code is scanned left-to-right, line-by-line and uses
        a DFA to build valid lexems and assign cooresponding tokens.
        """
        # Break _source_code into a list of str, one str per newline
        line_list = []

        # Loops for each newline in _source_code
        for current_line in line_list:
            # Feed current line to the DFA
            curr_line_tokens = self.deterministic_finite_automata(current_line)

        # Add token line to the output file


    def deterministic_finite_automata(self, current_line) -> str:
        """
        Processes current line of code and returns a list of token_type attribute grabbed upon each token's creation.
        """
        lexeme_sequence = []
        lexeme_sequence.append(current_line[0])
        char_index = 0

        # Outer Loop
        # Loops through each char of the current_line
        while char_index < len(current_line):

            # if initial_char = (a-z)(A-Z)(0-9) then lexeme will either be an identifier, keyword or error
            # keep looping until a non-letter is detected, check if letter str is a keyword, if not then
            # assign it an identifer token
            if lexeme_sequence[0].isalpha():
                char_index += 1

                # Keep adding chars until non alphanumeric is found or end of list
                while current_line[char_index].isalnum() and char_index < len(current_line):
                    lexeme_sequence.append(current_line[char_index])
                    char_index += 1

                # Check if keyword
                type_buffer = TOKEN_TYPES.get(lexeme_sequence, "identifer")
                if type_buffer != "identifer":
                    self._tokenStream.append(Token(type_buffer, type_buffer))
                # Else make it an identifer
                else:
                    self._tokenStream.append(Token(type_buffer, lexeme_sequence))


            # if initial_char is a number(0-9) then keep looping until a non number is detected. Then assign the lexeme
            # a number token.
            elif lexeme_sequence[0].isdigit():
                char_index += 1

                # Keep looping until nondigit or end of list
                while current_line[char_index].isdigit() and char_index < len(current_line):
                    lexeme_sequence.append(current_line[char_index])
                    char_index += 1
                # Add number token to token stream
                self._tokenStream.append(Token("number", lexeme_sequence))


            # if initial_char is any operator symbol and the following char is not another valid operator symbol then
            # lexeme will be assigned its respective single operator token. If a second operator is detected following
            # the first then the token will be its respective valid double operator token ie. +=, ++, ==. The only
            # exception to this is if a double forward slash operator is detected //. this means that the token assigned
            # will be a comment, the // and all characters that comme after the // will be a valid part of the comment
            # which doesnt end until the next newline character.
            else:
                # first char will always be an operator
                type_buffer = TOKEN_TYPES.get(lexeme_sequence[0])
                if False:
                    break

            # Setup for next loop, ie next lexeme
            char_index += 1
            lexeme_sequence.clear()
            lexeme_sequence.append([char_index])
            type_buffer = None

        return 0

########################################################################################################################


