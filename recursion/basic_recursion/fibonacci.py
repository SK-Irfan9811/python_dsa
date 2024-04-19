from typing import List


def print_fibo(a, b, limit, ans):
    if limit == 0:
        return ans
    a, b = b, a + b
    ans.append(b)
    return print_fibo(a, b, limit - 1, ans)


def generate_fibonacci_numbers(n: int) -> List[int]:
    ans = [0, 1]
    if n == 1:
        return [0]
    if n == 2:
        return ans

    return print_fibo(0, 1, n - 2, ans)


print(generate_fibonacci_numbers(6))
