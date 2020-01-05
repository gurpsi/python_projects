def fibonacci(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    elif n > 2:
        return fibonacci(n-1) + fibonacci(n-2)

# If we do for couple e.g. till 10 or so it runs quick but if we want to run it for 101 terms it stucks.
# So to solve this issue we will use the concept of Memorization (Idea: Cache Values) [13.1_Recurssion]


for n in range(1,101):
    print(n, ":", fibonacci(n))


