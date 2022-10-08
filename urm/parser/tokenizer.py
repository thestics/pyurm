import typing as tp
import string

from urm.parser.token import Token, TokenType
from urm.parser.reader import StringReader


space_symbols = "\n\t "


def tokenize_str(input: str) -> tp.List[Token]:
    reader = StringReader(input)
    tokens = []
    
    while reader.peek_next() is not None:
        char = reader.get_next()

        # special symbols
        if char in space_symbols:
            continue
        if char in 'JZTS(),':
            token_type = TokenType._value2member_map_[char]
            tokens.append(Token(token_type, reader.line, reader.col))
        # number identifier
        elif char in string.digits:
            num_chars = [char]
            while reader.peek_next() in string.digits:
                num_chars.append(reader.get_next())
            num = int(''.join(num_chars))
            tokens.append(
                Token(TokenType.NUM, reader.line, reader.col, t_value=num)
            )
        else:
            raise Exception(f'Unexpected symbol {char} on '
                            f'{reader.line}:{reader.col}')
    return tokens
