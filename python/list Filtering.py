# Create a function that takes a list of non-negative integers and strings and returns a new list with the string filtered out

list = [1, 2, 'a', 'b']

def filter_list(l):
    return [e for e in l if isinstance(e, int)]

print(filter_list(list))
