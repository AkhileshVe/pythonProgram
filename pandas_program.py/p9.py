# re-indexing 

import pandas as pd


ind = ['a','b','c','d','e','f','g','h']
student = {
    "student_id": [1,2,3,4,5,6,7,8],
    "student_name": ["raj","ravi","riya","rahul","ritesh","jiya","tiya","priya"],
    "age":[26,27,28,26,27,26,27,28],
    "city": ["ind","bpl","jab","sat","ujj","Dev","KTE","SEO"],
    "c_id": [401,401,402,402,403,403,406,406]
}

df = pd.DataFrame(student,index=ind)
print(df)

print()
print()
print("*************************************************.  re-index.  **************************************************")
print()
print()
df2 = df.reindex(['e','h','c','d','f','g','a','b'])
print(df2)





print()
print()
print("*************************************************.  re-index by coloumn.  **************************************************")
print()
print()
df3 = df.reindex(columns=["student_id","c_id","city","student_name","age","address"])
print(df3)


print()
print()
print("*************************************************.  re-index by coloumn. remove nan from address   **************************************************")
print()
print()
df4 = df.reindex(columns=["student_id","c_id","city","student_name","age","address"],fill_value="indore")
print(df4)


print()
print()
print("*************************************************.  re-index get data by perticular index   **************************************************")
print()
print()
df5 = df.set_index('student_id')
print(df5)
print(df5.loc[1])





print()
print()
print("*************************************************.  re-index to remove duplicate    **************************************************")
print()
print()
inde = ['a','b','c','d','e','f','g','h']
students = {
    "student_id": [1,1,3,4,5,6,7,8],
    "student_name": ["raj","raj","riya","rahul","ritesh","jiya","tiya","priya"],
    "age":[26,26,28,26,27,26,27,28],
    "city": ["ind","bpl","jab","sat","ujj","Dev","KTE","SEO"],
    "c_id": [401,401,402,402,403,403,406,406]
}

df6 = pd.DataFrame(student)

print(df6)

