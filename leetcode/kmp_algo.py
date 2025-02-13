# for string matching algorithm
# construction of LSP table
pattern = "leeto"
sequence = "leetcode"
prevLPS, i = 0, 1
lps = [0] * len(pattern)
while i < len(pattern):
    if pattern[i] == pattern[prevLPS]:
        lps[i] = prevLPS + 1
        prevLPS += 1
        i += 1
    elif prevLPS == 0:
        lps[i] = 0
        i += 1
    else:
        prevLPS = lps[prevLPS - 1]
print(lps)

i, j = 0
while i < len(sequence):
    if sequence[i] == pattern[j]:
        i, j = i + 1, j + 1
    else:
        if j == 0:
            i += 1
        else:
            j = lps[j - 1]
    if j == len(pattern):
        print(i - j)
print(-1)
