# i = 1


# while i< 3:
#     # print(i)
#     j =1
#     while j < 4:
#         print(i , " ", j)
      
#         j += 1

#     i +=1


# for i in range(1, 6):
#     for j in range(1,6):
#         if(j <= i):
#             print(j,end = "")

#         else:
#             print(" ", end = " ")


for i in range(1, 6):
    for j in range(1, 6):
        if j <= i:
            print(j, end=" ")
        else:
            print(" ", end=" ")
    print()   # new line after each row
