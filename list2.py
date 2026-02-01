ls = [76, 34, 89, 45, 24, 66, 59]
ls2 = [6, 4, 3, "jai", 45]

ls.sort()  # for shorting assending order
print(ls)

ls.reverse()  # for reverse all the list order
print(ls)

ls.clear() # for clear the all list and return empty list
print(ls)
print(len(ls))  # to find the length of list

del ls # to delete the list 

ls.pop() # remove the last object
print(ls)

ls.remove(66) # remove the perticular object [76, 34, 89, 45, 24, 59]
print(ls)

print(ls.count(24)) # to count the perticular object in the list


ls.append(23) # to add a 23 at last index with the help of append
print(ls)

ls.insert(2,67)  # to add a 67  at 2 index with the help of insert and sift all the object after the second index
print(ls)

ls.extend(ls2) # to merge the second list in first list 
print(ls)


ls3 = ls + ls2  #  
print(ls3)

lis = []
n = n = int(input("How amny obj you want to add : "))
i = 1

for i in range (1 <= 6):
    n = int(input("enter any 5 obj : "))
    lis.append(n)
print(lis)

while i <= n:
    print("Enter", i , "element")
    data = input()
    lis.append(data)
    i += 1
print(lis)

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

n = int(input("enter the number : "))
i = 0
ls1 =[]


while i < n:
    ls1.append([])
    j = 0
    jls = ["Name", "roll no.", "address"] 
    while j < len(jls):
        print("enter ", i+1, jls[j], " : ")
        data = input()
        ls1[i].append(data)
        j += 1
    i += 1

print(ls1)


