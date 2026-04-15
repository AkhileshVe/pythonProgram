# merge two data frame 

import pandas as pd

course = {
    "course_id" : [401,402,403,405],
    "course_name" : ["BCA","BBA","BA","MCA"],
    "course_fee" : [40000,45200,25000,78000],
    "course_duration" : ["3years","3years","3years","3years"],
}


student = {
    "student_id": [1,2,3,4,5,6,7,8],
    "student_name": ["raj","ravi","riya","rahul","ritesh","jiya","tiya","priya"],
    "age":[26,27,28,26,27,26,27,28],
    "city": ["ind","bpl","jab","sat","ujj","Dev","KTE","SEO"],
    "c_id": [401,401,402,402,403,403,406,406]
}

c_df = pd.DataFrame(course)
s_df = pd.DataFrame(student)

# print("*****************************************************************")
# print(c_df)
# print("*****************************************************************")
# print(s_df)

student_course_inner = pd.merge(s_df,c_df, how='inner', left_on='c_id', right_on='course_id')
student_course_left = pd.merge(s_df,c_df, how='left', left_on='c_id', right_on='course_id')
student_course_right = pd.merge(s_df,c_df, how='right', left_on='c_id', right_on='course_id')
student_course_outer = pd.merge(s_df,c_df, how='outer', left_on='c_id', right_on='course_id')
student_course_cross = pd.merge(s_df,c_df, how='cross')
print()
print("***************************.  student_course inner. join **************************************")
print()
print(student_course_inner)

#    student_id student_name  age city  c_id  course_id course_name  course_fee course_duration
# 0           1          raj   26  ind   401        401         BCA       40000          3years
# 1           2         ravi   27  bpl   401        401         BCA       40000          3years
# 2           3         riya   28  jab   402        402         BBA       45200          3years
# 3           4        rahul   26  sat   402        402         BBA       45200          3years
# 4           5       ritesh   27  ujj   403        403          BA       25000          3years
# 5           6         jiya   26  Dev   403        403          BA       25000          3years
# 6           7         tiya   27  KTE   404        404        BCOM       23000          3years
# 7           8        priya   28  SEO   404        404        BCOM       23000          3years



print()
print("***************************.  student_course left. join **************************************")
print()
print(student_course_left)


#    student_id student_name  age city  c_id  course_id course_name  course_fee course_duration
# 0           1          raj   26  ind   401        401         BCA       40000          3years
# 1           2         ravi   27  bpl   401        401         BCA       40000          3years
# 2           3         riya   28  jab   402        402         BBA       45200          3years
# 3           4        rahul   26  sat   402        402         BBA       45200          3years
# 4           5       ritesh   27  ujj   403        403          BA       25000          3years
# 5           6         jiya   26  Dev   403        403          BA       25000          3years
# 6           7         tiya   27  KTE   404        404        BCOM       23000          3years
# 7           8        priya   28  SEO   404        404        BCOM       23000          3years

print()
print("***************************.  student_course right. join **************************************")
print()
print(student_course_right)

#    student_id student_name   age city   c_id  course_id course_name  course_fee course_duration
# 0         1.0          raj  26.0  ind  401.0        401         BCA       40000          3years
# 1         2.0         ravi  27.0  bpl  401.0        401         BCA       40000          3years
# 2         3.0         riya  28.0  jab  402.0        402         BBA       45200          3years
# 3         4.0        rahul  26.0  sat  402.0        402         BBA       45200          3years
# 4         5.0       ritesh  27.0  ujj  403.0        403          BA       25000          3years
# 5         6.0         jiya  26.0  Dev  403.0        403          BA       25000          3years
# 6         7.0         tiya  27.0  KTE  404.0        404        BCOM       23000          3years
# 7         8.0        priya  28.0  SEO  404.0        404        BCOM       23000          3years
# 8         NaN          NaN   NaN  NaN    NaN        405         MCA       78000          3years



print()
print("***************************.  student_course outer. join **************************************")
print()
print(student_course_outer)

#    student_id student_name   age city   c_id  course_id course_name  course_fee course_duration
# 0         1.0          raj  26.0  ind  401.0        401         BCA       40000          3years
# 1         2.0         ravi  27.0  bpl  401.0        401         BCA       40000          3years
# 2         3.0         riya  28.0  jab  402.0        402         BBA       45200          3years
# 3         4.0        rahul  26.0  sat  402.0        402         BBA       45200          3years
# 4         5.0       ritesh  27.0  ujj  403.0        403          BA       25000          3years
# 5         6.0         jiya  26.0  Dev  403.0        403          BA       25000          3years
# 6         7.0         tiya  27.0  KTE  404.0        404        BCOM       23000          3years
# 7         8.0        priya  28.0  SEO  404.0        404        BCOM       23000          3years
# 8         NaN          NaN   NaN  NaN    NaN        405         MCA       78000          3years


print()
print("***************************.  student_course cross. join **************************************")
print()
print(student_course_cross)

#     student_id student_name  age city  c_id  course_id course_name  course_fee course_duration
# 0            1          raj   26  ind   401        401         BCA       40000          3years
# 1            1          raj   26  ind   401        402         BBA       45200          3years
# 2            1          raj   26  ind   401        403          BA       25000          3years
# 3            1          raj   26  ind   401        405         MCA       78000          3years
# 4            2         ravi   27  bpl   401        401         BCA       40000          3years
# 5            2         ravi   27  bpl   401        402         BBA       45200          3years
# 6            2         ravi   27  bpl   401        403          BA       25000          3years
# 7            2         ravi   27  bpl   401        405         MCA       78000          3years
# 8            3         riya   28  jab   402        401         BCA       40000          3years
# 9            3         riya   28  jab   402        402         BBA       45200          3years
# 10           3         riya   28  jab   402        403          BA       25000          3years
# 11           3         riya   28  jab   402        405         MCA       78000          3years
# 12           4        rahul   26  sat   402        401         BCA       40000          3years
# 13           4        rahul   26  sat   402        402         BBA       45200          3years
# 14           4        rahul   26  sat   402        403          BA       25000          3years
# 15           4        rahul   26  sat   402        405         MCA       78000          3years
# 16           5       ritesh   27  ujj   403        401         BCA       40000          3years
# 17           5       ritesh   27  ujj   403        402         BBA       45200          3years
# 18           5       ritesh   27  ujj   403        403          BA       25000          3years
# 19           5       ritesh   27  ujj   403        405         MCA       78000          3years
# 20           6         jiya   26  Dev   403        401         BCA       40000          3years
# 21           6         jiya   26  Dev   403        402         BBA       45200          3years
# 22           6         jiya   26  Dev   403        403          BA       25000          3years
# 23           6         jiya   26  Dev   403        405         MCA       78000          3years
# 24           7         tiya   27  KTE   406        401         BCA       40000          3years
# 25           7         tiya   27  KTE   406        402         BBA       45200          3years
# 26           7         tiya   27  KTE   406        403          BA       25000          3years
# 27           7         tiya   27  KTE   406        405         MCA       78000          3years
# 28           8        priya   28  SEO   406        401         BCA       40000          3years
# 29           8        priya   28  SEO   406        402         BBA       45200          3years
# 30           8        priya   28  SEO   406        403          BA       25000          3years
# 31           8        priya   28  SEO   406        405         MCA       78000          3years
