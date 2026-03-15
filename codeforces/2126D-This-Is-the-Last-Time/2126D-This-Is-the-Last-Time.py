import sys

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    
    ptr = 0
    t = int(data[ptr])
    ptr += 1
    
    ans = []
    for _ in range(t):
        n = int(data[ptr])
        k = int(data[ptr + 1])
        ptr += 2
        
        casinos = []
        for _ in range(n):
            l = int(data[ptr])
            r = int(data[ptr + 1])
            real = int(data[ptr + 2])
            ptr += 3
            casinos.append((l, real))
            
        casinos.sort()
        
        x = k
        best = -1
        i = 0
        
        while i < n:
            if casinos[i][0] <= x:
                if casinos[i][1] > best:
                    best = casinos[i][1]
                i += 1
            elif best > x:
                x = best
            else:
                break
        
        x = max(x, best)
        ans.append(str(x))
    
    sys.stdout.write("\n".join(ans) + "\n")

if __name__ == "__main__":
    solve()