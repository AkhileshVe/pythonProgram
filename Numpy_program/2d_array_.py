import numpy as np

# ar1= np.array([10,20,30,40,50,60])
# print(ar1.ndim)
# print(ar1.dtype)
# print(ar1.size)
# print(ar1.shape)
# print(ar1.itemsize)

# print("********************* Agg function in the numpy array *******************")
# print("Max Ele",np.max(ar1))
# print("Min Ele",np.min(ar1))
# print("Avg Ele",np.mean(ar1))
# print("Mid Ele",np.median(ar1))
# print("Sum Ele",np.sum(ar1))
# print("Var result ",np.var(ar1))
# print("Std Div ",np.std(ar1))

# aggregate
# max()
# min()
# mean()
# median()
# sum()
# Varience


# **************** 

print("********************* Agg function in the numpy  2d array *******************")

arr2 = np.array([
    [10,20,30],
    [40,50,60]
])

# print("size of arrray",np.size(arr2))
# print(arr2[0])
# print(arr2[1])

# print("********************* first row of element *******************")
# print(arr2[0,0])
# print(arr2[0,1])
# print(arr2[0,2])
# ar1d = arr2[0]
# print("Max Ele",np.max(ar1d))
# print("Min Ele",np.min(ar1d))
# print("Avg Ele",np.mean(ar1d))
# print("Mid Ele",np.median(ar1d))
# print("Sum Ele",np.sum(ar1d))
# print("Var result ",np.var(ar1d))
# print("Std Div ",np.std(ar1d))
# print("********************* Second row of element *******************")
# print(arr2[1,0])
# print(arr2[1,1])
# print(arr2[1,2])

# ar2d = arr2[0]
# print("Max Ele",np.max(ar2d))
# print("Min Ele",np.min(ar2d))
# print("Avg Ele",np.mean(ar2d))
# print("Mid Ele",np.median(ar2d))
# print("Sum Ele",np.sum(ar2d))
# print("Var result ",np.var(ar2d))
# print("Std Div ",np.std(ar2d))


# using slice operator


slarr = np.array([
    [10,20,30],
    [40,50,60]
])

print(slarr[0:1,0:2])# [[10 20]]
print(slarr[0:1,1:3])# [[20 30]]

print(slarr[0:2,1:3])# [[20 30],[50 60]]

print(slarr[0:2,0:1])# [[10][40]]
print(slarr[0:2,1:2])# [[20][50]]
 
print(slarr[0:2,2:3])# [[30][600]]


# ////////////////////////////

print(slarr.shape)
print(slarr.shape[0])
print(slarr.shape[1])
# rkfnd jknrkjfdnjkr