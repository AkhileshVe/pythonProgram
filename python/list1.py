ls =[] # empty list

print(ls) # []
print(type(ls)) # <class list>
print(id(ls))  # address of memory 4349360512
print(ls.__sizeof__()) # default size is 40

ls1 = [76, 34, 89, 45, 24, 66, 59]
print(ls1)                     # print the list 
print(len(ls1))                # find the length of list
print(min(ls1))                # find the minimum value of list 
print(max(ls1))                # find the maximum value of list
print(sum(ls1))                # find the sum of all values of list
print(ls1*3)                   # [76, 34, 89, 45, 24, 66, 59, 76, 34, 89, 45, 24, 66, 59, 76, 34, 89, 45, 24, 66, 59]

print(ls1[2]) # 89 this is how we can find the index
print 

i = 0
for x in ls1:
    ls1[i] = x +2
    i += 1

print(ls1)



for x in ls1:
    if(x%2==0):
        print(x)


# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# maximum


ls1 = [76, 34, 89, 45, 24, 66, 59]
leng = len(ls1)
x = 0
res = 0

while x < leng :
    if(res <=ls1[x]):
        res= ls1[x]
    x+=1
print(res)

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

#  minimum 

ls1 = [76, 34, 89, 45, 24, 66, 59]
leng = len(ls1)
x = 0
res = ls1[0]
while x < leng :
    if(res >=ls1[x]):
        res= ls1[x]
    x+=1
print(res)

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

sum
ls1 = [76, 34, 89, 45, 24, 66, 59]
leng = len(ls1)
x = 0
sum = 0

while x < leng :
    sum = sum + ls1[x]
    x+=1
print(sum)


for i in ls1:
    sum += i
print(sum)
   
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

