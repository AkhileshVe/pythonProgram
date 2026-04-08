import numpy as np

arr1 = np.array([10,20,30,40],dtype='int8')
arr2 = np.array([10,20,30,40],dtype='int16')
arr3 = np.array([10,20,30,40],dtype='int32')
arr4 = np.array([10,20,30,40],dtype='int64')


print(arr1.dtype)
print(arr2.dtype)
print(arr3.dtype)
print(arr4.dtype)

arrFloat2 = np.array([10,20,30,40],dtype='float16')
arrFloat3 = np.array([10,20,30,40],dtype='float32')
arrFloat4 = np.array([10,20,30,40],dtype='float64')

print(arrFloat2.dtype)
print(arrFloat3.dtype)
print(arrFloat4.dtype)

a = np.array([1, "Akhilesh", 3.5], dtype=object)
print(a.dtype)



# 🔹 What is Data Type in NumPy?

# Data type (dtype) defines what kind of data is stored in a NumPy array.

# Unlike Python list:
# 👉 NumPy array stores same type of data only (homogeneous)

# 🔹 Check Data Type
# import numpy as np

# a = np.array([1, 2, 3])
# print(a.dtype)

# Output:

# int64
# 🔥 Main Data Types in NumPy
# 1️⃣ Integer Types
# np.int8
# np.int16
# np.int32
# np.int64

# Example:

# a = np.array([1,2,3], dtype=np.int32)
# 2️⃣ Float Types
# np.float16
# np.float32
# np.float64
# a = np.array([1.5, 2.3], dtype=np.float32)
# 3️⃣ Boolean
# np.bool_
# a = np.array([True, False, True])
# 4️⃣ String
# np.str_
# a = np.array(["a", "b", "c"])
# 5️⃣ Complex Numbers
# np.complex64
# np.complex128
# a = np.array([1+2j, 3+4j])
# 🔹 Special Data Type
# Object Type
# np.object_

# Used when mixed data:

# a = np.array([1, "Akhilesh", 3.5], dtype=object)
# 🔥 Important Concept (Auto Conversion)
# a = np.array([1, 2, 3.5])
# print(a.dtype)

# Output:

# float64

# 👉 NumPy converts to highest precision type

# 🔹 Change Data Type (astype)
# a = np.array([1,2,3])

# b = a.astype(float)

# print(b)

# Output:

# [1. 2. 3.]
# 🔥 Memory Importance (Interview Point)
# Type	Size
# int8	1 byte
# int16	2 bytes
# int32	4 bytes
# int64	8 bytes

# 👉 Smaller dtype = less memory

# 🧠 Why dtype Important?

# ✔ Memory optimization
# ✔ Speed improvement
# ✔ ML models require specific types
# ✔ Data consistency

# 🎯 Interview One-Liner

# NumPy dtype defines the type of elements stored in an array and ensures all elements are of the same type for efficient computation.

# 🚀 Practice Task

# Try this:

# arr = np.array([1,2,3,4])

# Do:
# 1️⃣ Convert to float
# 2️⃣ Convert to string
# 3️⃣ Check dtype
# 4️⃣ Create array with int16