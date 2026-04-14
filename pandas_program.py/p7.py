import pandas as pd
from sqlalchemy import create_engine


# engine = create_engine("mysql+pymysql://root:Vermaji123@localhost:3306/pd_database")

# # query1 = "select * from student where city = 'bpl' "
# # query = "select * from student"
# # df = pd.read_sql(query1, con=engine)

# # print(df)


# df1 = pd.read_excel("student.xlsx")
# print(df1)

# # df2 = pd.read_html("student.html")
# # print(df2)

# df3 = pd.read_json("student.json")
# print(df3)


# # read file and convert
# df4 = pd.read_csv("student.csv")
# df4.to_json("new_std.json")





# read downloaded file


df4 = pd.read_csv("Datagov.csv")
print(df4)

print("********************************************************************************")

df5 = df4.dropna()
print(df5)
