n, k =map(int, input().split())
a = list(map(int, input().split()))
learn = sorted(enumerate(a, 1), key=lambda x: x[1])
total = 0 
choice = []
for i, cost in learn:
    if total + cost <= k:
        total += cost
        choice.append(i)
    else:
        break
print(len(choice))
print(*choice)