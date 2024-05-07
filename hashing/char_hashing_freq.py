word = input("ENTER A WORD")
# hash array
hash_arr = [0] * 256
for char in word:
    hash_arr[ord(char) - ord('a')] += 1
print(hash_arr)