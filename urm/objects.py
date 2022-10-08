import typing as tp


class Command:
    def run(self, registers: tp.DefaultDict[int, int]) -> tp.Optional[int]:
        pass


class Z(Command):
    def __init__(self, n):
        self._n = n
        
    def run(self, registers: tp.DefaultDict[int, int]) -> tp.Optional[int]:
        registers[self._n] = 0
        return None


class S(Command):
    def __init__(self, n):
        self._n = n
    
    def run(self, registers: tp.DefaultDict[int, int]) -> tp.Optional[int]:
        registers[self._n] += 1
        return None


class T(Command):
    def __init__(self, n, m):
        self._n, self._m = n, m
    
    def run(self, registers: tp.DefaultDict[int, int]) -> tp.Optional[int]:
        registers[self._n] = registers[self._m]
        return None


class J(Command):
    def __init__(self, m, n, q):
        self._m, self._n, self._q = m, n, q
    
    def run(self, registers: tp.DefaultDict[int, int]) -> tp.Optional[int]:
        r_m = registers[self._m]
        r_n = registers[self._n]
        if r_m == r_n:
            return self._q
        return None
