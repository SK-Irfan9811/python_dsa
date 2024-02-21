# 12-->4+4+4
# 13-->9+4


def find_divs(num, div, cnt):
    if num == 0:
        print("got a solution", cnt)
        return
    elif num < 0:
        return
    else:
        cnt += 1
        print(cnt)
    for i in sqrs[::-1]:
        find_divs(num - i, i, 0)


n = 5
sqrs = [x * x for x in range(1, int(n ** 0.5) + 1)]

find_divs(n, 1, cnt=0)
