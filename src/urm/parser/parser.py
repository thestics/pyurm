import typing as tp

from urm.objects import Command
from urm.parser.reader import Reader
from urm.parser.token import Token, TokenType
from urm.parser.grammar import GRAMMAR, CMD_GRAMMAR
from urm.objects import J, S, Z, T


def _read_stream_with_pattern(
        stream_reader: Reader,
        token_type_pattern: tp.List[TokenType],
        exc=Exception()
):
    res = []
    for token_type in token_type_pattern:
        real_token: tp.Optional[Token] = stream_reader.get_next()
        if real_token is None or real_token.token_type != token_type:
            raise exc
        res.append(real_token)
    return res


def _convert_cmd_tokens_to_cmd(valid_tokens: tp.List[Token]):
    cmd_token, *rest = valid_tokens
    cmd_token: Token
    
    if cmd_token.token_type == TokenType.Z:
        _, num, _ = rest
        return Z(num.token_value)
    elif cmd_token.token_type == TokenType.S:
        _, num, _ = rest
        return S(num.token_value)
    elif cmd_token.token_type == TokenType.T:
        _, num1, _, num2, _ = rest
        return T(num1.token_value, num2.token_value)
    elif cmd_token.token_type == TokenType.J:
        _, num1, _, num2, _, num3, _ = rest
        return J(num1.token_value, num2.token_value, num3.token_value)


def parse_token_stream(input: tp.List[Token]) -> tp.List[Command]:
    """
    Convert parsed tokens into a list of commands
    
    :param input: List of tokens
    :return:
    """
    res = []
    if not input:
        return res
    input_reader = Reader(input)
    cur_token: Token = input_reader.get_next()

    while cur_token is not None:
        next_token: tp.Optional[Token] = input_reader.peek_next()
        if not next_token:
            return res

        if next_token.token_type not in GRAMMAR[cur_token.token_type]:
            raise Exception(f"Unexpected sequence of tokens: "
                            f"`{cur_token}` `{next_token}`")
        
        if cur_token.token_type in \
            {TokenType.J, TokenType.S, TokenType.Z, TokenType.T}:
            next_tokens_patt = CMD_GRAMMAR[cur_token.token_type]
            cmd_tokens = _read_stream_with_pattern(
                input_reader,
                next_tokens_patt,
                Exception(f"Unexpected tokens after: {cur_token}"))
            cmd = _convert_cmd_tokens_to_cmd([cur_token, *cmd_tokens])
            res.append(cmd)

        cur_token = input_reader.get_next()
    return res