def order_weight(strng):
    # sort strng element alphabetical order
    sort1 = sorted(strng.split(' '))
    # sort pesorted strng elements based on their digits sums
    sort2 = sorted(sort1, key=sumnum)
    return ' '.join(sort2)

# the function used as sorted2's key
def sumnum(n):
    return sum([int(item) for item in n])

print(order_weight("103 123 4444 99 2000"))
