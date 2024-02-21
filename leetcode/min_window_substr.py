# def min_window(s: str, t: str) -> str:
#     if s == t:
#         return s
#     if len(s) < len(t):
#         return ""
#     l = r = 0
#     temp = list(t)
#     flag = 0
#     min_str = ""
#     while l < len(s):
#         if flag == 0:
#             if s[l] in temp:
#                 flag = 1
#                 temp.remove(s[l])
#                 r = l + 1
#             else:
#                 l += 1
#
#         elif flag == 1:
#             if r < len(s) and s[r] in temp:
#                 temp.remove(s[r])
#                 r += 1
#             elif r < len(s) and s[r] not in temp:
#                 r += 1
#             else:
#                 flag = 0
#                 l += 1
#                 r = 0
#                 temp = list(t)
#         if not temp:
#             flag = 0
#             temp = list(t)
#             if not min_str or len(min_str) >= len(s[l:r]):
#                 min_str = s[l:r]
#             l += 1
#             r = 0
#     return min_str

# print(min_window("ADOBECODEBANC", "ABC"))
# print(min_window("aa", "aaa"))
# print(min_window("aa", "a"))
# print(min_window("ss", "t"))
# print(min_window("a", "b"))
# print(min_window("bdab", "ab"))
# print(min_window("bba", "ab"))
# print(min_window("acbbaca", "aba"))

# the above code gives TLE for large test cases
# here is the window-sliding technique
def min_window(s: str, t: str) -> str:
    l = r = 0
    res, res_len = [-1, -1], float("infinity")
    window, count = {}, {}
    for i in t:
        count[i] = 1 + count.get(i, 0)
    have, need = 0, len(count)
    while r < len(s):
        window[s[r]] = 1 + window.get(s[r], 0)
        if s[r] in count and window[s[r]] == count[s[r]]:
            have += 1
        while have == need:
            if (r - l + 1) < res_len:
                res_len = r - l + 1
                res = [l, r]
            window[s[l]] -= 1
            if s[l] in count and window[s[l]] < count[s[l]]:
                have -= 1
            l += 1
        r += 1
    l, r = res
    return s[l:r + 1] if res_len != float("infinity") else ""


#
print(min_window("ADOBECODEBANC", "ABC"))
print(min_window("aa", "aaa"))
print(min_window("aa", "a"))
print(min_window("ss", "t"))
print(min_window("a", "b"))
print(min_window("bdab", "ab"))
print(min_window("bba", "ab"))
print(min_window("acbbaca", "aba"))
