def solve():
    n = int(input())
    a = list(map(int, input().split()))
    
    def is_derangement(arr):
        if len(arr) == 0:
            return False
        sorted_arr = sorted(arr)
        for i in range(len(arr)):
            if arr[i] == sorted_arr[i]:
                return False
        return True
    
    
    if is_derangement(a):
        print("YES")
        print(n)
        print(*a)
        return
    
    
    for i in range(n):
        new_arr = a[:i] + a[i+1:]
        if is_derangement(new_arr):
            print("YES")
            print(len(new_arr))
            print(*new_arr)
            return
    

    for i in range(n):
        for j in range(i + 1, n):
            new_arr = [a[k] for k in range(n) if k != i and k != j]
            if is_derangement(new_arr):
                print("YES")
                print(len(new_arr))
                print(*new_arr)
                return
    
    
    if n <= 10:
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    new_arr = [a[l] for l in range(n) if l != i and l != j and l != k]
                    if is_derangement(new_arr):
                        print("YES")
                        print(len(new_arr))
                        print(*new_arr)
                        return
    

    for start in range(n):
        for end in range(start + 1, n + 1):
            subarray = a[start:end]
            if is_derangement(subarray):
                print("YES")
                print(len(subarray))
                print(*subarray)
                return
    
    print("NO")

def main():
    t = int(input())
    for _ in range(t):
        solve()

if __name__ == "__main__":
    main()