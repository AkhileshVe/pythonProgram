# Exception hendling


try :
    a = int(input("enter a number : "))
    c = 10/a
    print(c)

except ZeroDivisionError:
    print("value should be greater then zero")

except ValueError:
    print("value should be an integer ")

except :
    print("Exception found")

