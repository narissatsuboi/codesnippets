"""
Python Tutorial: Itertools Module - Iterator Functions for Efficient Looping
https://www.youtube.com/watch?v=Qu3dThVy6KQ
"""

import itertools 

print()
print('>> Example: Simple Counter')
counter = itertools.count() 
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print()

print('>> Example: Pair counter items with other iterable data')
data = [100, 200, 300, 400]
# x - axis is day, day 0 , day 1, day 2 
# y - axis is data for corresponding day 
daily_data = list(zip(itertools.count(), data))
print('Zipped cout with list of data')
print(daily_data)
print()

print('>> Counter has start and step parameters')