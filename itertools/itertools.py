"""
Python Tutorial: Itertools Module - Iterator Functions for Efficient Looping
https://www.youtube.com/watch?v=Qu3dThVy6KQ
https://docs.python.org/3/library/itertools.html#itertools.count 
"""

import itertools 


print('--------------------------------------')
print('ITERTOOLS SNIPPETS')
print('counter')
print('zip_longest')
print('cycle')
print('repeat')
print('combination / permutation')
print('chain')
print('islice')
print('select specific data')
print('accumulate')
print('groupby')
print('tee')
print('--------------------------------------\n')


print('--------------------------------------')
print('COUNTER')
print('--------------------------------------\n')

print('--------------------------------------')
print('>> Simple counter')
counter = itertools.count() 
print(next(counter), end= ' ')
print(next(counter), end= ' ')
print(next(counter), end= ' ')
print(next(counter), end= ' ')
print()
print('--------------------------------------')

print('>> Pair counter items with other iterable data')
data = [100, 200, 300, 400]
# x - axis is day, day 0 , day 1, day 2 
# y - axis is data for corresponding day 
daily_data = list(zip(itertools.count(), data))
print('Zipped cout with list of data')
print(daily_data)
print('--------------------------------------')

print('>> Counter starts at 5')
counter = itertools.count(start=5) 
print(next(counter), end= ' ')
print(next(counter), end= ' ')
print(next(counter), end= ' ')
print(next(counter), end= ' ')
print()
print('--------------------------------------')

print('>> Counter steps by 5')
counter = itertools.count(step=5) 
print(next(counter), end= ' ')
print(next(counter), end= ' ')
print(next(counter), end= ' ')
print(next(counter), end= ' ')
print()
print('--------------------------------------')

print('>> Counter steps backward by 5')
counter = itertools.count(step=-5) 
print(next(counter), end= ' ')
print(next(counter), end= ' ')
print(next(counter), end= ' ')
print(next(counter), end= ' ')
print()
print('--------------------------------------')


print('--------------------------------------')
print('ZIP_LONGEST')
print('--------------------------------------\n')

"""
zip vers zip_longest
"""
print('>> zip verus long zip ')
print('zip pairs until one iterable runs out of items...')
print('given a range of 10 and a list of 4, zip will stop at 4 pairs...')
daily_data = list(zip(range(10), data))
print(daily_data)
print()
print('zip_longest pairs until the longest iterable runs out of objects')
print('and fills the rest with none values')
daily_data = list(itertools.zip_longest(range(10), data))
print(daily_data)
print('--------------------------------------')


print('--------------------------------------')
print('CYCLE')
print('--------------------------------------\n')

print('>> given an iterable, cycle through those values over and over')
counter = itertools.cycle([1, 2, 3])
print(next(counter), end= ' ')
print(next(counter), end= ' ')
print(next(counter), end= ' ')
print(next(counter), end= ' ')
print(next(counter), end= ' ')
print(next(counter), end= ' ')
print()
print('--------------------------------------')


print('>> use cycle to simulate state')
counter = itertools.cycle(('On', 'Off'))
print(next(counter), end= ' ')
print(next(counter), end= ' ')
print(next(counter), end= ' ')
print(next(counter), end= ' ')
print(next(counter), end= ' ')
print(next(counter), end= ' ')
print()
print('--------------------------------------')

print('--------------------------------------')
print('REPEAT')
print('--------------------------------------\n')

print('>> repeat the same value indefinately')
counter = itertools.repeat('same val')
print(next(counter), end= ' ')
print(next(counter), end= ' ')
print(next(counter), end= ' ')
print(next(counter), end= ' ')
print()
print('--------------------------------------')

print('>> repeat the 3 times')
counter = itertools.repeat('same val', times=3)
print(next(counter), end= ' ')
print(next(counter), end= ' ')
print(next(counter), end= ' ')
print()
print('--------------------------------------')

print('>> use repeat with map to calc squares of nums 0 through 9')
squares = list(map(pow, range(10), itertools.repeat(2)))
print(squares, end= ' ')
print() 
print('--------------------------------------')

"""
starmap + repeat  
"""
# starmap takes eles already paired as iterables 
print('>> starmap with repeat')
squares = list(itertools.starmap(pow, [(0,2), (1,2), (2, 2)]))
print(squares, end= ' ')
print() 
print('--------------------------------------')

print('--------------------------------------')
print('COMBINATION / PERMUTATION')
print('--------------------------------------\n')
letters = ['a', 'b', 'c', 'd']
numbers = [0, 1, 2, 3]
names = ['Corey', 'Nicole']
print('>>  Get all the possible combinations of 2 values in each')
print('iterable: ', letters)
combos = itertools.combinations(letters, 2)
print('combos:  ', end = ' ')
for item in combos:
    print(item, end= ' ')
print() 
print('--------------------------------------')

print('>> Get all the possible permuitations of 2 values in each')
print('iterable: ', letters)
perms = itertools.permutations(letters, 2)
print('permuata:  ', end = ' ')
for item in perms:
    print(item, end= ' ')
print() 
print('--------------------------------------')

print('>> Create a 3 digit code including repeats with product')
print('iterable: ', numbers)
perms = itertools.product(numbers, repeat=3)
print('permuata:  ', end = ' ')
for item in perms:
    print(item, end= ' ')
print() 
print('--------------------------------------')

print('>> Create a 3 digit combinations with replacement')
print('iterable: ', numbers)
perms = itertools.combinations_with_replacement(numbers, 3)
print('permuata:  ', end = ' ')
for item in perms:
    print(item, end= ' ')
print() 
print('--------------------------------------')

print('--------------------------------------')
print('CHAIN')
print('--------------------------------------\n')

print('>> Loop over all values in the sample lists without combining the lists')
print('CANNOT do newList = letters + numbers + names')
combined = itertools.chain(letters,numbers,names)
for item in combined:
    print(item, end = ' ')
print() 
print('--------------------------------------')

print('--------------------------------------')
print('ISLICE')
print('--------------------------------------\n')

print('>> Get the first five elements in an iterable of 10 elements')
result = itertools.islice(range(10), 5)  # stopping point 
for item in result:
    print(item, end=' ')
print() 
print('--------------------------------------')

print('>> Get the first five elements in an iterable of 10 elements starting from the second element')
result = itertools.islice(range(10), 1, 5)  # starting point / stopping point 
for item in result:
    print(item, end=' ')
print() 
print('--------------------------------------')

print('>>  Get the first five elements stepped by 2 in an iterable of 10 elements starting from the second element')
result = itertools.islice(range(10), 1, 5, 2)  # starting point / stopping point / step
for item in result:
    print(item, end=' ')
print() 
print('--------------------------------------')

print('>> Get the first 3 lines from the logfile')
# files are iterators too! 
with open('logfile.txt', 'r') as f: 
    header = itertools.islice(f, 3)  # stop at 3rd line of file 

    for line in header: 
        print(line, end='')
print() 
print('--------------------------------------')

print('--------------------------------------')
print('SELECT SPECIFIC DATA')
print('--------------------------------------\n')

# you have a list of true false values corresponding to the letters list 
selectors = [True, True, False, True] 
print('>> Compress the letters with the True selectors')
print('letters:   ', letters)
print('selectors: ', selectors)
result = itertools.compress(letters, selectors)
print('result:    ', end=' ')
for item in result:
    print(item, end=' ')
print()
print('--------------------------------------')
# compare to filter, filter needs a function 

print('>> use filter to get vals less than 2 from numbers list')
def valsLessThan2(n): 
    if n < 2: 
        return True
    return False 

result = filter(valsLessThan2, numbers)

for item in result: 
    print(item, end=' ')
print()
print('--------------------------------------')

print('>> use filterfalse to get vals greater than 2 from numbers list')
result = itertools.filterfalse(valsLessThan2, numbers)
for item in result: 
    print(item, end=' ')
print()
print('--------------------------------------')

# dropwhile drops values from an iterable until one of the values returns true 
print('>> use dropwhile to get vals greater than 2 from numbers list')
numbers2 = [0, 1, 2, 3, 2, 1, 0]
result = itertools.dropwhile(valsLessThan2, numbers2)
for item in result: 
    print(item, end=' ')
print()
print('--------------------------------------')

# takewhile keeps all values that return true, until it hits a false value
# then it returns the values it had up until that point 
print('>> use takewhile to values until first item to return false')
numbers2 = [0, 1, 2, 3, 2, 1, 0]
result = itertools.takewhile(valsLessThan2, numbers2)
for item in result: 
    print(item, end=' ')
print()
print('--------------------------------------')

print('--------------------------------------')
print('ACCUMULATE')
print('--------------------------------------\n')

# accumulate - sum items it sees 
print('>> Print the running total of the numbers list at each iteration')
result = itertools.accumulate(numbers)
for item in result: 
    print(item, end= ' ')
print()
print('--------------------------------------')

# accumulate - product 
import operator 
print('>> Print the running product of numbers')
numbers3 = [1, 2, 3]
result = itertools.accumulate(numbers3, operator.mul)
for item in result: 
    print(item, end= ' ')
print()
print('--------------------------------------')

print('--------------------------------------')
print('GROUPBY')
print('--------------------------------------\n')

people = [
    {
        'name': 'John Doe',
        'city': 'Gotham',
        'state': 'NY'
    },
    {
        'name': 'Jane Doe',
        'city': 'Kings Landing',
        'state': 'NY'
    },
    {
        'name': 'Corey Schafer',
        'city': 'Boulder',
        'state': 'CO'
    },
    {
        'name': 'Al Einstein',
        'city': 'Denver',
        'state': 'CO'
    },
    {
        'name': 'John Henry',
        'city': 'Hinton',
        'state': 'WV'
    },
    {
        'name': 'Randy Moss',
        'city': 'Rand',
        'state': 'WV'
    },
    {
        'name': 'Nicole K',
        'city': 'Asheville',
        'state': 'NC'
    },
    {
        'name': 'Jim Doe',
        'city': 'Charlotte',
        'state': 'NC'
    },
    {
        'name': 'Jane Taylor',
        'city': 'Faketown',
        'state': 'NC'
    }
]

print('>>  Group people by state they are from')
# group by expects data to be sorted by the key in advance 
# write a function to tell group by what to return 
def get_state(person): 
    return person['state'] # key to return to group by 

person_group = itertools.groupby(people, get_state)

for key, group in person_group: 
    print(key)
    for person in group: 
        print(person)
    print() 
print()
print('--------------------------------------')

print('--------------------------------------')
print('TEE')
print('--------------------------------------\n')

copy1, copy2 = itertools.tee(person_group)
# don't use the original iterator after your copy it! 
