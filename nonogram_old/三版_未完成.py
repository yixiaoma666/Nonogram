import time


class Solve:
    def __init__(self, hangN0, lieN0, hanglt0, lielt0):
        self.hangN, self.lieN, self.hanglt, self.lielt = hangN0, lieN0, hanglt0, lielt0
        self.board = []
        self.init_board()  # 初始化板子，0位未知，1为实，2为叉

    def init_board(self):
        self.board = [[0 for x in range(lieN)] for y in range(hangN)]

    def solve_hang(self, n):
        pass

    def solve_lie(self, n):
        pass


class Make:
    def __init__(self, lt, lt_len, outname):  # lt为信息，lt_len为信息要填的格数，outname为输出文件名
        self.lt, self.lt_len, self.outname = lt, lt_len, outname
        self.all_possible = []

    def all_possible_in(self):  # 用于填所有可能
        all_possible_begin = []
        can_blank = self.lt_len - sum(self.lt) - (len(self.lt) - 1)  # 可自由分配的空格格子数
        need_blank = len(self.lt) + 1  # 需要分的组数
        out_blank = []  # 分组的结果
        temp_blank = [0 for x in range(need_blank - 1)] + [can_blank]  # 分组的缓存
        out_blank.append(temp_blank[:])
        print(can_blank)
        print(need_blank)
        while True:  # 用来生成所有分配结果
            if temp_blank[0] == can_blank:
                break
            if temp_blank[-1] != 0:
                temp_blank[-1] -= 1
                temp_blank[-2] += 1
                out_blank.append(temp_blank[:])
            else:
                try:
                    for j in range(-1, -(can_blank + 1), -1):
                        if temp_blank[j] != 0 and temp_blank[j - 1] != 0:
                            temp_blank[j - 1] += 1
                            temp_blank[j] = 0
                            temp_blank[-1] = can_blank - sum(temp_blank[:-1])
                            out_blank.append(temp_blank[:])
                            break
                except IndexError:
                    pass
                try:
                    for j in range(-1, -(can_blank + 1), -1):
                        if temp_blank[j] != 0 and temp_blank[j - 1] == 0:
                            temp_blank[j] = 0
                            temp_blank[j - 1] += 1
                            temp_blank[-1] = can_blank - sum(temp_blank[:-1])
                            out_blank.append(temp_blank[:])
                            break
                except IndexError:
                    pass
        print(out_blank)
        for k in range(len(out_blank)):
            all_possible_begin_temp = []
            for j in range(len(self.lt)):
                if j == 0:
                    all_possible_begin_temp.append(out_blank[k][j] + self.lt[j] - 1)
                else:
                    all_possible_begin_temp.append(
                        out_blank[k][j] + self.lt[j] + j - 1 + all_possible_begin_temp[j - 1])
            all_possible_begin.append(all_possible_begin_temp[:])

        all_possible_temp = [2 for x in range(self.lt_len)]
        print(all_possible_begin)
        for each in all_possible_begin:
            for j in range(len(each)):
                for k in range(self.lt[j]):
                    all_possible_temp[each[j] + k] = 1
            outstring = ""
            for each in all_possible_temp:
                outstring += str(each)
            self.all_possible.append(outstring)
            all_possible_temp = [2 for x in range(self.lt_len)]


with open("inp5.txt", mode="r") as f:  # 打开输入文档
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
my_make = Make([2, 2, 2, 2, 2, 2, 2, 3], 35, "abc")
my_make.all_possible_in()
# print(my_make.all_possible)
