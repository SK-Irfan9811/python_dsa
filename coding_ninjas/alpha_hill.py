import string

n = 3
alphas = string.ascii_uppercase
for i in range(n):
    matter = ' '.join(alphas[:i] + alphas[i] + alphas[:i][::-1])
    print((2 * (n-i-1)) * ' ' + matter)
