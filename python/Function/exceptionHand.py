# # Exception hendling


# try :
#     a = int(input("enter a number : "))
#     c = 10/a
#     print(c)

# except ZeroDivisionError:
#     print("value should be greater then zero")

# except ValueError:
#     print("value should be an integer ")

# except :
#     print("Exception found")



# +++++++++++++++++++++++++++++++++++++.  raise .   ++++++++++++++++++++++

# a = 5
# if(a<0):
#     raise Exception("invalid value ......")
# else:
#     print(a)

# try:
#     aa = "ten"
#     if type(aa) is not int:
#         raise TypeError("value should be an integer......")
#     else:
#         print(aa)
# except Exception as e:
#     print(e)



# try: 
#     per = int(input("enter any percentage : "))
#     if(per<0):
#         raise Exception("Percentage should be >= 0 .....")
#     elif per > 100:
#         raise Exception("Percentage should be <= 100 .....")
#     else: 
#         print(per)
# except Exception as e:
#     print(e)


# +++++++++++++++++++++++++++++++++++++.  Assignment.   ++++++++++++++++++++++

# Write a Python program that:
# Has a fixed balance = 10000
# Asks the user to enter withdrawal amount.
# Handles the following cases using exception handling:
# Conditions:
# If user enters text → show: "Please enter a valid number"
# If user enters negative number → show: "Amount cannot be negative"
# If withdrawal amount > balance → show: "Insufficient balance"
# If everything is correct →
# Deduct amount
# Print remaining balance
# Use:
# try
# except
# else
# finally
# and at least one raise




try:
    print("Welcome to ATM\n")

    account = 10000
    n = int(input("Enter withdrawal amount: "))

    if n < 0:
        raise Exception("Amount cannot be negative")

    if n > account:
        raise Exception("Insufficient balance")

    # If everything correct
    account -= n
    print("You have withdrawn", n)
    print("Remaining balance:", account)

except ValueError:
    print("Please enter a valid number")

except Exception as e:
    print(e)

finally:
    print("Thank you for visiting our ATM")


