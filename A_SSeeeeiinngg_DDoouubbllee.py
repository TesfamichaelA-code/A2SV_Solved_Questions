t = int(input())

for _ in range(t):
    s = sorted(input().strip())
    print("".join(s + s[::-1]))

