
# LISTS: Are mutable
item_1 = ['Pen', 'Cap', 'Notebook', 'Notepad']
item_2 = ['Watch', 'Laptop', 'Earphone']
item_3 = [1,4,3,7,8]

# defining the enpty lists
item_4 = []
item_5 = list()

print('Prints out all the items in list:',item_1)

item_1.append('Eraser')
print('All the items in list after appending:',item_1)

item_2.insert(-1,'Headphone')
print('All the items in list after insertion:',item_2)

item_1.extend(item_2)
print('First list is extended with list 2',item_1)

item_1.remove('Watch')
print('First list after removal of one item:', item_1)

popped = item_1.pop()
print(f'First list after popping one value:{item_1} and popped value is: {popped}')

item_1.reverse()
print('Reversal of first list:', item_1)

item_4 = sorted(item_1)
print('Alphabetically sorted first list:', item_4)

item_1.sort()
print('Alphabetically sorted first list inplace:', item_1)

print(f'Sum:{sum(item_3)}, Min:{min(item_3)}, Max:{max(item_3)}')

print('Returns the index location of the item:',item_3.index(3))

for val in item_3:
	print(val)

for idx, val in enumerate(item_3):
	print(idx, val)

item_5 = '|'.join(item_1)
print('Joining all the items of first list with pipe:',item_5)

item_5 = item_5.split('|')
print('Splitting all the items of first list with pipe:',item_5)

# TUPLE: Are Immutable, i.e. the values in it cant be altered.

tu_1 = ()
tu_2 = tuple()


# SET: Unordered values and No duplicated

set_1 = set()
set_2 = {1,2,4,5,7}

print(set_2)


