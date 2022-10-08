import enum


class TokenType(enum.Enum):
    J = 'J'
    Z = 'Z'
    T = 'T'
    S = 'S'
    NUM = 'NUM'
    COMA = ','
    LPAR = '('
    RPAR = ')'


class Token:
    def __init__(self, t_type: TokenType, line: int, col: int, t_value=None):
        self.token_type = t_type
        self._line = line
        self._col = col
        self.token_value = t_value

    def __repr__(self):
        return f"Token({self.token_type}, {self._line}, {self._col})"
    
    def __str__(self):
        return f"{self.token_type} at {self._line}:{self._col}"
