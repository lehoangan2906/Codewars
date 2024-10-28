def S(N):
    return sum(i for i in range(1, N+1)) 

def Z(N):
    return sum(S(i) for i in range(1, N+1))

def sum_of_sums(n):
    return S(Z(n))
