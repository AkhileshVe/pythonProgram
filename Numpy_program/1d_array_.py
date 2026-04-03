
import numpy as np

l1 = [10,20,30,40]
#print(l1[1])
for x in range(4):
    
      l1[x]=l1[x]+5
      
# print(l1)

# =========    =======    ======      =========           ======     =========     ========     =====
#  list opration........
l1= [2,4,6,8]
l2= [3,6,9,12]

# l3 = l1 +l2 # [5,10,15,20]
# l4 = l1-l2  # [-1,-2,-3,-4]

l3 =[]
l4 = []

for i in range(len(l1)):
     e1 = l1[i]+l2[i]
     e2 = l1[i]-l2[i]
     l3.append(e1)
     l4.append(e2)

# print(l3)
# print(l4)


#  array opration........
lis = [2,4,6,8]
n1 = np.array([2,4,6,8])
n2 = np.array([3,6,9,12])

n3 = n1 + n2
n4 = n1 - n2
n5 = n1 * n2
print(type(lis))
print(type(n1))
print(n3)
print(n4)
print(n5)


# np.array(list,tuple, set)

# n11 = np.array([10,20,30,40,50])
# n11 = np.array([[10,20,30],[40,50,60]])
# print(n11.dtype) # int64. datatype
# print(n11.size) # 5.  size of array
# print(n11.ndim) #  1. dimention
# print(n11.shape) #  (5,) 
# print(n11.itemsize) # 8 
# print(n11)


n = np.array([10,20,30,40,50])
i=0
nl = n.size
while(i < nl):
    #   print(n[i])
      i +=1


# exampl of salary
# salary = [20000,30000,45000,50000]
# salarynp = np.array(salary)
# tax = salarynp*0.10
# actual_salary = salarynp-tax

# print(actual_salary)
# print()

