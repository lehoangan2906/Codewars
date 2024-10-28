def S(N):
    return N * (N + 1) // 2

def Z(N):
    sum_of_integers = N * (N + 1) // 2
    sum_of_squares = N * (N + 1) * (2 * N + 1) // 6
    return (sum_of_integers + sum_of_squares) // 2

def sum_of_sums(N):
    return S(Z(N))

print(sum_of_sums(3))  # Expected output: 55

