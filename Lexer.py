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
    r"//": "comment",  # r".." indicates a raw string to avoid escape sequences being detected
    r"(": "leftParen",
    r")": "rightParen",
    r"[": "leftBracket",
    r"]": "rightBracket",
    r"{": "leftBrace",
    r"}": "rightBrace",
    r".": "dot",
    r"+": "plus",
    r"-": "minus",
    r"*": "multiply",
    r"/": "divide",
    r"%": "modulus",
    r"<": "lessThan",
    r">": "greaterThan",
    r"=": "assignment",
    r";": "semicolon",
    r",": "comma",
    r"++": "increment",
    r"--": "decrement",
    r"<=": "lessThanEq",
    r">=": "greaterThanEq",
    r"==": "logicEqual",
    r"&&": "logicAnd",
    r"||": "logicOr",
    r"!": "logicNot",
    r"&": "bitAnd",
    r"\|": "bitOr",
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

    def deterministic_finite_automata(self, current_line):
        """
        Processes current line of code and adds valid tokens to the token stream, one lexeme at a time.
        """
        lexeme_sequence = []
        lexeme_sequence.append(current_line[0])
        char_index = 0

        # Outer Loop
        # Loops through each char of the current_line
        while char_index < len(current_line):

            # if initial_char = (a-z)(A-Z) then lexeme will either be an identifier, keyword or error
            # keep looping until a non-letter is detected, check if letter str is a keyword, if not then
            # assign it an identifer token
            if str(lexeme_sequence[0]).isalpha():
                char_index += 1

                # Keep adding chars until non alphanumeric is found or end of list
                while char_index < len(current_line) and current_line[char_index].isalnum():  #######################-1

                    lexeme_sequence.append(current_line[char_index])
                    char_index += 1

                # Check if keyword
                type_buffer = TOKEN_TYPES.get("".join(lexeme_sequence), "identifer")
                if type_buffer != "identifer":
                    self._tokenStream.append(Token(type_buffer, type_buffer))
                # Else make it an identifer
                else:
                    self._tokenStream.append(Token(type_buffer, "".join(lexeme_sequence)))
                # char_index -= 1  ##### I hate this but it was a fix -_- ################################################


            # if initial_char is a number(0-9) then keep looping until a non number is detected. Then assign the lexeme
            # a number token.
            elif str(lexeme_sequence[0]).isdigit():
                char_index += 1

                # Keep looping until nondigit or end of list
                while char_index < len(current_line) and current_line[char_index].isdigit():  ########################-1
                    lexeme_sequence.append(current_line[char_index])
                    char_index += 1
                # Add number token to token stream
                self._tokenStream.append(Token("number", "".join(lexeme_sequence)))
                # char_index -= 1  ##### I hate this but it was a fix -_- ##################################################


            # if initial_char is any operator symbol and the following char is not another valid operator symbol then
            # lexeme will be assigned its respective single operator token. If a second operator is detected following
            # the first then the token will be its respective valid double operator token ie. +=, ++, ==. The only
            # exception to this is if a double forward slash operator is detected //. this means that the token assigned
            # will be a comment, the // and all characters that come after the // will be a valid part of the comment
            # which doesnt end until the next newline character.

            else:
                # first char will always be an operator, save it
                type_buffer = TOKEN_TYPES.get("".join(str(lexeme_sequence[0])), "error")
                # char_index += 1

                if char_index < len(current_line):
                    # Add next char to list, so we can check if double operator
                    lexeme_sequence.append(current_line[char_index])

                    # Grabs double operator from dictionary
                    # type_buffer = TOKEN_TYPES.get("".join(lexeme_sequence), "error")
                    # How bout lets not alter type_buffer
                    double_op = TOKEN_TYPES.get("".join(lexeme_sequence), "error")

                    # Is a Comment, add rest of current line into lexeme
                    if double_op == "comment":
                        lexeme_sequence.extend(current_line[char_index:])
                        char_index = len(current_line)  # Skip to the end
                        self._tokenStream.append(Token(double_op, "".join(lexeme_sequence)))

                    # Is a Double Operator
                    elif double_op != "error":
                        self._tokenStream.append(Token(double_op, "".join(lexeme_sequence)))

                    # Is a Single Operator
                    else:
                        self._tokenStream.append(Token(type_buffer, lexeme_sequence[0]))
                                            # ##### I hate this but it was a fix -_-

                # Is last char of list
                else:
                    # submit original operator
                    self._tokenStream.append( type_buffer, "".join(str(lexeme_sequence[0])))

            # Debugging
            debug = self._tokenStream[-1]  # ##### I hate this but it was a fix -_-
            print(debug.token_type, debug.token_details)

            # Setup for next loop, ie next lexeme
            char_index += 1
            lexeme_sequence = [current_line[char_index]] if char_index < len(
                current_line) else []  # ##### I hate this but it was a fix -_-
            type_buffer = None
            double_op = None

        return 0

########################################################################################################################


