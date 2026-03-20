import sys

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    t = int(data[0])
    idx = 1
    out = []
    for _ in range(t):
        if idx >= len(data):
            break
            
        n = int(data[idx])
        idx += 1

        a = [int(x) for x in data[idx : idx+n]]
        idx += n
        
        b = [int(x) for x in data[idx : idx+n]]
        idx += n
        
        ops = []

        for i in range(n):
            for j in range(n - 1 - i):
                if a[j] > a[j+1]:
                    a[j], a[j+1] = a[j+1], a[j]
                    ops.append((1, j + 1))

        for i in range(n):
            for j in range(n - 1 - i):
                if b[j] > b[j+1]:
                    b[j], b[j+1] = b[j+1], b[j]
                    ops.append((2, j + 1))

        for i in range(n):
            if a[i] > b[i]:
                a[i], b[i] = b[i], a[i]
                ops.append((3, i + 1))

        out.append(str(len(ops)))
        for op, index in ops:
            out.append(f"{op} {index}")

    if out:
        sys.stdout.write('\n'.join(out) + '\n')

if __name__ == '__main__':
    solve()