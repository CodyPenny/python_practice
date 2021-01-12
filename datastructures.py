# data structures are containers that organize and group data types together

# LIST
months = [ 'jan', 'feb', 'mar', 'apr', 'may']

# can contain a mix of data types
list_of_random_things = ['string', 3, True]

# can use len() method
# can use negative index, -1 is the last element
# is an item in a list? use 'in' or 'not in' keyword, returns bool
print(5 in list_of_random_things)

# mutability - can an object change once it's been created
# lists are mutable. Strings are NOT mutable or immutable
# order - if position of an element can be used to access the element
# strings and lists are ordered
# list methods
list_of_nums = [ 3, 5, 45, 2, 15 ]
print(len(list_of_nums))
print(min(list_of_nums))
print(max(list_of_nums))
print(sorted(list_of_nums))

# join is a string method that takes a list of strings as an argument, and returns a string of list items joined by a separator string
new_str = '\n'.join(['this', 'is', 'a', 'list'])
print(new_str)

# append adds an item to the end of the list

# TUPLES

# for immutable ordered sequence - can't add, remove or sort them in place
# often to store related pieces of info
# use parenthesis but also can be omitted if it doesn't clarify the code
# can use index to access and it can hold different types
# can assign multiple variables in a compact way
# useful for data integrity

dimensions = 15, 14, 10
# tuple unpacking
length, width, height = dimensions
print(f'dimensions are {length} {width} {height}')
# or even in one line
length2, width2, height2 = 17, 19, 20

# tuples have method count and index

# SETS
# for mutable, unordered collection of unique elements
# application is to quickly remove dups from a list
nums = [ 2, 4, 6, 8, 12, 16, 1, 4, 2, 6, 3, 5, 7]
unique_nums = set(nums)
print(unique_nums) # {1, 2, 3, 4, 5, 6, 7, 8, 12, 16}

# sets support the in operator as lists do
# use curly braces to define or set()
# can use add method, pop method removes a random element
# it's unordered so there is no 'last' element

fruit = {'apple', 'fruits', 'watermelon', 'grapes', 'cherries'}
print('melon' in fruit) # False

fruit.add('melon')
print('fruit', fruit)

print(fruit.pop())

# sets can performm mathematical sets, union, intersection, difference and are faster than other containers
