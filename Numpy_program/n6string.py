import numpy as np

arr1 = np.array(["ajay, indore", "vijay BHOPAL ", "rahul UjjAin", "RohiT, Dewas"])

arr2 = np.array([" sHArma", "VERMA", "sonu.  ",  "  sahu",  "thakur" ])
# # np.char.upper
# print(np.char.upper(arr1))
# # np.char.lower
# print(np.char.lower(arr2))

# # np.char.title
# print(np.char.title(arr1))

# # np.char.capitalize
# print(np.char.capitalize(arr1))

# # np.char.strip
# print(np.char.strip(arr1))
# # np.char.split
# print(np.char.split(arr1))

# print(np.char.isupper(arr1))
# print(np.char.islower(arr1))
# print(np.char.isdigit(arr1))
# print(np.char.isalnum(arr1))
# print(np.char.isnumeric(arr1))



arr3 = np.char.add(arr1,arr2)
print(arr3)

arr4 = np.char.multiply(arr2,2)
print(arr4)