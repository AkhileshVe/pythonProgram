import numpy as np

arr1 = np.array([40,10,30,50,20])
print(arr1)
print(np.sort(arr1))
print(np.sort(arr1)[::-1])
print(np.argsort(arr1))
print(np.argmax(arr1))
print(np.argmin(arr1))
print(np.searchsorted(arr1,40))


# np.unique()    imp
print("***************. uniq ***********************************************")
arr2 = np.array([40,20,10,30,50,30,20])
print(np.unique(arr2))


print("***************. count_nonZero ***********************************************")
arr = np.array([0,2,1,0,0,3,0])
print(np.count_nonzero(arr))



print("***************. bincount ***********************************************")
arrb = np.array([0,1,1,1,2,2,3,2])
print(np.bincount(arrb))



print("***************. where ***********************************************")
arr4 = np.array([40,20,10,30,50,30,20])
print(np.where(arr4>25)) #[0, 3, 4, 5])



print("***************. argwhere ***********************************************")
arr5 = np.array([[10,20,30],[40,50,60]])

print(np.argwhere(arr5))


arr6 = np.array([40,20,10,30,50,30,20])
print(np.a(arr6>25)) #[0, 3, 4, 5])