from collections import deque
# sample folder from kickstart test data
testn = 2
sample = True
if sample:
    samplen = "sample_"
else:
    samplen = ""
fin = open(f"./{samplen}test_set_{testn}/{samplen}ts{testn}_input.txt", 'r')
fout = open("./output.txt", 'w')

T = int(fin.readline())

def solve(grid):
    #0 up
    #1 right
    #2 down
    #3 left
    total = 0
    for row in grid:
        for spot in row:
            if spot == "*":
                total += 1
    #print(total)
    r = len(grid)*2
    c = len(grid[0])*2
    rr = len(grid)
    cc = len(grid[0])
    gg = [[0 for _ in range(c)] for _ in range(r)]
    visited = [[0 for _ in range(cc)] for _ in range(rr)]
    for row in range(len(grid)):
        for col in range(len(grid[0])):

            gr = row * 2
            gc = col * 2
            if grid[row][col] == "*":
                gg[gr][gc] = 1
                gg[gr][gc+1] = 2
                gg[gr+1][gc+1] = 3
                gg[gr+1][gc] = 0
            else:
                gg[gr][gc] = 5
                gg[gr][gc+1] = 5
                gg[gr+1][gc+1] = 5
                gg[gr+1][gc] = 5
                visited[row][col] = 1
    def inbound(row,col):
        return row >= 0 and row < len(grid) and col >= 0 and col < len(grid[0])

    q = deque()
    q.append((0,0))
    visited[0][0] = 1
    while q:
        row,col = q.popleft()
        
        total -= 1
        nr = row * 2
        nc = col * 2
        if inbound(row, col + 1) and visited[row][col + 1] == 0:
            gg[nr][nc + 1] = 1
            gg[nr + 1][nc + 2] = 3
            q.appendleft((row, col + 1))
            visited[row][col + 1] = 1
        if inbound(row + 1, col) and visited[row + 1][col] == 0:
            gg[nr + 1][nc + 1] = 2
            gg[nr + 2][nc] = 0
            q.appendleft((row + 1, col))
            visited[row + 1][col] = 1
        if inbound(row - 1, col) and visited[row - 1][col] == 0:
            gg[nr][nc] = 0
            gg[nr-1][nc+1] = 2
            q.appendleft((row - 1, col))
            visited[row - 1][col] = 1
        if inbound(row, col - 1) and visited[row][col - 1] == 0:
            gg[nr+1][nc] = 3
            gg[nr][nc-1] = 1
            q.appendleft((row, col - 1))
            visited[row][col - 1] = 1

    def dfs(row,col):
        #computer doesn't have enough memory for recursive approach XD!!!
        nonlocal total
        visited[row][col] = 1
        total -= 1
        nr = row * 2
        nc = col * 2
        if inbound(row, col + 1) and visited[row][col + 1] == 0:
            gg[nr][nc + 1] = 1
            gg[nr + 1][nc + 2] = 3
            dfs(row, col + 1)
        if inbound(row + 1, col) and visited[row + 1][col] == 0:
            gg[nr + 1][nc + 1] = 2
            gg[nr + 2][nc] = 0
            dfs(row + 1, col)
        if inbound(row - 1, col) and visited[row - 1][col] == 0:
            gg[nr][nc] = 0
            gg[nr-1][nc+1] = 2
            dfs(row - 1, col)
        if inbound(row, col - 1) and visited[row][col - 1] == 0:
            gg[nr+1][nc] = 3
            gg[nr][nc-1] = 1
            dfs(row, col - 1)

    #dfs(0,0)
    if total != 0:
        print(total)
        return "IMPOSSIBLE"
    first = 2
    row = 0
    col = 0
    ans = ""
    while True:
        if (row,col) == (0,0):
            first -= 1
        if first == 0:
            return ans
        c = gg[row][col]
        if c == 0:
            ans += "N"
            row -= 1
        elif c == 1:
            ans += "E"
            col += 1
        elif c == 2:
            ans += "S"
            row += 1
        elif c == 3:
            ans += "W"
            col -= 1

for case in range(T):
    #print(case)
    r,c = [int(x) for x in fin.readline().strip().split()]
    grid = [fin.readline() for _ in range(r)]
    fout.write(f"Case #{case}: {solve(grid)}\n")

fin.close()