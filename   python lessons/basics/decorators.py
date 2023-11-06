# def outer(func):
#     def inner():
#         print("before ")
#         func()
#         print("after")
#     return inner

# def hey():
#     print("Hello")

# hey = outer(hey)
# hey()

# import time
# import math

# def time_cal(func):
#     def inner(*args, **kwargs):
#         b = time.time()
#         func(*args, **kwargs)
#         e = time.time()
#         print("{func.__name__}", e-b)
#     return inner
# @time_cal
# def fac(n):
#     print(math.factorial(n))

# fac(10)

# def outer(func):
#     def inner(*args, **kwargs):
#         r = func(*args, **kwargs)
#         return r
#     return inner
# @outer
# def add(a,b):
#     return a+b
  
# print("The sum is: ",add(1,2))  

# import time
# import math
# def outer(func):
#     def inner(*args, **kwargs):
#         b = time.time()
#         r = func(*args, **kwargs)
#         e = time.time()
#         return f'Result {r} of  {func.__name__} in {e-b}'
#     return inner

# @outer
# def fac(n):
#     time.sleep(5)
#     return math.factorial(n)

# print(fac(10))    

# def wrapper(f):
#     def fun(l):
#         li = []
#         for i in l:
#             i = str(i)
#             if i[0]=='0':
#                 n = f'+91 {i[1:6]} {i[6:11]}'
#                 li.append(n)
#             elif i[0:2]=='91':
#                 n = f'+91 {i[2:7]} {i[7:12]}'
#                 li.append(n)
#             elif i[0:3]=='+91':
#                 n = f'+91 {i[3:8]} {i[8:13]}'
#                 li.append(n)
#             # li.append(n)
#         print(li)
#         f(li)
#     return fun

# @wrapper
# def sort_phone(l):
#     print(*sorted(l), sep='\n')
    
# l = [ 7895462130,919875641230,9195969878]
# # if __name__ == '__main__':
# #     l = [input() for _ in range(int(input()))]
# sort_phone(l) 
    
    

# def outer(func):
#     def inner(l):
#         li =[]
#         for i in l:
#             li.append(f'+91 {i[-10:-5]} {i[-5:]}')
#         func(li)
#     return inner

# @outer
# def p(l):
#     print(*l,sep='\n')
     
# if __name__=="__main__":
#     l= [input() for i in range(int(input("Kati ota")))] 
#     p(l)   
# from functools import reduce
# print(reduce((lambda x,y:x+y),[1,2,3],9))

# from fractions import Fraction
# from functools import reduce

# def product(fracs):
#     t = reduce(lambda x,y:x*y,fracs)
#     return t.numerator, t.denominator

# if __name__ == '__main__':
#     fracs = []
#     for _ in range(int(input())):
#         fracs.append(Fraction(*map(int, input().split())))
        
#     result = product(fracs)
#     print(*result)
