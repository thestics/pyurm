from collections import defaultdict
import sys
from pathlib import Path

from urm.parser.tokenizer import tokenize_str
from urm.parser.parser import parse_token_stream
from urm.runner import Runner


usage = "usage: pyurm [src file]"


def read_and_validate_params() -> Path:
    params = sys.argv
    if not len(params) == 2:
        exit(usage)
    path = Path(params[1])
    if not path.exists():
        exit(f"`{path}` does not exist")
    if path.is_dir():
        exit(f"`{path}` is a directory")
    return path


def main():
    path = read_and_validate_params()
    with open(path) as fd:
        src = fd.read()
    tokenized = tokenize_str(src)
    parsed = parse_token_stream(tokenized)
    registers = defaultdict(int)
    runner = Runner(parsed, registers)
    runner.run()
    print({k: v for k, v in sorted(registers.items())})


if __name__ == '__main__':
    main()
