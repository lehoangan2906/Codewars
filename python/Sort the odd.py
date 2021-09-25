# You will be given an array of numbers. You have to sort the odd numbers in ascending order
# while leaving the even numbers at their original positions.
""" 
Examples
[7, 1]  =>  [1, 7]
[5, 8, 6, 3, 4]  =>  [3, 8, 6, 5, 4]
[9, 8, 7, 6, 5, 4, 3, 2, 1, 0]  =>  [1, 8, 3, 6, 5, 4, 7, 2, 9, 0]
 """

def sort_array(source_array):
    n = len(source_array)

    # Base case length = 0
    if n == 0:
        return source_array
    
    else:
        list = []
        num = 0
        for i in range(n):
            if source_array[i] % 2 != 0:
                list.append(source_array[i])
                num += 1

        list.sort()
        f = 0

        while f < num:
            for j in range(n):
                if source_array[j] % 2 != 0:
                    source_array[j] = list[f]
                    f += 1
    
    return source_array


def sort_array(arr):
  odds = sorted((x for x in arr if x%2 != 0), reverse=True)
  return [x if x%2==0 else odds.pop() for x in arr]

print(sort_array([5, 3, 2, 8, 1, 4]))