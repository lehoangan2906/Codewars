bool isPrime(int n) {
    if (n <= 1) {
        return false;  // Numbers less than or equal to 1 are not prime
    }
    if (n <= 3) {
        return true;   // 2 and 3 are prime
    }
    if (n % 2 == 0 || n % 3 == 0) {
        return false;  // Multiples of 2 and 3 are not prime
    }

    int sqrtN = sqrt(n);

    // Check for prime using 6k +/- 1 rule
    for (int i = 5; i <= sqrtN; i += 6) {
        if (n % i == 0 || n % (i + 2) == 0) {
            return false;  // If n is divisible by any number in the form 6k ± 1, it's not prime
        }
    }

    return true;  // If no divisors are found, n is prime
}

