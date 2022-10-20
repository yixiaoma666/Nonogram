import time
import pickle


class Solve:
    def __init__(self, hang, lie, hanglt, lielt):
        self.hang = hang
        self.lie = lie
        self.hanglt = hanglt
        self.lielt = lielt
        self.hanglt_all = []
        self.lielt_all = []
        for i in range(hang):
            tt = time.time()
            make = Make(hanglt[i], lie)
            self.hanglt_all.append(make.ltoutput[:])
            with open("temp/hanglt_all{}".format(i), mode="wb") as f:
                pickle.dump(self.hanglt_all[0], f)
            ttt = time.time()
            if (ttt - tt) > 1:
                print("第{}行初始化完成，用时{:.2f}秒".format(i, ttt - tt))
            del self.hanglt_all[0]
        for i in range(lie):
            tt = time.time()
            make = Make(lielt[i], hang)
            self.lielt_all.append(make.ltoutput[:])
            with open("temp/lielt_all{}".format(i), mode="wb") as f:
                pickle.dump(self.lielt_all[0], f)
            ttt = time.time()
            if (ttt - tt) > 1:
                print("第{}列初始化完成，用时{:.2f}秒".format(i, ttt - tt))
            del self.lielt_all[0]
        self.board = []  # 初始化解题板
        for i in range(hang):  # 将解题版全部填 -1 ，其中 -1 为待填入，0 为空，1 为实
            self.board.append(self.lie * [-1])

    def dohang(self):
        for i in range(self.hang):
            tt = time.time()
            board = self.board[i]
            temp_hanglt = len(board) * [0]
            with open("temp/hanglt_all{}".format(i), mode="rb") as f:
                hanglt_all = pickle.load(f)
            for j in range(len(hanglt_all) - 1, -1, -1):
                for k in range(len(board)):
                    if board[k] != -1:
                        if board[k] != hanglt_all[j][k]:
                            del hanglt_all[j]
                            break
            for k in range(len(board)):
                for each in hanglt_all:
                    temp_hanglt[k] += each[k]
            for j in range(len(temp_hanglt)):
                if temp_hanglt[j] == len(hanglt_all):
                    temp_hanglt[j] = 1
                elif temp_hanglt[j] == 0:
                    temp_hanglt[j] = 0
                else:
                    temp_hanglt[j] = -1
            self.board[i] = temp_hanglt[:]
            with open("temp/hanglt_all{}".format(i), mode="wb") as f:
                pickle.dump(hanglt_all, f)
            ttt = time.time()
            if (ttt - tt) > 1:
                print("第{}行已填，用时{:.2f}秒".format(i, ttt - tt))

    def dolie(self):
        for i in range(self.lie):
            tt = time.time()
            board = [0] * self.hang
            for m in range(self.hang):
                board[m] = self.board[m][i]
            temp_lielt = len(board) * [0]
            with open("temp/lielt_all{}".format(i), mode="rb") as f:
                lielt_all = pickle.load(f)
            for j in range(len(lielt_all) - 1, -1, -1):
                for k in range(len(board)):
                    if board[k] != -1:
                        if board[k] != lielt_all[j][k]:
                            del lielt_all[j]
                            break
            for k in range(len(board)):
                for each in lielt_all:
                    temp_lielt[k] += each[k]
            for j in range(len(temp_lielt)):
                if temp_lielt[j] == len(lielt_all):
                    temp_lielt[j] = 1
                elif temp_lielt[j] == 0:
                    temp_lielt[j] = 0
                else:
                    temp_lielt[j] = -1
            for m in range(self.hang):
                self.board[m][i] = temp_lielt[m]
            with open("temp/lielt_all{}".format(i), mode="wb") as f:
                pickle.dump(lielt_all, f)
            ttt = time.time()
            if (ttt - tt) > 1:
                print("第{}列已填，用时{:.2f}秒".format(i, ttt - tt))

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
        self.ltdo = [0] * self.ltlen
        self.m2n()
        self.change()

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
                        self.begin[-1 * i - 1], self.begin[-1 * i - 2] = self.begin[-1 * i - 2], self.begin[
                            -1 * i - 1]
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


t_all = time.time()
t_1 = time.time()
with open("inp10.txt", mode="r") as f:  # 打开输入文档
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
print("导入时间：{:.2f}秒".format(time.time() - t_1))
t_1 = time.time()
solve = Solve(hangN, lieN, hanglt, lielt)  # 根据hangN，lieN，hanglt，lielt（行数，列数，行信息，列信息）从Solve类构造solve对象
print("初始化时间：{:.2f}秒".format(time.time() - t_1))
tempsolve = solve.board[:]
while True:
    t_1 = time.time()
    solve.dohang()
    solve.dolie()
    solve.Qprint()
    print("")
    if tempsolve == solve.board:
        break
    tempsolve = solve.board[:]
    print("本次时间：{:.2f}秒".format(time.time() - t_1))
solve.Qprint()
print("总时间：{:.2f}秒".format(time.time() - t_all))
