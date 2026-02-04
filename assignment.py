rec = []
persent=0
n = int(input("how many students you want to add : "))
i = 1
k=1

while i <=n:
    print("input", i , "record")
    roll_no = int(input("Enter roll no : "))
    name = input("Enter name : ")
    physics = int(input("Enter physics mark : "))
    chemestry = int(input("Enter chemestry mark : "))
    maths = int(input("Enter maths mark : "))
    total_mark = physics+chemestry+maths
    persent = total_mark/3

    mr = [roll_no, name, physics, chemestry, maths, total_mark, persent]
    rec.append(mr)
    i+=1
# print(rec)

# Extended list with some failing marks for testing
rec1 = [
    [101, "Akhil", 56, 54, 76, 186, 62.0],
    [102, "Rohit", 65, 60, 70, 195, 65.0],
    [103, "Ankit", 72, 68, 75, 215, 71.67],
    [104, "Neha", 80, 78, 82, 240, 80.0],
    [105, "Pooja", 60, 62, 64, 186, 44.0],
    [106, "Aman", 55, 58, 60, 173, 57.67],
    [107, "Riya", 85, 88, 90, 263, 87.67],
    [108, "Kunal", 70, 65, 68, 203, 67.67],
    [109, "Suman", 66, 64, 69, 199, 66.33],
    [110, "Vikas", 75, 72, 78, 225, 75.0],
    [111, "Nitin", 58, 55, 60, 173, 57.67],
    [112, "Sneha", 82, 80, 85, 247, 82.33],
    [113, "Rahul", 68, 70, 72, 210, 70.0],
    [114, "Kavita", 74, 76, 78, 228, 76.0],
    [115, "Deepak", 62, 60, 65, 187, 62.33],
    [116, "Pankaj", 69, 67, 71, 207, 69.0],
    [117, "Meena", 88, 90, 92, 270, 90.0],
    [118, "Suresh", 54, 56, 58, 168, 56.0],
    [119, "Priya", 77, 75, 80, 232, 77.33],
    [120, "Manoj", 4, 6, 8, 18, 10.0],
    # Adding for failing students (Passing mark < 40)
    [121, "Fail_All", 32, 15, 10, 45, 15.0],
    [122, "Fail_One", 39, 60, 15, 165, 55.0],
    [123, "Fail_Two", 30, 25, 80, 135, 45.0]
]

print("Enter 1 for all list")
print("Enter 2 for even list")
print("Enter 3 for odd list")
print("Enter 4 to search student detail by roll no.")
print("Enter 5 for all pass student list")
print("Enter 6 for all fail studentlist")
print("Enter 7 for all first division student list")
print("Enter 8 for all second division student list")
print("Enter 9 for all third division student list")
print("Enter 10 for who are fail in all subject")
print("Enter 11 for who are fail in 1 subject")
print("Enter 12 for who are fail in 2 subject")

choice = int(input("Enter a number : " ))
print("\t"f"{'Roll':<6} {'Name':<12} {'Physics':<12} {'Chemistry':<12} {'Maths':<12} {'Total Mark':<12} {'Persentage':<12}")


for x in rec: 

#  for all list 
    if(choice == 1):
        print("\t"f"{x[0]:<6} {x[1]:<12} {x[2]:<12} {x[3]:<12} {x[4]:<12} {x[5]:<12} {x[6]:<12}")

#  for evevn 
    if(x[0]%2 == 0 and choice == 2):
        print("\t"f"{x[0]:<6} {x[1]:<12} {x[2]:<12} {x[3]:<12} {x[4]:<12} {x[5]:<12} {x[6]:<12}")


#  for odd 

    elif(x[0]%2 == 1 and choice == 3):
        print("\t"f"{x[0]:<6} {x[1]:<12} {x[2]:<12} {x[3]:<12} {x[4]:<12} {x[5]:<12} {x[6]:<12}")



# # for ? roll number
    elif(choice == 4):
            roll_num = int(input("enter roll number : "))
            for y in rec:
                if(y[0]== roll_num):
                    print("\t",y[0],"\t",y[1],"\t" ,y[2],"\t \t",y[3],"\t  \t",y[4], "\t",y[5], "\t\t ",y[6])



#  who are pass ?
    elif(x[2] >= 34 and x[3]>= 34 and x[4]>= 34 and x[6]>= 34  and choice == 5):
        print("\t"f"{x[0]:<6} {x[1]:<12} {x[2]:<12} {x[3]:<12} {x[4]:<12} {x[5]:<12} {x[6]:<12}")


#  who are fail ?
    elif(x[6]<= 34 and x[2] <= 34 and x[3]<= 34 and x[4]<= 34 and choice == 6):
        print("\t"f"{x[0]:<6} {x[1]:<12} {x[2]:<12} {x[3]:<12} {x[4]:<12} {x[5]:<12} {x[6]:<12}")


#  who are first division ?
    elif(x[6] >=60 and x[6]<=100 and choice == 7):
        print("\t"f"{x[0]:<6} {x[1]:<12} {x[2]:<12} {x[3]:<12} {x[4]:<12} {x[5]:<12} {x[6]:<12}")

#  who are second division ?
    elif(x[6] >= 45 and x[6]<=59 and choice == 8):
         print("\t"f"{x[0]:<6} {x[1]:<12} {x[2]:<12} {x[3]:<12} {x[4]:<12} {x[5]:<12} {x[6]:<12}")

 #  who are third division ?
    elif(x[6] >= 33 and x[6]<=44 and choice == 9):
        print("\t"f"{x[0]:<6} {x[1]:<12} {x[2]:<12} {x[3]:<12} {x[4]:<12} {x[5]:<12} {x[6]:<12}")

 #  who are fail in all subject ?
    elif(x[2]<=33 and x[3]<=33 and x[4]<=33 and choice == 10):
        print("\t"f"{x[0]:<6} {x[1]:<12} {x[2]:<12} {x[3]:<12} {x[4]:<12} {x[5]:<12} {x[6]:<12}")

#  who are fail in one subject ?
    elif(x[2]<=33 and x[3]>=33 and x[4]>=33 or
         x[3]<=33 and x[4]>=33 and x[2]>=33 or 
         x[4]<=33 and x[2]>=33 and x[3]>=33 and choice == 11):
        print("\t"f"{x[0]:<6} {x[1]:<12} {x[2]:<12} {x[3]:<12} {x[4]:<12} {x[5]:<12} {x[6]:<12}")

#  who are fail in two subject ?
    elif(choice == 12 and x[2]<=33 and x[3]<=33 and x[4]>=33 or
         x[3]<=33 and x[4]<=33 and x[2]>=33 or 
         x[4]<=33 and x[2]<=33 and x[3]>=33 ):
        print("\t"f"{x[0]:<6} {x[1]:<12} {x[2]:<12} {x[3]:<12} {x[4]:<12} {x[5]:<12} {x[6]:<12}")
            
            
    
