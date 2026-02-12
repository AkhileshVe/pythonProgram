# def fact(x):
#     # print(x)
#     if(x == 1):
#         f = 1
#     else:
#         f=x*fact(x-1)
#     return f
# res = fact(5)
# print("fact = ",res)

# natural number sum using recursion
# input digit sum using recursion
# print the fibonacci seris using recursion

# def natural(x):
#     print(x)
#     if(x==1):
#         f=1
#     else:
#         f = x+natural(x-1)
#     return f

# result = natural(5)
# print(result)


# print the fibonacci seris using recursion (0,1,1,2,3,5,8,13,21)








# dusra tarika fabinachi
def fib(x ,n1=0, n2=1):
    if x > 0:
        print(n1)
        fib(x-1,n2,n1+n2)

fib(8)
     

     