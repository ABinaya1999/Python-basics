# a = [1,2,3]
# b = iter(a)
# for i in  iter(a):
#     print(i)

# from itertools import *
# d = 1
# for i in count(0,2):
#     if d > 10:
#         break
#     else:
#         print(i)
#     d += 1
# d = 1
# for i in cycle([1,2,3]):
#     if d > 6:
#        break
#     else:
#          print(i)
#     d += 1
# # c = 1
# for i in repeat('binay', 5):
#     # if c > 8:
#     #     break
#     # else:
#     #     print(i)
#     #     c += 1
#     print(i)
# import operator
# for i in accumulate([1,2,3],operator.mul):
#     print(i)
 
# for i in chain([12,33],[3,4]):
#     print(i,end= " ")

# for i in product('binay',repeat=2):
#     print(i)

# from itertools import product
# a= list(map(int,input().split()))
# b = list(map(int,input().split()))      
# print(*product(a,b))

# print(*product('ABC',repeat =2))
# print(*permutations('ABC', 2))
# print(*combinations("ABC",2))

# from itertools import *
# s = input().split()
# so = sorted(s[0])
# ss = "".join(so)
# ss = ss.upper()

# for i in combinations(ss,1):
#     print(*i)

# for i in combinations(ss,2):
#     print(*i)

# from itertools import *

# string, n = input().split()
# n = int(n)

# string = sorted(string)

# for i in range(1, n ):
#     output = combinations(string, i)
    
#     output = sorted([''.join(item) for item in output])
    
#     for item in output:
#         print(item)

# x = list(map(int,input().split()))
# y = list(map(int,input().split()))
# # # print(product(x,y), end = " ")
# print(list(product(x,y)))

# print(*range(1,10 ))

# print(*product(x,y))
# print(list(combinations('abc',2)))
# s = 'binay'
# for i in s:
#     print(i)

# from itertools import combinations

# string, n = input().split()
# n = int(n)
# string = string.upper()
# string = sorted(string)
# # print(string)

# for i in range(1, n + 1):
#     output = [''.join(item) for item in combinations(string, i)]
    
#     for item in output:
#         print(item)

# *********************************************

# from collections import Counter
# # print(Counter ([1,3, 1,2,3]))
# Counter ()
