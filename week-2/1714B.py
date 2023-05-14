t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    removed = 0
    b = set()
    for i in range(n):
        if a[i] in b:
            break
        b.add(a[i])
        removed += 1
    print(n - removed)
