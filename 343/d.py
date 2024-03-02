n, t = map(int,input().split())
records = [list(map(int,input().split())) for i in range(t)]

points = [0]*n

# TLE (逐次更新，その度にset化)
for record in records:
    player, point = record
    points[player-1] += point
    print(len(set(points)))