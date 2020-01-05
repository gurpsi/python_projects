from functools import lru_cache

# LRU cache = Least Recently Used Cache

@lru_cache(maxsize=1000) # Default is 128 (i.e last 128 values are cached)
def fibonacci_2(n):
    # Check the input is a positive integer:
    if type(n) != int:
        raise TypeError("n must be positive int")
    if n < 1:
        raise ValueError("n must be a positive int")

    # Conpute the nth term
    if n == 1:
        return 1
    elif n == 2:
        return 1
    elif n > 2:
        return fibonacci_2(n-1) + fibonacci_2(n-2)


for n in range (1,1000):
    print(n, ":", fibonacci_2(n))

print(fibonacci_2('One'))