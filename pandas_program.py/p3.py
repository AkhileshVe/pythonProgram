import pandas as pd
ind = [ "a","b","c","d","e"]

emp={
    "emp_id":[101,102, 103,104,105,106, 107, 108, 109, 110,],
    "name":["raj", "ravi", "rahul", "ritesh", "nimesh","rajveer","ravikant" ,"rahulsingh","ritu","sameer" ],
    "age":[26,27,28,26,27,26,27,28,26,27],
    "salary":[30000,35000,40000,45000,50000,30000,35000,40000,45000,50000]
}


df = pd.DataFrame(emp,index=ind)
df.to_csv("employee.csv", index=False)

# print(df)
# print("first_row. : ",df.iloc[0])
# print("first_row. : ",df.loc['a'])
# print("first_row. : ",df.iloc[0:2,[0,1,2]]) # [row,,[col]]

# sal = df["salary"]

# print("****************************** salary result ************************")

# print(sal)
# print("Total salary. : ",   sal.sum())
# print("max salary. : ",   sal.max())
# print("min salary. : ",   sal.min())
# print("avg salary. : ",   sal.mean())
# print("std salary. : ",   sal.std())
# print("var salary. : ",   sal.var())



# print("****************************** age result ************************")
# age = df["age"]
# print(age)

# print("max age. : ",   age.max())
# print("min age. : ",   age.min())
# print("avg age. : ",   age.mean())
# print("std age. : ",   age.std())
# print("var age. : ",   age.var())



# print("****************************** salary and age result ************************")
# salary_age = df["age", "salary"]


# print("max salary_age. : ",   salary_age.max())
# print("min salary_age. : ",   salary_age.min())
# print("avg salary_age. : ",   salary_age.mean())
# print("std salary_age. : ",   salary_age.std())
# print("var salary_age. : ",   salary_age.var())
