can_blank = 7
need_blank = 4
temp_blank = [0 for x in range(need_blank - 1)] + [can_blank]
while True:
    if temp_blank[0] == can_blank:
        break

    if temp_blank[-1] != 0:
        temp_blank[-1] -= 1
        temp_blank[-2] += 1
        print(temp_blank)
    else:
        try:
            for j in range(-1, -(can_blank + 1), -1):
                if temp_blank[j] != 0 and temp_blank[j - 1] != 0:
                    temp_blank[j-1] += 1
                    temp_blank[j] = 0
                    temp_blank[-1] = can_blank - sum(temp_blank[:-1])
                    print(temp_blank)
                    break
        except IndexError:
            pass

        try:
            for j in range(-1, -(can_blank + 1), -1):
                if temp_blank[j] != 0 and temp_blank[j - 1] == 0:
                    temp_blank[j] = 0
                    temp_blank[j - 1] += 1
                    temp_blank[-1] = can_blank - sum(temp_blank[:-1])
                    print(temp_blank)
                    break
        except IndexError:
            pass
