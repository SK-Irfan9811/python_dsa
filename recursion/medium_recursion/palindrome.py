def is_palindrome(word, l, r):
    if l >= r:
        return True
    if word[l] != word[r]:
        return False
    return is_palindrome(word, l + 1, r - 1)


palindromic_words = ["radar", "level", "civic", "rotor", "deed",
                     "noon", "kayak", "racecar", "madam", "refer","GoaT"
                     ]

for word in palindromic_words:
    print(is_palindrome(word.lower(), 0, len(word) - 1))
