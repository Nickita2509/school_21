matrix = []
with open('input.txt', 'r') as f:
    for line in f:
        if line.strip():
            row = list(map(int, line.split()))
            matrix.append(row)
n = len(matrix)
squares = 0
circles = 0

for i in range(n):
    for j in range(n):
        if matrix[i][j] == 1:
            to_check = [(i, j)]
            matrix[i][j] = 0
            count = 1
            min_i, max_i = i, i
            min_j, max_j = j, j

            while len(to_check) > 0:
               r, c = to_check.pop()
               if r < min_i: min_i = r
               if r > max_i: max_i = r
               if c < min_j: min_j = c
               if c > max_j: max_j = c

               neighbors = [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]
               for nr, nc in neighbors:
                   if 0 <= nr < n and 0 <= nc < n and matrix[nr][nc] == 1:
                       matrix[nr][nc] = 0
                       to_check.append((nr, nc))
                       count += 1
            if count > 1:
                area =  (max_i - min_i + 1) * (max_j - min_j + 1)
                if area == count:
                    squares += 1
                else:
                    circles += 1

print(squares, circles)