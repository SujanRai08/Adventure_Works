"""functional programming treats computations
 as the evaluations of mathematical functions 
and avoids changing state or mutable data. python 
supports functional programming concepts like lambda,
 map ,filter and reduce. /"""

# lambda functions 
# anonymous functions - syntax lambda arguments: expression
square = lambda x:x*x
print(square(5))

# map  applies a functions to all items in a iterable
# syntax - map(functions, iterable)
numbers = [1,2,3,4,5]
squares = map(lambda x:x*x , numbers)
print(list(squares))

#filter filteres elements based on a condition sytnax - filter(functions.iterable)
number = [1,2,3,4]
even_number =(list(filter(lambda x:x %2 == 0,numbers)))
print(even_number)

#reduces an iterable to a sindle cumulative value
from functools import reduce
product = reduce(lambda x,y:x*y,numbers)
print(product)