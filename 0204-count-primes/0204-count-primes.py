from math import isqrt

class Solution:
    def countPrimes(self, n: int) -> int:
        
        primes = [True] * n

        if n == 0 or n == 1:
            return 0

        primes[0], primes[1] = False, False

        for i in range(2, isqrt(n)+1):
            if primes[i]:
                for j in range(i * i, n, i):
                    primes[j] = False

        return sum(primes)