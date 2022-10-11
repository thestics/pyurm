import typing as tp


class Command:
    def run(self, registers: tp.DefaultDict[int, int]) -> tp.Optional[int]:
        pass
    
    def __repr__(self):
        return str(self)

class Z(Command):
    def __init__(self, n):
        self._n = n
        
    def run(self, registers: tp.DefaultDict[int, int]) -> tp.Optional[int]:
        registers[self._n] = 0
        return None
    
    def __str__(self):
        return f"Z({self._n})"

class S(Command):
    def __init__(self, n):
        self._n = n
    
    def run(self, registers: tp.DefaultDict[int, int]) -> tp.Optional[int]:
        registers[self._n] += 1
        return None
    
    def __str__(self):
        return f"S({self._n})"


class T(Command):
    """Transfer from N to M"""
    def __init__(self, n, m):
        self._n, self._m = n, m
    
    def run(self, registers: tp.DefaultDict[int, int]) -> tp.Optional[int]:
        registers[self._m] = registers[self._n]
        return None
    
    def __str__(self):
        return f"T({self._n}, {self._m})"

class J(Command):
    def __init__(self, m, n, q):
        self._m, self._n, self._q = m, n, q
    
    def run(self, registers: tp.DefaultDict[int, int]) -> tp.Optional[int]:
        r_m = registers[self._m]
        r_n = registers[self._n]
        if r_m == r_n:
            return self._q
        return None
    
    def __str__(self):
        return f"J({self._m}, {self._n}, {self._q})"