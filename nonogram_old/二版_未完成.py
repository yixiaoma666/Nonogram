import time
import pickle


class Solve:
    def __init__(self, filename):
        self.board, self.hangN, self.hanglt, self.lieN, self.lielt = None, None, None, None, None
        self.filename = filename
        self.importfile()
        self.init_board()
        self.do_board()

    def init_board(self):
        self.board = [[0] * self.lieN] * self.hangN

    def do_board(self):
        while True:
            self.do_hang()
            self.do_lie()
            if True:
                self.print_solve()
                break
            pass
        pass

    def do_hang(self):
        temp_board = self.board
        for i in range(self.hangN):
            board = temp_board[i]
        pass

    def do_lie(self):
        pass

    def print_solve(self):
        pass

    def importfile(self):
        with open(self.filename, mode="r") as f:  # 打开输入文档
            txt = f.read()  # 读取输入文档
            txt = txt.split("\n")  # 文档用换行分隔，存为列表
            txt = [x for x in txt if x != ""]  # 列表去空元素
            a = txt[0].split(",")  # a为行数和列数
            hangN, lieN = int(a[0]), int(a[1])  # hangN为行数，lieN为列数
            del a  # 去除a
            txt.pop(0)  # 将输入的列表第一行去掉
            hanglt = []  # 初始化行的信息
            lielt = []  # 初始化列的信息
            for i in range(hangN):  # 根据行数循环
                a = txt[i]  # a 为第一行的信息
                a = a.split(",")  # a用逗号分隔后存为列表
                a = list(map(int, a))  # 列表的字符串转数字
                hanglt.append(a)  # 以列表形式存入hanglt
            for i in range(hangN):  # 此循环去除行的信息，使最前面为列信息
                txt.pop(0)
            for i in range(lieN):  # 根据列数循环
                a = txt[i]  # a 为第一列的信息
                a = a.split(",")  # a用逗号分隔后存为列表
                a = list(map(int, a))  # 列表的字符串转为数字
                lielt.append(a)  # 以列表的形式存入lielt
        del a, f, i, txt
        self.hangN, self.lieN, self.hanglt, self.lielt = hangN, lieN, hanglt, lielt
        del self.filename


solve = Solve("inp5.txt")
print(solve.board)
