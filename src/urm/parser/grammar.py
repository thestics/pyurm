from .token import TokenType


GRAMMAR = {
    TokenType.J: {TokenType.LPAR},
    TokenType.Z: {TokenType.LPAR},
    TokenType.T: {TokenType.LPAR},
    TokenType.S: {TokenType.LPAR},
    TokenType.LPAR: {TokenType.NUM},
    TokenType.NUM: {TokenType.COMA, TokenType.RPAR},
    TokenType.RPAR: {TokenType.J, TokenType.Z, TokenType.T, TokenType.S},
}


_ONE_PARAM_CMD = (
    TokenType.LPAR, TokenType.NUM, TokenType.RPAR
)
_TWO_PARAM_CMD = (
    TokenType.LPAR, TokenType.NUM, TokenType.COMA, TokenType.NUM,
    TokenType.RPAR
)
_THREE_PARAM_CMD = (
    TokenType.LPAR, TokenType.NUM, TokenType.COMA, TokenType.NUM,
    TokenType.COMA, TokenType.NUM, TokenType.RPAR)


CMD_GRAMMAR = {
    TokenType.J: _THREE_PARAM_CMD,
    TokenType.Z: _ONE_PARAM_CMD,
    TokenType.T: _TWO_PARAM_CMD,
    TokenType.S: _ONE_PARAM_CMD
}
