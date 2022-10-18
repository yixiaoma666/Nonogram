import numpy as np

class Solve:
    def __init__(self, _file) -> None:
        self.file_name = _file
        self.row = 0
        self.col = 0
        self.row_hint_list = []
        self.col_hint_list = []
        self.board: np.ndarray # -1错，0空，1对

    def _read_txt(self):
        with open(self.file_name) as f:
            s = f.read()
        s_list = s.split("\n")
        try:
            while True:
                s_list.remove("")
        except ValueError:
            pass
        self.row, self.col = tuple(map(int, s_list.pop(0).split(",")))
        for _ in range(self.row):
            self.row_hint_list.append(list(map(int, s_list.pop(0).split(","))))
        for _ in range(self.col):
            self.col_hint_list.append(list(map(int, s_list.pop(0).split(","))))
        self.board = np.zeros((self.row, self.col))
        return
    
    def get_row(self, index):
        return list(self.board[index, :])
    
    def get_col(self, index):
        return list(self.board[:, index])
    
    def set_row(self, index, lt):
        self.board[index, :] = lt
        
    def set_col(self, index, lt):
        self.board[:, index] = lt
        
    def solve_line(self, rc, index):
        if rc == "r":
            solving_hint = self.row_hint_list[index]
            solving_line = self.get_row(index)
        elif rc == "c":
            solving_hint = self.col_hint_list[index]
            solving_line = self.get_col(index)


if __name__ == "__main__":
    myx = Solve("input.txt")
    s = myx._read_txt()
    t = myx.get_col(0)
    pass
