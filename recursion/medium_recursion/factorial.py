# functional way
def get_fact_fun(n):
    if n < 1:
        return 1
    return n * get_fact_fun(n - 1)


print(get_fact_fun(-1))


# parameterized way
def get_fact_par(n, prod):
    if n < 1:
        return prod
    return get_fact_par(n - 1, prod * n)


print(get_fact_par(-1, 1))
