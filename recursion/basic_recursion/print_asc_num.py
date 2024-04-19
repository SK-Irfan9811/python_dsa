def asc(n, k):
    if n > k:
        return
    print(n)
    asc(n + 1, k)


n = 1
k = 5
asc(n, k)
