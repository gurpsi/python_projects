'''
List a = [1,2,3]
List occupies more space as we have more number of methods available with it and it is mutable.
i.e. Add, Remove, Change data.

Tuple b = (1,4,6,9)
Occupies less memory as we have less number of methods available with it, and it is immutable.
i.e. Cannot be changed.
'''

import sys
import timeit

# print(dir(sys))

list_eg = [1,2,3,"a","b","c",True,3.14]
tuple_eg = (1,2,3,"a","b","c",True,3.14)

print("List size = ", sys.getsizeof(list_eg))
print("Tuple size = ", sys.getsizeof(tuple_eg))


# In terms of big data sets tuple is created more quickly than lists.

list_test = timeit.timeit(stmt="[1,2,3,4,5]", number=1000000)
tuple_test = timeit.timeit(stmt="(1,2,3,4,5)", number=1000000)

print("List time:", list_test)
print("Tuple time:", tuple_test)

# Tuple Assingment:

test = 1, # The comma is necessary to tell python that we want it in tuple.
test2 = 1,2,3

test3 = (3,)
test4 = (1,2,3,4)

print(test,'\t',type(test))
print(test2,'\t',type(test2))
print(test3,'\t',type(test3))
print(test4,'\t',type(test4))