# Integers 1 to 10:

odds = set([1,3,5,7,9])
evens = set([2,4,6,8,10])
primes = set([2,3,5,7])
composites = set([4,6,8,9,10])

print(odds.union(evens))
print(evens.union(odds))

print(odds)
print(evens)

print(odds.intersection(primes))
print(primes.intersection(evens))

print(2 in primes) # to check if the element is in a set.

# To add elements we can use <set-name>.add

# To remove element we can <set-name>.remove [Prompts error if element is not present].
# Or we can discard the element <set-name>.discard [Doesn't prompt error if element is not present]
