# dx[0], dy[0] => 오른쪽
# dx[1], dy[1] => 왼쪽
# dx[2], dy[2] => 아래
# dx[3], dy[3] => 위
dx = [0,0,1,-1]
dy = [1,-1,0,0]

N, M = map(int, input().split())
a = [list(map(int, list(input()))) for _ in range(N)]
# print(a)
visit = [[False]*M for _ in range(N)] #방문 했는지 안했는지 체크하기 위해
distance = [[0]*M for _ in range(N)] #방문하면서 거리를 재기 위해

#BFS Starts
queue = []
queue.append((0,0))
visit[0][0] = True
distance[0][0] = 1

while queue:

    x, y = queue.pop(0) #queue의 첫번째 튜플을 리턴하고 지움 -> pop의 역할
    # print(x,y)
    for i in range(4): #dx, dy의 길이만큼
        nx = x+dx[i] #deque해서 나오는 대상의 x값에 dx[i] 즉 0,0,1,-1을 다 대입한 결과가 nx
        ny = y+dy[i]
        if 0 <= nx < N and 0 <= ny < M: #만약 nx와 ny의 값이 미로를 안 벗어날경우에,
            if visit[nx][ny] == False and a[nx][ny] == 1: #아직 방문하지 않았고, 방문할수 있는 위치에 있다면,
                queue.append((nx,ny)) #방문 가능한 좌표를 저장
                distance[nx][ny] = distance[x][y]+1 #원래칸에 저장된 값 + 1
                visit[nx][ny] = True
print(distance[N-1][M-1])
                
