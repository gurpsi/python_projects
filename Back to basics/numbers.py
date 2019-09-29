num_1 = 2
num_2 = 3
num_3 = '100'
num_4 = '200'

# Getting the data type
print('Type of num_1:', type(num_1))
print('Type of num_3:', type(num_3))

print('Division:', num_1 / num_2)
print('Multiplication:', num_1 * num_2)

print('Floor Division', num_1 // num_2)
print('Exponent/power', num_1 ** num_2)
print('Modulous:', num_2 % num_1)

print('BODMAS:',num_1 ** num_1 * num_2 / (num_1 + num_2)) # 4 * 3 / 5 -> 12/5 -> 2.4

print('Absolute value:', abs(-num_1))
print('BODMAS rounded:', round(num_1 ** num_1 * num_2 / (num_1 + num_2)))
print('BODMAS rounded to first plcae:', round(num_1 ** num_1 * num_2 / (num_1 + num_2), 1))

print('Comparison operators returning True/False:', num_1 == num_2)

print('Adding string variables:', num_3 + num_4)
print('Adding string after casting', int(num_3) + int(num_4))

num_1 += 10
print('Increment by 10:', num_1)
