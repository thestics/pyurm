class Reader:
    """
    Wrapper around indexable objects, to allow lookahead operations
    """
    def __init__(self, src):
        self._src = src
        self._cur_idx = 0

    def peek_next(self):
        if self._cur_idx >= len(self._src):
            return None
        return self._src[self._cur_idx]
    
    def before_get_next_hook(self, rv):
        """Hook which shall be triggered before next item is returned"""
        pass
    
    def get_next(self):
        if self._cur_idx >= len(self._src):
            return None
        res = self._src[self._cur_idx]
        self._cur_idx += 1
        self.before_get_next_hook(res)
        return res
    
    def get_copy(self):
        obj = self.__class__(self._src)
        obj._cur_idx = self._cur_idx
        return obj
    

class StringReader(Reader):
    """
    Wrapper around string. Additionally, keeps track of current line and column
    """
    def __init__(self, src):
        super().__init__(src)
        self._cur_line = 1
        self._cur_col = 1

    @property
    def line(self):
        return self._cur_line
    
    @property
    def col(self):
        return self._cur_col
    
    def before_get_next_hook(self, rv):
        if rv == '\n':
            self._cur_line += 1
            self._cur_col = 1
        else:
            self._cur_col += 1
    
    def get_copy(self):
        obj = super().get_copy()
        obj._cur_line = self._cur_line
        obj._cur_col = self._cur_col
        return obj