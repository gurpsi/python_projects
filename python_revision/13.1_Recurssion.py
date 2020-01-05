fibonacci_cache = {}
def fibonacci_1(n):
    # If we have cached the value, then return it.
    if n in fibonacci_cache:
        return fibonacci_cache[n]

    # Compute the nth term:
    if n == 1:
        value = 1
    elif n == 2:
        value = 1
    elif n > 2:
        value = fibonacci_1(n-1) +fibonacci_1(n-2)

    # Cache the value and return it:
    fibonacci_cache[n] = value
    return value

for n in range(1,1010):
    print(n, ":", fibonacci_1(n))