def findLongest(lt):
    outlt = []
    S = 0
    left, right = None, None
    open = False
    outltCover = []
    for i in range(len(lt)):
        if lt[i] == 1:
            flag = True
            if not open:
                left = i
                open = True
        else:
            if open:
                right = i
                open = False
            flag = False
        if flag:
            S += 1
        else:
            outlt.append(S)
            if left is not None and right is not None:
                outltCover.append((left, right - 1))
            S = 0
    try:
        while True:
            outlt.remove(0)
    except ValueError:
        pass
    outltCover = sorted(list(set(outltCover)), key=lambda x: x[0])
    return outlt, outltCover


ls = [0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0]
print(findLongest(ls))
