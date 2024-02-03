def symmetry(n: int):
    for i in range(n):
        print('* ' * (n - i) + ' ' * (2 * i) + '* ' * (n - i))
    for i in range(1, n + 1):
        print('* ' * i + ' ' * (2 * (n - i)) + '* ' * i)

