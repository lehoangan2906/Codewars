def find_it(seq):
    result = 0
    for num in seq:
        result ^= num

    return result

"""
In Python, XOR (exclusive OR) is a bitwise operation where:

- a XOR a = 0 (any number XOR itself is 0)
- a XOR 0 = a (any number XOR 0 is the number itself)

XOR is commutative and associative, meaning the order of operations doesn't matter.
"""
