from collections import defaultdict

limit = 4
nums = [[1, 4], [2, 5], [1, 3], [3, 4]]
balls = {}
colors = defaultdict(int)
unique_colors = 0

for ball, color in nums:
    if ball in balls:
        old_color = balls[ball]
        colors[old_color] -= 1
        if colors[old_color] == 0:
            unique_colors -= 1
    balls[ball] = color
    if colors[color] == 0:
        unique_colors += 1
    colors[color] += 1
    print(unique_colors)
