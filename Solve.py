import numpy as np


class Solve:
    def __init__(self, _file) -> None:
        self.file_name = _file
        self.row = 0
        self.col = 0
        self.row_hint_list = []
        self.col_hint_list = []
        self.board: np.ndarray  # -1错，0空，1对
        self.solve_list = []

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

    def solve_line(self, index, rc):
        if rc == "r":
            solving_hint = self.row_hint_list[index]
            solving_line = self.get_row(index)
        elif rc == "c":
            solving_hint = self.col_hint_list[index]
            solving_line = self.get_col(index)

    def _is_match(self, line, hint, now) -> bool:
        for i in range(len(hint)):
            if -1 in line[now[i]:now[i]+hint[i]]:
                return False
            if now[i] != 0 and line[now[i]-1] == 1:
                return False
            if now[i]+hint[i] != len(line) and line[now[i]+hint[i]] == 1:
                return False
        return True
    
    def move(self, line, hint):
        now = []
        for i in range(len(hint)):
            now.append(sum(hint[:i])+i)        
        
        
            
    def add_solve_list(self, index, rc):
        if (index, rc) in self.add_solve_list:
            return
        else:
            self.solve_list.append((index, rc))

    def init_solve_list(self):
        for i in range(self.row):
            self.solve_list.append((i, "r"))
        for i in range(self.col):
            self.solve_list.append((i, "c"))

    def solving(self):
        while not self.is_solved:
            index_rc = self.solve_list.pop(0)
            self.solve_line(index_rc[0], index_rc[1])

    def is_solved(self):
        return 0 not in self.board


if __name__ == "__main__":
    myx = Solve("input.txt")
    ans = myx.move([], [2, 4])
    print(ans)
    pass
