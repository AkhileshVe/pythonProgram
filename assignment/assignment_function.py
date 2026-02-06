def title():
    print("\t" f"----------------------------------------------------------------------------------------------------------------------------------")
    print("\t" f"{"❗️":<4} {'Roll no':<10} {"❗️":<4} {'Name':<10} {"❗️":<4} {'Physics':<10} {"❗️":<4} {'Chemestry':<10} {"❗️":<4} {'Maths':<10} {"❗️":<4} {'Total Mark':<10} {"❗️":<4} {'Percentage':<10} {"❗️":<4} {'Pass/Fail':<10} {"❗️":<4}")
    print("\t" f"----------------------------------------------------------------------------------------------------------------------------------")

def choice_fun(x):
    print("\t" f"{"|":<4} {x[0]:<10} {"|":<4} {x[1]:<10} {"|":<4} {x[2]:<10} {"|":<4} {x[3]:<10} {"|":<4} {x[4]:<10} {"|":<4} {x[5]:<10} {"|":<4} {x[6]:<10} {"|":<4} {x[7]:<10} {"|":<4}")
    print("\t" f"----------------------------------------------------------------------------------------------------------------------------------")

def marksheet():
    k=1
    # i = 1
    # n = int(input("how many student record you want : "))
    loop = True
    # rec = []
    # while i <= n:
    #     roll = int(input("enter roll no. : "))
    #     name = input("enter Name : ")
    #     physics = int(input("enter physics mark : "))
    #     chemestry = int(input("enter chemestry mark : "))
    #     math = int(input("enter maths mark : "))
    #     total_mark = physics+chemestry+math
    #     persent = total_mark//3
    #     if(persent<=33):
    #        result =  "❌"
    #     else:
    #         result = "✅"
              

    #     mr = [roll, name, physics, chemestry, math, total_mark, persent, result]
    #     rec.append(mr)
    #     i+=1
    # print(rec)
    rec = [
    [101, "Akhil", 56, 54, 76, 186, 62.0 , "✅"],
    [102, "Rohit", 65, 60, 70, 195, 65.0,"✅"],
    [103, "Ankit", 72, 68, 75, 215, 71.67, "✅"],
    [104, "Neha", 80, 78, 82, 240, 80.0, "✅"],
    [105, "Pooja", 60, 62, 64, 186, 44.0, "✅"],
    [106, "Aman", 55, 58, 60, 173, 57.67, "✅"],
    [107, "Riya", 85, 88, 90, 263, 87.67, "✅"],
    [108, "Kunal", 70, 65, 68, 203, 67.67, "✅"],
    [109, "Suman", 66, 64, 69, 199, 66.33, "✅"],
    [110, "Vikas", 75, 72, 78, 225, 75.0, "✅"],
    [111, "Nitin", 58, 55, 60, 173, 57.67, "✅"],
    [112, "Sneha", 82, 80, 85, 247, 82.33, "✅"],
    [113, "Rahul", 68, 70, 72, 210, 70.0, "✅"],
    [114, "Kavita", 74, 76, 78, 228, 76.0, "✅"],
    [115, "Deepak", 62, 60, 65, 187, 62.33, "✅"],
    [116, "Pankaj", 69, 67, 71, 207, 69.0, "✅"],
    [117, "Meena", 88, 90, 92, 270, 90.0, "✅"],
    [118, "Suresh", 54, 56, 58, 168, 56.0, "✅"],
    [119, "Priya", 77, 75, 80, 232, 77.33, "✅"],
    [120, "Manoj", 4, 6, 8, 18, 10.0, "❌"],
    # Adding for failing students (Passing mark < 40)
    [121, "Fail_All", 32, 15, 10, 45, 15.0, "❌"],
    [122, "Fail_One", 39, 60, 15, 165, 55.0, "✅"],
    [123, "Fail_Two", 30, 25, 80, 135, 45.0, "❌"]
]
    
    heading= {1:"\t\t\t\t\t  \t""All list (1)",
            2:"\t\t\t\t\t  \t""Even list (2)",
            3:"\t\t\t\t \t \t""Odd list (3)",
            4:"\t\t\t\t \t""Search student detail by roll no. (4)",
            5:"\t\t\t\t\t\t""All pass student list (5)",
            6:"\t\t\t\t\t\t""All fail student list (6)",
            7:"\t\t\t\t\t""All first division student list (7)",
            8:"\t\t\t\t\t""All second division student list (8)",
            9:"\t\t\t\t\t\t""All third division student list (9)",
           10:"\t\t\t\t\t\t""Fail in all subject student list (10)",
           11:"\t\t\t\t \t  \t""Fail in one subject (11)",
           12:"\t\t\t\t\t\t""Fail in two subject student list (12)"}

        
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
        choice = int(input("Enter your choice : "))
        print()
        if(choice<12):
            print(heading[choice])
        print("\t" f"----------------------------------------------------------------------------------------------------------------------------------")
        print("\t" f"{"❗️":<4} {'Roll no':<10} {"❗️":<4} {'Name':<10} {"❗️":<4} {'Physics':<10} {"❗️":<4} {'Chemestry':<10} {"❗️":<4} {'Maths':<10} {"❗️":<4} {'Total Mark':<10} {"❗️":<4} {'Percentage':<10} {"❗️":<4} {'Pass/Fail':<10} {"❗️":<4}")
        print("\t" f"----------------------------------------------------------------------------------------------------------------------------------")
        for x in rec:
    
            if choice == 1:
                choice_fun(x)
    
            elif (x[0]%2 == 0 and choice == 2):
                choice_fun(x)

            elif (x[0]%2-1 == 0 and choice == 3):
                choice_fun(x)

            elif choice == 4:

                print()
                roll_num = int(input("enter roll number : ")) if k == 1 else "Fail"
                title()
                for x in rec:
                    if(x[0]== roll_num):
                        choice_fun(x)
                        k = 0
                break

            elif (x[2] >= 34 and x[3]>= 34 and x[4]>= 34 and x[6]>= 34 and choice == 5):
                choice_fun(x)

            elif (x[6]<= 34 and x[2] <= 34 and x[3]<= 34 and x[4]<= 34 and choice == 6):
                choice_fun(x)

            elif (x[6] >=60 and x[6]<=100 and choice == 7):
                choice_fun(x)

            elif(x[6] >= 45 and x[6]<=59 and choice == 8):
                choice_fun(x)

            elif(x[6] >= 33 and x[6]<=44 and choice == 9):
                choice_fun(x)

            elif(x[2]<=33 and x[3]<=33 and x[4]<=33 and choice == 10):
                choice_fun(x)

            elif(x[2]<=33 and x[3]>=33 and x[4]>=33 or
               x[3]<=33 and x[4]>=33 and x[2]>=33 or 
               x[4]<=33 and x[2]>=33 and x[3]>=33 and choice == 11):
                choice_fun(x)

            elif(x[2]<=33 and x[3]<=33 and x[4]>=33 or
               x[3]<=33 and x[4]<=33 and x[2]>=33 or 
               x[4]<=33 and x[2]<=33 and x[3]>=33 and choice == 12):
                choice_fun(x)
                
            elif choice == 13:
                loop=False
            
            elif(choice >= 14):
                print("\t\t\t\t   \t""invalid input please try again 💁🏼💁🏼")

print("\t\t\t\t   \t""App bahar aa chuke hai 💁🏼💁🏼")
    
marksheet()

