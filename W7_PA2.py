def isSymmetric(mat, N):
    for i in range(N):
        for j in range(N):
            if mat[i][j] != mat[j][i]:
                return False
    return True


# Driver code
n, m = map(int, input().split())
mat = list(map(int, input().split()))


if isSymmetric(mat, m):
    print("YES", end="")
else:
    print("No", end="")