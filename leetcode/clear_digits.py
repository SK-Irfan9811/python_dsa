def clear_digits(s):
    stk = []
    for char in s:
        if char.isalpha():
            stk.append(char)
        else:
            if stk:
                stk.pop()
    return "".join(stk)


print(clear_digits("cb34"))
