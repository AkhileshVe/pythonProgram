i = 2
n = int(input("Enter a number: "))
count = 0
is_prime = True

if n <= 1:

    is_prime = False
else:
    while i < n:
        if n % i == 0:
            count+=1
            is_prime = False
            break
        i += 1

if count == 0:
    print(n, "is a prime number")
else:
    print(n, "is not a prime number")



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



# ++++++++++++++++++++++++++++++++++++...4...+++++++++++++++++++++++++++

# when i enter 10 the output is (2 3 5 7 11 13 17 19 23 29)

n = int(input("enter any value : "))
i = 2
count = 0

while count < n:
    j=2
    while j<i:
        if( i % j == 0):
            break
        j += 1
    if(j == i):
        print(i, end=" ")
        count +=1

    i +=1


#  prime number up to n using for loop 

n = int(input("Enter any number: "))

for x in range(2, n):
    for j in range(2, x):
        if x % j == 0:
            break
    else:
        print(x)
