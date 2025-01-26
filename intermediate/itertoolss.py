from itertools import groupby, product, permutations, combinations,accumulate
import operator
# a = [1,2,3]
# perm = permutations(a,1)
# print(list(perm))

# a = [1,2,3,4,5]
# acc =accumulate(a,func=operator.mul)
# print(list(a))
# print(list(acc))

a = [1,2,3,4,5]
group_obj = groupby(a,key=lambda x: x<3)
for key,v in group_obj:
    print(key,list(v))

# comb = combinations(a,2)
# print(list(comb))
# a = [1,2]
# b =[3,4]
# prod = product(a,b, repeat=1)
# print(list(prod))