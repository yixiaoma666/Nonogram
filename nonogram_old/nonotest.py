import time

d = [0, 1, 2, 3]


def L(j):
    if j > 1:
        return 1
    else:
        return 0


def S(i, j):
    if (i, j) in save_S.keys():
        return save_S[(i, j)]
    if i == 0 and j == 0:
        save_S[(i, j)] = 1
        return 1
    elif i < 0 or j < 0:
        save_S[(i, j)] = 0
        return 0
    else:
        save_S[(i, j)] = S(i - 1, j) + S(i - d[j] - L(j), j - 1)
        return S(i - 1, j) + S(i - d[j] - L(j), j - 1)


save_S = dict()
t1 = time.time()
for i in range(0, 13):
    for j in range(0, len(d)):
        print("S({},{})={}".format(i, j, S(i, j)), end="\t")
    print("")
print(time.time() - t1)
