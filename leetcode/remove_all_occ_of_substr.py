s = "kpygkivtlqoocskpygkpygkivtlqoocssnextkqzjpycbylkaondskivtlqoocssnextkqzjpycbylkaondssnextkqzjpycbylkaondshijzgaovndkjiiuwjtcpdpbkrfsi"
p = "kpygkivtlqoocssnextkqzjpycbylkaonds"
stack = []
for i in s:
    stack.append(i)

    if len(stack) >= len(p) and "".join(stack[-len(p):]) ==p:
        del stack[-len(p):]
print(stack)
