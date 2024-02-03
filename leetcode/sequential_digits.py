import string

#
#
# def get_first_seq(ln):
#     return int(string.digits[1:ln + 1])
#
#
# def get_len(val):
#     return len(str(val))
#
#
#
# low = 10
# high = 1000000000
# ans = set()
# c = 0
#
#
# def get_sub_seq(val, high, low):
#     v = []
#     while '0' not in str(val) and val < high:
#         if val >= low:
#             v.append(val)
#         val += int('1' * get_len(val))
#     return v
#
#
# while True:
#     value = get_first_seq(get_len(low) + c)
#     c += 1
#     if value >= high or c > 9:
#         break
#     ans.update(get_sub_seq(value, high, low))
# print(sorted(list(ans)))

# another approach
low = 1000
high = 13000
digits = string.digits[1:]
l = len(str(low))
h = len(str(high))
ans = []
for i in range(l, h + 1):
    j = 0
    while i + j <= 9:
        val = int(digits[j:j + i])
        if low <= val <= high:
            ans.append(val)
        j += 1
print(ans)