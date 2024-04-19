def fibo(n, cache):
    if n in cache:
        return cache[n]
    if n == 0 or n == 1:
        return n
    cache[n] = fibo(n - 1, cache) + fibo(n - 2, cache)
    return cache[n]


n = int(input("enter a number (>1)"))
cache = {}  # memorization
print(fibo(n - 1, cache))
