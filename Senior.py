n = int(input())
holes = list(map(int,input().split()))
m = int(input())
balls = list(map(int,input().split()))
pos = []
i = 0

holefill = []
for x in range(len(holes)):
    holefill.append(0)

ballpos = []
for x in range(len(balls)):
    ballpos.append(0)

while(i != m):
    ball = balls[i]
    noofholes = len(holes)
    j = noofholes - 1
    while(j != -1):
        if(ball <= holes[j]):
            if(holefill[j] < (j+1)):
                ballpos[i] = j+1
                holefill[j] += 1
                break
        j -= 1
    i += 1
for x in ballpos:
    print(x,end=' ')
