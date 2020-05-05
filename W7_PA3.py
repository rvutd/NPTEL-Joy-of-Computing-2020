n , m = map(int, input().split())
list = list(map(int, input().split()))
check = []

for i in range(n*m):

    if list[i] == 0 or list[i] == 1:
        check.append(list[i])

if len(check) == len(list):
    print("YES", end="")
else:
    print("NO", end="")