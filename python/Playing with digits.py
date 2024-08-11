def dig_pow(n, p):
    # Convert the number to a string to easily access each digit
    digits = [int(d) for d in str(n)]

    # Calculate the sum of digits raised to the consecutive powers
    tol_sum = 0
    for i in range(len(digits)):
        tol_sum += digits[i] ** (p + i)

    # check if the sum is divisible by n
    if tol_sum % n == 0:
        return tol_sum // n
    else:
        return -1

def dig_pow2(n, p):
    s = 0
    for i,c in enumerate(str(n)):
        s += pow(int(c), p + i)
    return s/n if s%n == 0 else -1

