# def fact(x):
#     print(x)
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

def fib(x):
    y = x
    z=1
    # print(y)
    if(y == 1):
        f = 1
    else:
        f = y - fib(y-1)
        z  += y 
        print(z)
    return f

fib(21)
# print(resu)