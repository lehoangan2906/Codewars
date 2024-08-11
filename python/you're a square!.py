def is_square(n):
    if n < 0:
        return False

    i = 0
    while i * i <= n:
        if i * i == n:
            return True
        i += 1
    return False


arr = [-1, 0, 3, 4, 25, 26]
for n in arr:
    print(is_square(n), "\n")
