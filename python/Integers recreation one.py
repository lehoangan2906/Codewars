import math

def list_squared(m, n):
    result = []
    
    # loop through all the numbers lie in the range m to n
    for num in range(m, n+1):
        
        # create an empty set to store the divisors of the number (if exist)
        divisors = set()
        
        # loop from 1 to the square root of the number
        for i in range(1, int(math.sqrt(num) + 1)):
            
            """
            By looping from 1 to sqrt(num)+1, we can conclude that if 
            i (current item in the loop) is a factor of num then num 
            divided by i must be another one.

            Eg: 2 is a factor of 10, so is 5 (10/2)
            """
            
            if num % i == 0:
                divisors.add(i ** 2)
                divisors.add(int(num/i) ** 2)
                
        total = sum(divisors)
        sqrt_sum = math.sqrt(total)
            
        if sqrt_sum - math.floor(sqrt_sum) == 0:
            result.append([num, total])
                
    return result
