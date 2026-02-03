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
print(rec)

rec=[[101, 'Akhil', 56, 54, 76, 186, 32.0],
     [104, 'Akhil', 65, 40, 76, 186, 62.0],
     [108, 'Akhil', 30, 54, 33, 186, 3.0]] 
print("\t Roll \t Name \t Physics \tChemistry \tMaths \t Total Mark  \t Persentage")


for x in rec:


#  for evevn 
    if(x[0]%2 == 1):
        print("\t",x[0],"\t",x[1],"\t" ,x[2],"\t \t",x[3],"\t  \t",x[4], "\t",x[5], "\t\t ",x[6])



#  for odd 
    if(x[0]%2 == 1):
        print("\t",x[0],"\t",x[1],"\t" ,x[2],"\t \t",x[3],"\t  \t",x[4], "\t",x[5], "\t\t ",x[6])
   


# for ? roll number
    roll_num = int(input("enter roll number"))
    for y in rec:
        if(y[0]== roll_num):
            print("\t",y[0],"\t",y[1],"\t" ,y[2],"\t \t",y[3],"\t  \t",y[4], "\t",y[5], "\t\t ",y[6])



#  who are pass ?

    if(x[6]> 34):
        print("\t",x[0],"\t",x[1],"\t" ,x[2],"\t \t",x[3],"\t  \t",x[4], "\t",x[5], "\t\t ",x[6])


#  who are fail ?

    if(x[6]< 34):
        print("\t",x[0],"\t",x[1],"\t" ,x[2],"\t \t",x[3],"\t  \t",x[4], "\t",x[5], "\t\t ",x[6])


#  who are first division ?
    if(x[6] >=60 and x[6]<=100):
        print("\t",x[0],"\t",x[1],"\t" ,x[2],"\t \t",x[3],"\t  \t",x[4], "\t",x[5], "\t\t ",x[6])

#  who are second division ?
    if(x[6] >= 45 and x[6]<=59):
         print("\t",x[0],"\t",x[1],"\t" ,x[2],"\t \t",x[3],"\t  \t",x[4], "\t",x[5], "\t\t ",x[6])

#  who are third division ?
    if(x[6] >= 33 and x[6]<=44):
        print("\t",x[0],"\t",x[1],"\t" ,x[2],"\t \t",x[3],"\t  \t",x[4], "\t",x[5], "\t\t ",x[6])
    
