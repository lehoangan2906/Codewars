from collections import deque

def find_most_adjacent(grid):
    if not grid:
        return None

    rows, cols = len(grid), len(grid[0])
    max_count, max_value = 0, float('inf')

    def bfs(r, c, value):
        count = 0
        q = deque([(r, c)])

        while q:
            i, j = q.popleft()
            count += 1

            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            for dr, dc in directions:
                ni, nj = i + dr, j + dc
                if 0 <= ni < rows and 0 <= nj < cols and grid[ni][nj] == value:
                    q.append((ni, nj))
                    grid[ni][nj] = None  # Mark visited cells as None

        return count

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] is not None:
                current_value = grid[r][c]
                current_count = bfs(r, c, current_value)

                if current_count > max_count or (current_count == max_count and current_value < max_value):
                    max_count = current_count
                    max_value = current_value

    return (max_value, max_count-1)