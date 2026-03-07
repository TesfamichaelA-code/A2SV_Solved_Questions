import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    t = int(input_data[0])
    idx = 1
    
    out = []
    for _ in range(t):
        n = int(input_data[idx])
        s = input_data[idx+1]
        idx += 2
        
        odd_digits = []
        for char in s:
            if int(char) % 2 != 0:
                odd_digits.append(char)
                if len(odd_digits) == 2:
                    break
        
        if len(odd_digits) == 2:
            out.append("".join(odd_digits))
        else:
            out.append("-1")
            
    print("\n".join(out))

if __name__ == '__main__':
    solve()