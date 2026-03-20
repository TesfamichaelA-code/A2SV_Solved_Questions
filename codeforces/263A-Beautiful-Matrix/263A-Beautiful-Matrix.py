import sys

def solve():
    for i in range(5):
        row = list(map(int, sys.stdin.readline().split()))
        if 1 in row:
            print(abs(i - 2) + abs(row.index(1) - 2))
            return

if __name__ == "__main__":
    solve()