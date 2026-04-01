
# rec = [
#     [101, "Akhil", 56, 54, 76, 186, 62.0 , "✅"],
#     [102, "Rohit", 65, 60, 70, 195, 65.0,"✅"],
#     [103, "Ankit", 72, 68, 75, 215, 71.67, "✅"],
#     [104, "Neha", 80, 78, 82, 240, 80.0, "✅"],
#     [105, "Pooja", 60, 62, 64, 186, 44.0, "✅"],
#     [106, "Aman", 55, 58, 60, 173, 57.67, "✅"],
#     [107, "Riya", 85, 88, 90, 263, 87.67, "✅"],
#     [108, "Kunal", 70, 65, 68, 203, 67.67, "✅"],
#     [109, "Suman", 66, 64, 69, 199, 66.33, "✅"],
#     [110, "Vikas", 75, 72, 78, 225, 75.0, "✅"],
#     [111, "Nitin", 58, 55, 60, 173, 57.67, "✅"],
#     [112, "Sneha", 82, 80, 85, 247, 82.33, "✅"],
#     [113, "Rahul", 68, 70, 72, 210, 70.0, "✅"],
#     [114, "Kavita", 74, 76, 78, 228, 76.0, "✅"],
#     [115, "Deepak", 62, 60, 65, 187, 62.33, "✅"],
#     [116, "Pankaj", 69, 67, 71, 207, 69.0, "✅"],
#     [117, "Meena", 88, 90, 92, 270, 90.0, "✅"],
#     [118, "Suresh", 54, 56, 58, 168, 56.0, "✅"],
#     [119, "Priya", 77, 75, 80, 232, 77.33, "✅"],
#     [120, "Manoj", 4, 6, 8, 18, 10.0, "❌"],
#     # Adding for failing students (Passing mark < 40)
#     [121, "Fail_All", 32, 15, 10, 45, 15.0, "❌"],
#     [122, "Fail_One", 39, 60, 15, 165, 55.0, "✅"],
#     [123, "Fail_Two", 30, 25, 80, 135, 45.0, "❌"]
# ]

# fobj1 = open("f1.text", "w")

# fobj1.write("\t" f"{"❗️":<4} {'Roll no':<10} {"❗️":<4} {'Name':<10} {"❗️":<4} {'Physics':<10} {"❗️":<4} {'Chemestry':<10} {"❗️":<4} {'Maths':<10} {"❗️":<4} {'Total Mark':<10} {"❗️":<4} {'Percentage':<10} {"❗️":<4} {'Pass/Fail':<10} {"❗️":<4} {"\n"}")

# for i in (rec):
#     fobj1.write("\t" f"{"|":<4} {i[0]:<10} {"|":<4} {i[1]:<10} {"|":<4} {i[2]:<10} {"|":<4} {i[3]:<10} {"|":<4} {i[4]:<10} {"|":<4} {i[5]:<10} {"|":<4} {i[6]:<10} {"|":<4} {i[7]:<10} {"|":<4}"+ "\n")
# fobj1.close()


fobjj = open("f1.text","r")
# data = fobjj.read()
data = fobjj.readable()
print(data)


# mode 
# w for write
# r for read
# a for append 

# w+ for write and read
# r+ for read and write
# a+ for append and read

fobj = open("f1.txt", "w")

fobj.write("Hello Student")
fobj.close()


# fobj2 = open("f2.txt", "w")

# n = int(input("Enter how many record you want : "))
# fobj2.write("\t  " + "name""\t")
# fobj2.write("\t  " + "mark"+ "\n")
# for i in (rec):
#     print("Enter", i, "record")
#     roll_no = int(input("Enter roll number :"))
#     name = input("Enter name :")
#     mark = int(input("Enter mark :"))
#     fobj2.write("\t""\t" + str(roll_no) + "\t")
#     fobj2.write("\t""\t" + name + "\t")
#     fobj2.write("\t""\t" + str(mark)+ "\t"+"\n")
# fobj2.close()

# print(fobj.name)     # File name
# print(fobj.mode)     # Mode (w)
# print(fobj.closed)   # False (file open hai)

# fobj.close()         # File close kar di

# print(fobj.closed)   # True