import numpy as np
from PIL import Image
from pathlib import Path
# pip install pillow




l3 = [
    [
     [10,20,20],
     [25,30,30],
    #  [111,222,70]
     ],

    [
     [40,50,21],
     [65,70,21],
    #  [14,92, 23]
     ],
]

ar3 = np.array(l3)

# print(ar3.ndim)
# print(ar3.shape)

# first_block = ar3[0]
# second_block = ar3[1]

# print(np.mean(ar3))
# print(first_block)
# print("first block average", np.mean(first_block))
# print("first block first row average", np.mean(first_block[0]))
# print(second_block)
# print("second block average", np.mean(second_block))
# print("second block second row average", np.mean(second_block[1]))


# # fetch element using index
# print("******************************. Index wise elemnt *****************")
# print(ar3[0,0,0])
# print(ar3[0,0,1])
# print(ar3[0,0,2]) 
# print(ar3[0,1,0])
# print(ar3[0,1,1])
# print(ar3[0,1,2])



# print(ar3[1,0,0])
# print(ar3[1,0,1])
# print(ar3[1,0,2])
# print(ar3[1,1,0])
# print(ar3[1,1,1])
# print(ar3[1,1,2])
# print("******************************. end *****************")




# # fetch element using slice

# print("******************************. slice wise elemnt *****************")
# print(ar3[0:2, 0:2,0:1])
# print(ar3[0:2, 0:2,1:2])

# print("******************************. end *****************")



# print("******************* using loop ******************")

# for i in ar3:
#     for j in i:
#          for k in j:
#             print("col",k)


# print("******************* using index ******************")

# for i in range(ar3.shape[0]):
#     for j in range(ar3.shape[1]):
#        for k in range(ar3.shape[2]):
#            print(ar3[i,j,k])


# print("******************* convert arrey to 3d to others ******************")

# ar1=ar3.flatten()
# print("1d array to use flatten", ar1)
# print("this is 3d array", ar3)

# ar2 = ar3.reshape(2,6)
# print("2d array to use reshape", ar2) # with the help of reshape we can make 3d also give the paramiter

# new_3d = ar2.reshape(3,1,4)
# print("3d array to use reshape",new_3d)


# n1 = np.array([[[10,20,30,40]]])
# n2 = np.array([[[2,3,4,5]]])

# add_result = np.add(n1,n2)
# subtract_result = np.subtract(n1,n2)
# multiply_result = np.multiply(n1,n2)
# divide_result = np.divide(n1,n2)


# print(add_result)
# print(subtract_result)
# print(multiply_result)
# print(divide_result)






# # pip install pillow

# img = Image.open(Path(r"/Users/akhileshverma/Downloads/WhatsApp Image 2026-03-16 at 16.47.08.jpeg"))
# arr = np.asarray(img)
# print(arr)
# print(arr.shape)
# print(arr.dtype)
# print(arr.itemsize)

print(np.sum(ar3[0]))