dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

N, M = map(int, input().split())

a = [list(map(int, list(input()))) for _ in range(N)]

# False로 가득찬 2d list
visit = [[False] * M for _ in range(N)]
distance = [[0] * M for _ in range(N)]

#BFS Starts
queue = []
queue.append((0,0))
visit[0][0] = True
distance[0][0] = 1

while queue:
    x, y = queue.pop(0) # list.pop(0) 맨 첫번째 인덱스의 값을 지우고, return
    for i in range(4):
        nx = x + dx[i] #좌우
        ny = y + dy[i] #상하
        if 0 <= nx < N and 0 <= ny < M:
            if visit[nx][ny] == False and a[nx][ny] == 1:
                queue.append((nx,ny)) #방문 가능한 좌표를 저장
                distance[nx][ny] = distance[x][y] + 1 # 우리가 지나온 길이 있는 distance에 1을 더해준다
                visit[nx][ny] = True

print(distance)
print(visit)
print(distance[N-1][M-1])


