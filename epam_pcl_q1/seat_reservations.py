def solution(N, S):
    map = {
        'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'J': 8, 'K': 9
    }
    total_seats = [[-1] * 10 for _ in range(N)]
    if S:
        for i in S.split(" "):
            total_seats[int(i[0:-1]) - 1][map[i[-1]]] = 0

    for i in total_seats:
        i[:] = [i[0:3], i[3:7], i[7:]]
    print(total_seats)
    cnt = 0
    for row in total_seats:
        if 0 not in row[0][1:] and \
                0 not in row[1] and \
                0 not in row[2][0:2]:
            cnt += 2
        elif 0 not in row[0][1:] and \
                0 in row[1][0:2] and 0 not in row[1][2:] and \
                0 not in row[2][:2]:
            cnt += 1
        elif 0 not in row[0][1:] and \
                0 not in row[1][0:2] and 0 in row[1][2:]:
            cnt += 1
        elif 0 in row[0][1:] and \
                0 not in row[1][2:] and 0 not in row[2][:2]:
            cnt += 1
    print(cnt)


solution(22, "1A 3C 2B 20G 5A")
# solution(1, "")
