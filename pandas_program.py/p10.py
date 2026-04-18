import pandas as pd

print()
print()
print("*************************************************.      **************************************************")
print()
print()

students = {
    "student_id": [1,1,3,4,5,6,7,8],
    "student_name": ["raj","raj","riya","rahul","ritesh","jiya","tiya","priya"],
    "age":[26,26,28,26,27,26,27,28],
    "city": ["ind","bpl","jab","sat","ujj","Dev","KTE","SEO"],
    "course": ['BCA','BBA','BSC','MCA','BBA','BCA','MCA','BSC'],
    "fee":[26000,26000,28000,26000,27000,26000,27000,28000],
}

df = pd.DataFrame(students)

print(df)

print("sum  : ", df['fee'].sum())
print("max  : ", df['fee'].max())
print("min  : ", df['fee'].min())
print("mean : ", df['fee'].mean())
print("std  : ", df['fee'].std())
print("var  : ", df['fee'].var())

print()
print()
print("*************************************************.   group by course fee calculation  **************************************************")
print()
print()

print("sum  : ", df.groupby('course')['fee'].sum())
print("max  : ", df.groupby('course')['fee'].max())
print("min  : ", df.groupby('course')['fee'].min())
print("mean : ", df.groupby('course')['fee'].mean())
print("std  : ", df.groupby('course')['fee'].std())
print("var  : ", df.groupby('course')['fee'].var())

print()
print()
print("*************************************************.   group by city fee calculation  **************************************************")
print()
print()

print("sum  : ", df.groupby('city')['fee'].sum())
print("max  : ", df.groupby('city')['fee'].max())
print("min  : ", df.groupby('city')['fee'].min())
print("mean : ", df.groupby('city')['fee'].mean())
print("std  : ", df.groupby('city')['fee'].std())
print("var  : ", df.groupby('city')['fee'].var())



print(df.groupby('age')['fee'].agg(['sum','max','min','count','mean']))

print(df.groupby('age')['fee'])





print()
print()
print("*************************************************.   group by sampleSuperstore  **************************************************")
print()
print()

df2=pd.read_csv('sampleSuperstore.csv')
print(df2.head(0))
print(df2.groupby('Category')['Sales'].sum())
# df3=df2.dropna()
# print(df3)
