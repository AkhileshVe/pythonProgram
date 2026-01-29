# ++++++++++++++++++++++++++++++++++++...1...+++++++++++++++++++++++++++
#  2!, 4!, 6! 
# 2 + 24 + 720 = 746

# i = 1
# n = int(input("enter any number : "))
# sum=0
# while(i<=n):
#     r = i*2
#     j = 1
#     fact =1
#     while(j <= r):
#         fact  = fact*j
#         j+=1
#     sum= sum+fact
#     print(fact ,end=" ")
#     if(i<=n-1):
#         print("+" ,end=" ")
#     else:
#         print("=" ,sum,end=" ")
#     i+=1
    # 2,24,720 = 746 ans

# ++++++++++++++++++++++++++++++++++++...2...+++++++++++++++++++++++++++

# 1! + 3! + 5! ........n 

# i = 1
# n = int(input("enter any number : "))
# sum=0

# while(i<=n):
#     j=1
#     fact=1
#     while(j<=i*2-1):
#         fact=fact*j
#         j+=1
#     sum += fact
#     print(fact, end=" ")
#     if(i<=n-1):
#         print("+", end=" ")
#     else:
#         print("=" ,sum, end=" ")
#     i+=1

    # ++++++++++++++++++++++++++++++++++++...3...+++++++++++++++++++++++++++

# 1! + 3! + 5! ........n 

# i = 1
# n = int(input("enter any number : "))
# sum=0

# while(i<=n):
#     j=1
#     fact=1
#     while(j<=i*2-1):
#         fact=fact*j
#         j+=1
    
#     print(fact, end=" ")
#     if(i<=n):
#         if(i%2==0):
#             sum += fact
#         else:
#             sum -= fact
#     if(i<=n-1):
#         if(i%2==0):
#             print("+", end=" ")
#         else:
#             print("-", end=" ")
#     else:
#         print("=" ,sum, end=" ")


    
#     i+=1


# i = 1
# n = int(input("Enter number of terms: "))
# sum = 0

# while i <= n:
#     num = 2 * i - 1     # 1, 3, 5, ...
#     j = 1
#     fact = 1

#     while j <= num:
#         fact *= j
#         j += 1

#     print(fact, end=" ")

#     if i % 2 != 0:          # odd term → +
#         sum += fact
#         if i != n:
#             print("-", end=" ")
#     else:                   # even term → -
#         sum -= fact
#         if i != n:
#             print("+", end=" ")

#     i += 1

# print("=", sum)


# ++++++++++++++++++++++++++++++++++++...4...+++++++++++++++++++++++++++



