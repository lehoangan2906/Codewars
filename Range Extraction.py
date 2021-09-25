""" A format for expressing an ordered list of integers is to use a comma separated list of either

- individual integers
- or a range of integers denoted by the starting integer separated from the end integer in the range by a dash, '-'. The range includes all integers in the interval including both endpoints. It is not considered a range unless it spans at least 3 numbers. For example "12,13,15-17"
Complete the solution so that it takes a list of integers in increasing order and returns a correctly formatted string in the range format.

Example:

solution([-6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20])
# returns "-6,-3-1,3-5,7-11,14,15,17-20" """

# idea: 
# - we create an empty list: out
# - we set both begin and end to the 0th element of the original list
# - next, we traverse through list's elements (starting from 1th element) one by one by variable n
# - after that, we check if n is equal to "end" + 1?
#         if not, we check if end == begin --> add that value to the list out[]                         (individual integer case)
#                 we check if end == begin + 1  -->  add both of end and begin to the list out[]        (range does not exceed 3 elements case)
#                 if both of the above case do not happen, add (begin - end) to the list out[]          (complete range case)
# - if n is not equal to "end" + 1, we reset "begin" and "end" value to equal n's value, then the loop will increment n by 1 and we'll start over

def solution(args):
    out = []
    begin = end = args[0]
    
    for n in args[1:] + [""]:    
        # the [""] help we enter the loop one more time after the loop's ending condition is met    
        if n != end + 1:
            if end == begin:
                out.append( str(begin) )
            elif end == begin + 1:
                out.extend( [str(begin), str(end)] )
            else:
                out.append( str(begin) + "-" + str(end) )
            begin = n
        end = n
    
    return ",".join(out)

print(solution([-6,-3,-2,-1,0,1,3,4,5,7,8,9,10,11,14,15,17,18,19,20]))
