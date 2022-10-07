import typing as tp
from collections import defaultdict

from .objects import Command


class Runner:
    def __init__(self,
                 instruction_set: tp.List[Command],
                 registers_cfg: tp.DefaultDict[int, int] = None):
        assert len(instruction_set) > 0
        if registers_cfg is None:
            registers_cfg = defaultdict(int)
        self._registers = registers_cfg
        self._instructions = instruction_set
    
    def run(self):
        cur_instruction = 0
        max_instruction = len(self._instructions) - 1

        while cur_instruction <= max_instruction:
            instruction: Command = self._instructions[cur_instruction]
            next_idx = instruction.run(self._registers)
            cur_instruction = cur_instruction + 1 if next_idx is None else next_idx
