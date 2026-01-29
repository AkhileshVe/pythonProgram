#find a sum of first even number


# i = 1
# sum = 0
# n =int(input("enter even number"))
# while(i <= n):
#     res = 2*i
#     sum +=res
#     #print("sum = ", res)
#     i = i+1

# print("sum = ", sum)


#find a sum of first natural number

# i = 1
# sum = 0
# n =int(input("enter odd number"))
# while(i <= n):
#     res = 2*i-1
#     sum +=res
#     #print("sum = ", res)
#     i = i+1

# print("sum = ", sum)



# i = 1
# sum = 0
# n =int(input("table of number"))
# while(i <= 10):
#     res = n*i
  
#     print( n ," * ",i," = ", res)
#     sum += res
#     i = i+1

# print("sum = ", sum)


# 1,2,4,7,11,16,22,29,38

# i = 1
# res= 0
# sum=1
# n = int(input("Enter a number = "))

# while(i<=n):
#     print(sum, end= " ")
#     res+=sum
#     sum +=i
#     if(n>i):
#           print("+", end=" ")
#     i+=1
# print("result = ",res)

# output should be 1,2,4,7,11,16,22,29,38

# for i in range(1, n+1):
#      print(sum)
#      res += sum 
#      sum +=i
#      if(n>i):
#           print("+")

# print("result = ",res)


# find the factorial of the given number

# i = 1
# n= int(input("enter the value"))
# fect = 1

# while(i<=n):
   
#     fect = fect * i
#     print(fect, end = " ")
#     if(n>i):
#           print("*", end = " ")
#     i+=1
# print("factorial = ",fect)



# # find the sum  factorial of the given number

# i = 1
# n= int(input("enter the value"))
# fect = 1
# sum = 0
# even = 0
# while(i<=n):
   
    
#     even += i+1

    

#     fect = fect * i
#     print(fect, end = " ")
#     if(i%2 == 0): 
#          sum = sum - fect
#          print("-", end = " ")
#     else:
#          sum = sum + fect
#          print("+", end = " ")
        
#     i+=1
# print("factorial = ",sum)




# find the factorial of the given number

# i = 1
# n= int(input("enter the value"))
# fect = 1
# sum = 0
# div = 1
# while(i<=n):
#     fect = fect * i
#     div = fect/i
#     sum = sum + div
#     print(fect, end = " ")
#     if(n>i):
#           print("*", end = " ")
#     i+=1
# print("factorial = ",sum)



i = 1
n= int(input("enter the value"))
fect = 1
sum = 0 
while(i<=n):
   
    fect = fect * i
    print(fect, end = " ")
    if(n*2>i):
          print("+", end = " ")
    i+=1
    sum = sum + fect
print("factorial = ",sum)
 



