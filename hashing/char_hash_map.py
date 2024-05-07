word = input("ENTER A WORD")
freq_map = {}
for i in word:
    freq_map[i] = freq_map.get(i, 0) + 1
print(freq_map)
