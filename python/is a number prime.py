import math

def is_prime(num):
  if num <= 1:
    return False
  elif num <= 3: 
    return True
  elif num % 2 == 0 or num % 3 == 0:
    return False

  sqrt_n = int(math.sqrt(num))
    
  for i in range(5, sqrt_n + 1, 6):
    if num % i == 0 or num % (i + 2) == 0:
        return False
  return True
