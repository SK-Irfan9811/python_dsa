import string


def alpha_triangle(n: int):
    alphas = string.ascii_uppercase
    for i in range(n):
        print(' '.join(alphas[n - i - 1:n][::-1]))


alpha_triangle(4)
