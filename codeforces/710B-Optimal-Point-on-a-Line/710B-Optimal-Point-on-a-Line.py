import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    x = sorted(int(val) for val in input_data[1:n+1])
    print(x[(n - 1) // 2])

if __name__ == '__main__':
    solve()