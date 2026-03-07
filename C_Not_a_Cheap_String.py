import sys
def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    t = int(data[0])
    curr = 1
    result = []
    for _ in range(t):
        w = data[curr]
        p = int(data[curr + 1])
        curr += 2
        total = 0
        count = [0] * 26
        for char in w:
            val = ord(char) - ord('a') + 1
            total += val
            count[val - 1] += 1
        for i in range(25, -1, -1):
            val = i + 1
            while count[i] > 0 and total > p:
                total -= val
                count[i] -= 1
        res = []
        for char in w:
            idx = ord(char) - ord('a')
            if count[idx] > 0:
                res.append(char)
                count[idx] -= 1
        result.append("".join(res))
    print("\n".join(result))
solve()