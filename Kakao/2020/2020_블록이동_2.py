import queue

class Point:
    def __init__(self, row, col, dir, time):
        self.row = row
        self.col = col
        self.dir = dir
        self.time = time

UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3
# 시계방향으로 증가
D = ((-1,0), (1,0), (0, -1), (0,1)) #상하좌우
Drot = (((1,1),(1,-1),(-1,-1), (-1, 1)), ((1,-1),(-1,-1),(-1,1), (1, 1))) # 시계방향 / 반시계 / 중앙 회전
Dcor = (((-1,1),(1,1),(1,-1), (-1, -1)), ((-1,-1),(-1,1),(1,1), (1, -1))) # 시계방향 / 반시계 / 테두리 회전

Board = []
N = 0
Q = queue.Queue()
Visited = [[[False for _ in range(4)] for _ in range(100)] for _ in range(100)]

def isValid(block):
    for pt in block:
        if pt.row < 0 or pt.row > N-1 or pt.col < 0 or pt.col > N-1:
            return False
        if Board[pt.row][pt.col] == 1:
            return False
        if Visited[pt.row][pt.col][pt.dir]:
            return False
    return True

def rotate(curr, ccw, idx):
    newPt = []
    a = idx
    b = (idx + 1) % 2
    dir = curr[a].dir
    newPt.append(Point(curr[a].row, curr[a].col, \
                        (curr[a].dir + (3 if ccw else 1)) % 4, curr[a].time + 1))
    newPt.append(Point(curr[b].row + Drot[ccw][dir][0], curr[b].col + Drot[ccw][dir][1], \
                        (curr[b].dir + (3 if ccw else 1)) % 4, curr[b].time + 1))

    if isValid(newPt) == False:
        return 0  

    if Board[curr[a].row + Dcor[ccw][dir][0]][curr[a].col + Dcor[ccw][dir][1]] == 1:
        return 0

    for pt in newPt:
        if pt.row == N-1 and pt.col == N-1:
            return pt.time
        Visited[pt.row][pt.col][pt.dir] = True     
        
    Q.put(newPt)
    return 0



def solution(board):
    global Board, N
    Board = board
    N = len(board)

    Q.put([Point(0,0,RIGHT, 0), Point(0,1,LEFT,0)])
    Visited[0][0][RIGHT] = True
    Visited[0][1][LEFT] = True

    while Q:
        curr = Q.get()

        for j in range(4):
            newPt = []
            for i in range(2):
                newPt.append(Point(curr[i].row + D[j][0], curr[i].col + D[j][1], \
                                curr[i].dir, curr[i].time + 1))
            
            if isValid(newPt) == False:
                continue

            for pt in newPt:
                if pt.row == N-1 and pt.col == N-1:
                    return pt.time
                Visited[pt.row][pt.col][pt.dir] = True
            
            Q.put(newPt)

        for ccw in range(2):
            for i in range(2):
                ret = rotate(curr, ccw, i)
                if ret:
                    return ret

    return 0