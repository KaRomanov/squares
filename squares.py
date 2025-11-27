def solve(row, col, matrix, symbols, rows_conflict, cols_conflict, boxes_conflict):
    global N, n
    if row == N:
        return True

    if col == N - 1:
        next_row = row + 1
        next_col = 0
    else:
        next_row = row
        next_col = col + 1

    if matrix[row][col] != "0":
        return solve(
            next_row,
            next_col,
            matrix,
            symbols,
            rows_conflict,
            cols_conflict,
            boxes_conflict,
        )

    box_row = row // n
    box_col = col // n
    box_index = box_row * n + box_col

    for sym in symbols:
        if (
            sym not in rows_conflict[row]
            and sym not in cols_conflict[col]
            and sym not in boxes_conflict[box_index]
        ):
            matrix[row][col] = sym
            rows_conflict[row].add(sym)
            cols_conflict[col].add(sym)
            boxes_conflict[box_index].add(sym)

            if solve(
                next_row,
                next_col,
                matrix,
                symbols,
                rows_conflict,
                cols_conflict,
                boxes_conflict,
            ):
                return True

            rows_conflict[row].remove(sym)
            cols_conflict[col].remove(sym)
            boxes_conflict[box_index].remove(sym)
            matrix[row][col] = "0"

    return False


n = int(input())
N = n * n
matrix = []

for i in range(N):
    curr_row = input().split()
    matrix.append(curr_row)

symbols = set()
for r in range(N):
    for c in range(N):
        if matrix[r][c] != "0":
            symbols.add(matrix[r][c])

rows_conflict = [set() for _ in range(N)]
cols_conflict = [set() for _ in range(N)]
boxes_conflict = [set() for _ in range(N)]

for r in range(N):
    for c in range(N):
        sym = matrix[r][c]
        if sym != "0":
            box_r_n = r // n
            box_c_n = c // n
            box_index = box_r_n * n + box_c_n

            rows_conflict[r].add(sym)
            cols_conflict[c].add(sym)
            boxes_conflict[box_index].add(sym)

print("\n")
if solve(0, 0, matrix, symbols, rows_conflict, cols_conflict, boxes_conflict):
    for row in matrix:
        print(" ".join(row))
