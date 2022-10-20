import sys
import time

sys.setrecursionlimit(5000)


class Make:  # 用于处理输入的列表
    def __init__(self, lt, ltlen):  # 构造函数，lt为信息的某一行（列），ltlen为这个信息的满长度
        self.lt = lt  # 信息的某一行（列）
        self.ltlen = ltlen  # 该行（列）的满长度
        self.ltout = []  # 初始化所有可能情况的列表，是带有数字的
        self.ltturn = list(map(lambda x: x + 1, self.lt))  # 把信息全部加一
        self.kong = self.ltlen + 1  # 该行（列）的空格数
        for each in self.ltturn:  # 计算该行（列）的空格数
            self.kong -= each
        self.begin = self.ltturn[:]
        self.begin = self.begin + [0] * self.kong  # 构造所有可能情况的初始值
        self.ltout.append(self.begin[:])  # 将初始值加入所有情况列表
        self.ltoutput = []  # 初始化所有可能情况的列表，只有0和1
        self.ltdo = [0] * self.ltlen  # TODO
        self.m2n()  # TODO
        self.change()  # TODO

    def m2n(self):  # 根据输入的信息和空的数量构造所有情况的列表
        while True:  # 无限循环
            if self.begin[0:self.kong] == [0] * self.kong:  # 当最前面全部为0
                self.ltout.append(self.begin[:])  # 此情况加入所有情况列表
                break  # 结束循环
            elif self.begin[-1] == 0:  # 当最后一位为0时，把从后数第一个非0值向后挪1
                for i in range(len(self.begin)):
                    if self.begin[-1 * i - 1] != 0:
                        self.begin[-1 * i - 1], self.begin[-1 * i] = self.begin[-1 * i], self.begin[-1 * i - 1]
                        break
                self.ltout.append(self.begin[:])  # 此情况加入所有情况列表
            else:
                for i in range(len(self.begin)):  # 当最后一位不为0时，把a000xyz中的a向后移一位，xyz接到a后
                    if self.begin[-1 * i - 1] == 0 and self.begin[-1 * i - 2] != 0:
                        self.begin[-1 * i - 1], self.begin[-1 * i - 2] = self.begin[-1 * i - 2], self.begin[-1 * i - 1]
                        while True:
                            if self.begin[-1 * i] == 0:
                                self.begin.pop(-1 * i)
                                self.begin.append(0)
                                continue
                            break
                        break
                self.ltout.append(self.begin[:])  # 此情况加入所有情况列表

    def change(self):  # 将数字m转化为m长度的1，并存入self.ltoutput
        for each in self.ltout:
            ltouti = []
            for eachi in each:
                if eachi == 0:
                    ltouti.append(0)
                else:
                    for m in range(eachi):
                        if m != eachi - 1:
                            ltouti.append(1)
                        else:
                            ltouti.append(0)
            ltouti.pop(-1)
            self.ltoutput.append(ltouti)

    def tian(self, yiyou):
        A = list(range(len(self.ltoutput)))
        A.reverse()
        for j in A:
            for i in range(self.ltlen):
                if yiyou[i] != -1:
                    if self.ltoutput[j][i] != yiyou[i]:
                        del self.ltoutput[j]
                        break
        for i in range(self.ltlen):
            templs = []
            for j in range(len(self.ltoutput)):
                templs.append(self.ltoutput[j][i])
            if sum(templs) == len(self.ltoutput):
                self.ltdo[i] = 1
            elif sum(templs) == 0:
                self.ltdo[i] = 0
            else:
                self.ltdo[i] = -1


class Solve:
    def __init__(self, hang, lie, hanglt, lielt):  # 构造函数
        self.hang = hang  # 保存行数
        self.lie = lie  # 保存列数
        self.hanglt = hanglt  # 保存行信息（以二维列表形式）
        self.lielt = lielt  # 保存列信息（以二维列表形式）
        self.board = []  # 初始化解题板
        for i in range(hang):  # 将解题版全部填 -1 ，其中 -1 为待填入，0 为空，1 为实
            self.board.append(self.lie * [-1])

    def dohang(self):  # 处理行的函数
        for hanghao in range(self.hang):  # 根据行数循环
            if -1 not in self.board[hanghao]:
                continue
            temphang = Make(self.hanglt[hanghao], self.lie)  # 选择行信息的第 hanghao 个元素，以及列数，用Make类构造temphang对象
            temphang.tian(self.board[hanghao])
            self.board[hanghao] = temphang.ltdo

    def dolie(self):
        for liehao in range(self.lie):
            templie = []
            for i in range(self.hang):
                templie.append(self.board[i][liehao])
            if -1 not in templie:
                continue
            templie = Make(self.lielt[liehao], self.hang)
            boardliehao = []
            for each in self.board:
                boardliehao.append(each[liehao])
            templie.tian(boardliehao)
            for i in range(len(self.board)):
                self.board[i][liehao] = templie.ltdo[i]

    def Qprint(self):
        for i in self.board:
            for j in i:
                if j == 1:
                    print("█", end="")
                elif j == 0:
                    print("XX", end="")
                else:
                    print('--', end="")
            print("")


t_1 = time.time()
with open("inp3.txt", mode="r") as f:  # 打开输入文档
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

solve = Solve(hangN, lieN, hanglt, lielt)  # 根据hangN，lieN，hanglt，lielt（行数，列数，行信息，列信息）从Solve类构造solve对象
tempsolve = solve.board[:]
while True:
    t_3 = time.time()
    solve.dohang()
    solve.dolie()
    solve.Qprint()
    print("")
    if tempsolve == solve.board:
        break
    tempsolve = solve.board[:]
    t_4 = time.time()
    print(t_4 - t_3)
solve.Qprint()
t_2 = time.time()
print(t_2 - t_1)
