# i = 2
# n = int(input("Enter a number: "))
# count = 0
# is_prime = True

# if n <= 1:

#     is_prime = False
# else:
#     while i < n:
#         if n % i == 0:
#             count+=1
#             is_prime = False
#             break
#         i += 1

# if count == 0:
#     print(n, "is a prime number")
# else:
#     print(n, "is not a prime number")



# prime number using for loop

n = int(input("Enter a number: "))
count = 0

for x in  range(2,n):
    if(n % x == 0):
        count += 1
        break
    

if(count == 0):
    print(n, "is a prime number")
else:
    print(n, "is not a prime number")
