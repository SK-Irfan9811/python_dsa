# functional way
def get_sum_fun(n):
    if n < 1:
        return 0
    return n + get_sum_fun(n - 1)


print(get_sum_fun(-1))


# parameterized way
def get_sum_par(n, _sum):
    if n < 1:
        return _sum
    return get_sum_par(n - 1, _sum + n)


print(get_sum_par(-1, 0))
