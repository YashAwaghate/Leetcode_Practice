def solve_bubbles(bubbles):
    rows, cols = len(bubbles), len(bubbles[0])
    def get_neighbors(i, j):
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for di, dj in directions:
            new_i, new_j = i + di, j + dj
            if 0 <= new_i < rows and 0 <= new_j < cols:
                yield new_i, new_j
    def find_exploding_bubbles(board):
        to_explode = set()
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == 0:
                    continue
                color = board[i][j]
                same_color_neighbors = 0
                for ni, nj in get_neighbors(i, j):
                    if board[ni][nj] == color:
                        same_color_neighbors += 1
                if same_color_neighbors >= 2:
                    to_explode.add((i, j))
                    for ni, nj in get_neighbors(i, j):
                        if board[ni][nj] == color:
                            to_explode.add((ni, nj))
        return to_explode
    def apply_gravity(board):
        for j in range(cols):
            bottom = rows - 1
            for i in range(rows - 1, -1, -1):
                if board[i][j] != 0:
                    if i != bottom:
                        board[bottom][j] = board[i][j]
                        board[i][j] = 0
                    bottom -= 1
        return board
    result = [row[:] for row in bubbles]
    exploding = find_exploding_bubbles(result)
    for i, j in exploding:
        result[i][j] = 0
    result = apply_gravity(result)

    return result

# Example usage:
bubbles = [
    [3, 1, 2, 1],
    [1, 1, 1, 4],
    [3, 1, 2, 2],
    [3, 3, 3, 4]
]

final_result = solve_bubbles(bubbles)


def solution(queries, diff):
    ddd = {}
    ds = []
    for q in queries:
        sign, num = q[0], int(q[1:])
        if sign == "+":
            if num not in ddd:
                ddd[num] = 0
            ddd[num] += 1
        else:
            ddd[num] -= 1
        c = 0
        for k in ddd:
            if (k - diff) in ddd:
                c += ddd[k - diff] * ddd[k]
            if (k + diff) in ddd:
                c += ddd[k + diff] * ddd[k]
        ds.append(c // 2)
    return ds