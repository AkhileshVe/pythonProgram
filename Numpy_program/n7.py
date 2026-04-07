import numpy as np

# np.abs()- Absolute value of each element.
# np.sqrt()- Square root of each element.
# np.power()- Element-wise power (raise each element to a certain power).
# np.mod()- Element-wise modulus (remainder of division).
# np.arcsin()- Inverse sine (arc sine).
# np.arccos()- Inverse cosine (arc cosine).
# np.arctan()- Inverse tangent (arc tangent).
# np.deg2rad()- Convert degrees to radians.
# np.rad2deg()- Convert radians to degrees.
# np.floor()- Round down to the nearest integer.
# np.ceil()- Round up to the nearest integer.
# np.round()- Round to the nearest integer (or specified decimal places).
# np.sign()- Return the sign of each element (1,-1,or 0).
# np.clip()- Clip (limit) the values of an array to a given range. 

ar1 = np.array([-1,-2,-3,-4,-5])
print(np.abs(ar1))

ar2 = np.array([1,2,3,4,5])
print(np.sqrt(ar2))

print(np.power(ar2,4))

print(np.mod(ar2,3))

arr3 = np.array([0.25,0.45,0.75,0.90])
print(np.arcsin(arr3))
print(np.arccos(arr3))
print(np.arctan(arr3))
print(np.deg2rad(arr3))
print(np.rad2deg(arr3))

arr4 = np.array([1.2,2.3,3.9,7.5])

print(np.floor(arr4))
print(np.ceil(arr4))
print(np.round(arr4))
print(np.round(arr4))


print(np.sign(arr4))
print(np.clip(arr4,1,3))

print(np.add(np.array([1,2,3]),np.array([4,5,6])))
print(np.subtract(np.array([1,2,3]),np.array([4,5,6])))
# np.multiply()
# np.divide()