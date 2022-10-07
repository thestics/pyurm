# Example of interface usage for URM library

from collections import defaultdict

from urm.parser.tokenizer import tokenize_str
from urm.parser.parser import parse_token_stream
from urm.runner import Runner

s = """
S(0)
S(1)
S(1)
T(0, 1)
"""
tokenized = tokenize_str(s)
parsed = parse_token_stream(tokenized)
registers = defaultdict(int)
runner = Runner(parsed, registers)
runner.run()
print(registers)