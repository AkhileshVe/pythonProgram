# file conversion (if we have data then in how many type to store data)

import pandas as pd
from sqlalchemy import create_engine


student={
    "rno":[101,102, 103,104,105],
    "name":["raj", "ravi", "rahul", "ritesh", "nimesh" ],
    "age":[26,27,None,26,27],
    "gender":["male","male","female","male","male"],
    "city": ["ind","bpl","jab","sat","ujjain"],
    "fee":[30000,35000,40000,None,None]
}


# df = pd.DataFrame(student)

# df.to_csv("student.csv", index=False) # file convert in csv
# df.to_excel("student.xlsx", index=False) # file convert in excel
# df.to_html("student.html", index=False) # file convert in html
# df.to_json("student.json") # file convert in json



# to connect with sql we need these library installation

#  pip install sqlalchemy
#  pip install mysql-connector-python
#  pip install pymysql





engine = create_engine("mysql+pymysql://root:Vermaji123@localhost:3306/pd_database")

# df = pd.read_sql("SELECT * FROM employee", engine)
# print(df)

df = pd.DataFrame(student)
df.to_sql('student', if_exists='replace', con=engine)



# student={
#     "rno":[101,102, 103,104,105],
#     "name":["raj", "ravi", "rahul", "ritesh", "nimesh" ],
#     "age":[26,27,None,26,27],
#     "gender":["male","male","female","male","male"],
#     "city": ["ind","bpl","jab","sat","ujjain"],
#     "fee":[30000,35000,40000,None,None]
# }
