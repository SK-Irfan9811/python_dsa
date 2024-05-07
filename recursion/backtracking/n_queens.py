def can_be_placed(arr, i, j, size):
    if "Q" in arr[i]:
        return False
    dummy_row = i
    dummy_col = j
    # left up corner
    while dummy_row >= 0 and dummy_col >= 0:
        if arr[dummy_row][dummy_col] == "Q":
            return False
        dummy_row -= 1
        dummy_col -= 1

    # left down the corner
    while i < size and j >= 0:
        if arr[i][j] == "Q":
            return False
        i += 1
        j -= 1

    return True


def n_queen_placement(arr, col, size, ans):
    if col == size:
        ans.append(list(arr[:]))
        return
    for row in range(size):
        if can_be_placed(arr, row, col, size):
            arr[row][col] = "Q"
            n_queen_placement(arr, col + 1, size, ans)
            arr[row][col] = "."


size = 5
ans = []
arr = [["."] * size for _ in range(size)]
n_queen_placement(arr, 0, size, ans)
print(ans)
