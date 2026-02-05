rec = {}
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
    persent = total_mark//3
    mr = [ name, physics, chemestry, maths, total_mark, persent]
    # rec.append(mr)
    rec[roll_no]=mr
    # rec.update(mr)
    i+=1
# print(rec)

# Extended list with some failing marks for testing
# rec = {
#     101: ["Akhil", 56, 54, 76, 186, 62.0],
#     102: ["Rohit", 65, 60, 70, 195, 65.0],
#     103: ["Ankit", 72, 68, 75, 215, 71.67],
#     104: ["Neha", 80, 78, 82, 240, 80.0],
#     105: ["Pooja", 60, 62, 64, 186, 44.0],
#     106: ["Aman", 55, 58, 60, 173, 57.67],
#     107: ["Riya", 85, 88, 90, 263, 87.67],
#     108: ["Kunal", 70, 65, 68, 203, 67.67],
#     109: ["Suman", 66, 64, 69, 199, 66.33],
#     110: ["Vikas", 75, 72, 78, 225, 75.0],
#     111: ["Nitin", 58, 55, 60, 173, 57.67],
#     112: ["Sneha", 82, 80, 85, 247, 82.33],
#     113: ["Rahul", 68, 70, 72, 210, 70.0],
#     114: ["Kavita", 74, 76, 78, 228, 76.0],
#     115: ["Deepak", 62, 60, 65, 187, 62.33],
#     116: ["Pankaj", 69, 67, 71, 207, 69.0],
#     117: ["Meena", 88, 90, 92, 270, 90.0],
#     118: ["Suresh", 54, 56, 58, 168, 56.0],
#     119: ["Priya", 77, 75, 80, 232, 77.33],
#     120: ["Manoj", 4, 6, 8, 18, 10.0],
#     #  Adding for failing students (Passing mark < 40)
#     121: ["Fail_All", 32, 15, 10, 45, 15.0],
#     122: ["Fail_One", 39, 60, 15, 165, 55.0],
#     123: ["Fail_Two", 30, 25, 80, 135, 45.0]
# }


print(rec[101][1])
print("\t"f"{'Roll':<6} {'Name':<12} {'Physics':<12} {'Chemistry':<12} {'Maths':<12} {'Total Mark':<12} {'Persentage':<12}")
for x in rec:
    if(x%2 == 0):
        print("\t"f"{x:<6} {rec[x][0]:<12} {rec[x][1]:<12} {rec[x][2]:<12} {rec[x][3]:<12} {rec[x][4]:<12} {rec[x][5]:<12}")
        

loop = True
while loop:
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
#  for all list 
    if(choice == 1):
        print("\t\t\t\t   \t""All list (1)")
        print()
        print("\t"f"{'Roll':<6} {'Name':<12} {'Physics':<12} {'Chemistry':<12} {'Maths':<12} {'Total Mark':<12} {'Persentage':<12}")
        for x in rec: 
            print("\t"f"{x:<6} {rec[x][0]:<12} {rec[x][1]:<12} {rec[x][2]:<12} {rec[x][3]:<12} {rec[x][4]:<12} {rec[x][5]:<12}")
        print()

#  for evevn 
    elif( choice == 2):
        print("\t\t\t\t  \t""Even list (2)")
        print()
        print("\t"f"{'Roll':<6} {'Name':<12} {'Physics':<12} {'Chemistry':<12} {'Maths':<12} {'Total Mark':<12} {'Persentage':<12}")
        for x in rec: 
            if(x%2 == 0):
                print("\t"f"{x:<6} {rec[x][0]:<12} {rec[x][1]:<12} {rec[x][2]:<12} {rec[x][3]:<12} {rec[x][4]:<12} {rec[x][5]:<12}")
        print()


#  for odd 

    elif(choice == 3):
        print("\t\t\t\t    \t""Odd list (3)")
        print()
        print("\t"f"{'Roll':<6} {'Name':<12} {'Physics':<12} {'Chemistry':<12} {'Maths':<12} {'Total Mark':<12} {'Persentage':<12}")
        for x in rec:
            if(x%2 == 1): 
                print("\t"f"{x:<6} {rec[x][0]:<12} {rec[x][1]:<12} {rec[x][2]:<12} {rec[x][3]:<12} {rec[x][4]:<12} {rec[x][5]:<12}")
        print()


# # for ? roll number
    elif(choice == 4):
        print("\t\t\t\t ""Search student detail by roll no. (4)")
        print()
        roll_num = int(input("enter roll number : "))
        print("\t"f"{'Roll':<6} {'Name':<12} {'Physics':<12} {'Chemistry':<12} {'Maths':<12} {'Total Mark':<12} {'Persentage':<12}")
        for x in rec:
            if(x== roll_num):
                print("\t"f"{x:<6} {rec[x][0]:<12} {rec[x][1]:<12} {rec[x][2]:<12} {rec[x][3]:<12} {rec[x][4]:<12} {rec[x][5]:<12}")
        print()

#  who are pass ?
    elif(choice == 5):
        print("\t\t\t\t\t""All pass student list (5)")
        print()
        print("\t"f"{'Roll':<6} {'Name':<12} {'Physics':<12} {'Chemistry':<12} {'Maths':<12} {'Total Mark':<12} {'Persentage':<12}")
        for x in rec:
            if(rec[x][1] >= 34 and rec[x][2]>= 34 and rec[x][3]>= 34 and rec[x][5]>= 34): 
                print("\t"f"{x:<6} {rec[x][0]:<12} {rec[x][1]:<12} {rec[x][2]:<12} {rec[x][3]:<12} {rec[x][4]:<12} {rec[x][5]:<12}")
        print()


#  who are fail ?
    elif( choice == 6):
        print("\t\t\t\t\t""All fail student list (6)")
        print()
        for x in rec:
             if(rec[x][1] <= 34 and rec[x][2]<= 34 and rec[x][3]<= 34 and rec[x][5]<= 34): 
                 print("\t"f"{x:<6} {rec[x][0]:<12} {rec[x][1]:<12} {rec[x][2]:<12} {rec[x][3]:<12} {rec[x][4]:<12} {rec[x][5]:<12}")
        print()
               

#  who are first division ?
    elif(choice == 7):
        print("\t\t\t\t""All first division student list (7)")
        print()
        for x in rec: 
            if(rec[x][5] >=60 and rec[x][5]<=100):
                print("\t"f"{x:<6} {rec[x][0]:<12} {rec[x][1]:<12} {rec[x][2]:<12} {rec[x][3]:<12} {rec[x][4]:<12} {rec[x][5]:<12}")
        print()
                
#  who are second division ?
    elif(choice == 8):
        print("\t\t\t\t""All second division student list (8)")
        print()
        for x in rec: 
            if(rec[x][5] >= 45 and rec[x][5]<=59):
                print("\t"f"{x:<6} {rec[x][0]:<12} {rec[x][1]:<12} {rec[x][2]:<12} {rec[x][3]:<12} {rec[x][4]:<12} {rec[x][5]:<12}")
        print()

 #  who are third division ?
    elif(choice == 9):
        print("\t\t\t\t\t""All third division student list (9)")
        print()
        for x in rec: 
            if(rec[x][5] >= 33 and rec[x][5]<=44):
                print("\t"f"{x:<6} {rec[x][0]:<12} {rec[x][1]:<12} {rec[x][2]:<12} {rec[x][3]:<12} {rec[x][4]:<12} {rec[x][5]:<12}")
        print()

 #  who are fail in all subject ?
    elif(choice == 10):
        print("\t\t\t\t\t""Fail in all subject student list (10)")
        print()
        for x in rec: 
            if(rec[x][1]<=33 and rec[x][2]<=33 and rec[x][3]<=33):
                print("\t"f"{x:<6} {rec[x][0]:<12} {rec[x][1]:<12} {rec[x][2]:<12} {rec[x][3]:<12} {rec[x][4]:<12} {rec[x][5]:<12}")
        print()

#  who are fail in one subject ?
    elif(choice == 11):
        print("\t\t\t\t   \t""Fail in one subject (11)")
        print()
        for x in rec: 
            if(rec[x][2-1]<=33 and rec[x][3-1]>=33 and rec[x][4-1]>=33 or
               rec[x][3-1]<=33 and rec[x][4-1]>=33 and rec[x][2-1]>=33 or 
               rec[x][4-1]<=33 and rec[x][2-1]>=33 and rec[x][3-1]>=33 ):
                print("\t"f"{x:<6} {rec[x][0]:<12} {rec[x][1]:<12} {rec[x][2]:<12} {rec[x][3]:<12} {rec[x][4]:<12} {rec[x][5]:<12}")
        print()

#  who are fail in two subject ?
    elif(choice == 12):
        print("\t\t\t\t\t""Fail in two subject student list (12)")
        print()
        for x in rec: 
            if(rec[x][2-1]<=33 and rec[x][3-1]<=33 and rec[x][4-1]>=33 or
               rec[x][3-1]<=33 and rec[x][4-1]<=33 and rec[x][2-1]>=33 or 
               rec[x][4-1]<=33 and rec[x][2-1]<=33 and rec[x][3-1]>=33):
                print("\t"f"{x:<6} {rec[x][0]:<12} {rec[x][1]:<12} {rec[x][2]:<12} {rec[x][3]:<12} {rec[x][4]:<12} {rec[x][5]:<12}")
        print()

    elif(choice == 13):
        loop = False

    elif(choice >= 14):
        print("\t\t\t\t   \t""invalid input please try again 💁🏼💁🏼")
            

print("\t\t\t\t   \t""App bahar aa chuke hai 💁🏼💁🏼")
            
