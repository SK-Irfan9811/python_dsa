def f(c):
    if c < 1:
        return
    print(c)
    c -= 1
    f(c)


count = 3
f(count)
