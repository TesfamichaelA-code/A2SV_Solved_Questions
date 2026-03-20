t = int(input())
for _ in range(t):
    n, s = map(int, input().split())
    x = list(map(int, input().split()))
    
    if n == 1:
        print(abs(x[0] - s))
    else:
        min_x = min(x)
        max_x = max(x)
        
        if s <= min_x:
            print(max_x - s)
        elif s >= max_x:
            print(s - min_x)
        else:
            print(min(s - min_x, max_x - s) + (max_x - min_x))