import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    t = int(input_data[0])
    pointer = 1
    results = []
    
    for _ in range(t):
        n = int(input_data[pointer])
        s = input_data[pointer + 1]
        pointer += 2
        
        if "aa" in s:
            results.append("2")
        elif "aba" in s or "aca" in s:
            results.append("3")
        elif "abca" in s or "acba" in s:
            results.append("4")
        elif "abbacca" in s or "accabba" in s:
            results.append("7")
        else:
            results.append("-1")
            
    sys.stdout.write("\n".join(results) + "\n")

if __name__ == "__main__":
    solve()