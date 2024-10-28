# Implement a function to subtracts one list from another and returns the result.
# It should remove all values from list `a`, which are present in list `b` keeping their order.

a = [1,2,2,2,3]
b = [2]

def array_diff(a, b):
    for ele in b:
        if ele in a:
            a = list(filter(lambda x: x != ele, a))

    return a 

print(array_diff(a, b))
