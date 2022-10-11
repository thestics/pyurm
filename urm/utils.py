import math
import typing as tp

from urm.objects import Command


def annotate_commands(commands: tp.List[Command]):
    idx_size = math.ceil(math.log10(len(commands)))
    pattern = "I_{i:0>" + str(idx_size) + "}: {c}"
    for i, c in enumerate(commands):
        print(pattern.format(i=i, c=c))
