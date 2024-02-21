a = [0, 4, -1, 0, 3]
b = [0, -2, 5, 0, 3]
fair_idx=0
for i in range(len(a)):
    if sum(a[0:i+1])==sum(b[0:i+1])==sum(a[i+1:])==sum(b[i+1:]):
        fair_idx+=1
print(fair_idx)
