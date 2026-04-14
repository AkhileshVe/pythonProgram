import pandas as pd 

# student={
#          "rno":[101,102,103,104,105],
#          "name":["raj","ravi","riya","rahul","ritesh"],
#          "age":[25,26,None,28,29],
#          "gender":["male","male","female","male","male"],
#          "city":["ind","bpl","jbl","bpl","sta"],
#          "fee" :[20000,30000,40000,None,None]
#         }
# df=pd.DataFrame(student)
# print(df)
# for check the non value
# print(df.isna())

# for the data clean
# df1=df.dropna()
# print(df1)


# for fill the  non value
# df2=df.fillna(df["age"].mean())
# print(df2)


# student={
#          "rno":[101,102,103,104,105],
#          "name":["raj","ravi","riya","rahul","ritesh"],
#          "age":[25,26,None,28,29],
#          "gender":["male","male","female","male","male"],
#          "city":["ind","bpl","jbl","bpl","sta"],
#          "fee" :[20000,30000,40000,None,None]
#         }
# df=pd.DataFrame(student)
# df2=df.fillna({"age":df['age'].mean(),"fee":df["fee"].mean()})
# print(df2)

# df=pd.read_csv('samplesuperstore.csv')
# print(df.head(0))
# print(df)
# df2=df.dropna()
# print(df2)


# df=pd.read_csv('Electric_Vehicle_Population_Data.csv')
# print(df.head(0))
# print(df)
# df2=df.dropna()
# print(df2)

df=pd.read_excel('file2.xlsx')
print(df)
df2=df.fillna('data')
print(df2)