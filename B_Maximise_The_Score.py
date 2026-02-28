t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    score = 0
    for j in range(0, 2 * n, 2):
        score +=  a[j]
    print(score)

