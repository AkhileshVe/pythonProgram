import pandas as pd

df = pd.read_csv("employee.csv")
# print(df.head(0))

new_df = df[['emp_id', 'name', 'salary']]
print(new_df)

new_df["department"]= ["HR","IT","SALES","IT","HR","IT","SALES","IT","HR","IT" ]

new_df["ta"]= new_df["salary"]*0.15
new_df["da"]= new_df["salary"]*0.20

new_df["gross_salary"]= new_df["salary"]+new_df['ta']+new_df['da']


new_df.to_csv("new_emp.csv", index=False)

new_df["tex"]= new_df["gross_salary"]* 0.05
new_df["tex_sal"]= new_df["gross_salary"]-new_df["gross_salary"]* 0.05
print(new_df)

tex_total= new_df["tex"].sum()
da_total= new_df['da'].sum()
ta_total= new_df['ta'].sum()
salary_total= new_df["salary"].sum()

print("tex_total.  : ",tex_total)
print("da_total.  : ",da_total)
print("ta_total.  : ",ta_total)
print("salary_total.  : ",salary_total)



