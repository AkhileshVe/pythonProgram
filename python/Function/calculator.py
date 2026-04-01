def message(mess):
    print("\t","----------------------------------------------------")
    print("\t", "\t",        mess)
    print("\t","----------------------------------------------------")


def calculator():
    message("Welcome to calculator")
    num1 = int(input("Enter first number : "))
    num2 = int(input("Enter second number : "))

    loop = True


    while loop:
        print("Press 'A' for addition")
        print("Press 'S' for substraction")
        print("Press 'D' for division")
        print("Press 'M' for multiplication")
        print("Press 'X' for exit")

        choise = input("Enter anyone of them : ")

        if(choise == "A"):
            print("\t","----------------------------------------------------")
            r = num1 + num2
            print("\t", "\t"    ,"Your addition of", num1, "+",num2, "=", r)
            print("\t","----------------------------------------------------")
        
        elif(choise == "S"):
            print("\t","----------------------------------------------------")
            r = num1 - num2
            print("\t", "\t"    ,"Your substraction of", num1, "-",num2, "=", r)
            print("\t","----------------------------------------------------")

        elif(choise == "M"):
            print("\t","----------------------------------------------------")
            r = num1 * num2
            print("\t", "\t"    ,"Your multiplication of", num1, "*",num2, "=", r)
            print("\t","----------------------------------------------------")

        elif(choise == "D"):
            r = num1 / num2
            print("\t","----------------------------------------------------")
            print("\t", "\t"    ,"\t", "\t","Your division of", num1, "/",num2, "=", r)
            print("\t","----------------------------------------------------")

        elif(choise == "X","E","x"):
            loop = False

    message("App calculator se bahar aa gaye")

calculator()


# def calculate(n1, n2, op):
#     if op == "A":
#         return n1 + n2
#     elif op == "S":
#         return n1 - n2
#     elif op == "M":
#         return n1 * n2
#     elif op == "D":
#         if n2 != 0:
#             return n1 / n2
#         else:
#             return "Division by zero not allowed"


# number = 123
# leng = len(str(abs(number)))
# i=1
# n =number
# while i < leng:
#     x = n%10