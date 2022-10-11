import argparse
from pathlib import Path
from collections import defaultdict

from urm.parser.tokenizer import tokenize_str
from urm.parser.parser import parse_token_stream
from urm.runner import Runner
from urm.utils import annotate_commands

usage = "usage: pyurm [src file]"


def read_and_validate_params() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="URM compiler")
    parser.add_argument('src', type=str)
    parser.add_argument(
        '--annotate', dest='annotate', action='store_true', default=False,
        help='Annotate parsed commands with their indexes')
    args = parser.parse_args()
    path = Path(args.src)
    if not path.exists():
        exit(f"`{path}` does not exist")
    if path.is_dir():
        exit(f"`{path}` is a directory")
    return args


def main():
    params = read_and_validate_params()
    with open(params.src) as fd:
        src = fd.read()
    tokenized = tokenize_str(src)
    commands = parse_token_stream(tokenized)
    if params.annotate:
        annotate_commands(commands)
        return
    registers = defaultdict(int)
    runner = Runner(commands, registers)
    runner.run()
    print({k: v for k, v in sorted(registers.items())})


if __name__ == '__main__':
    main()
