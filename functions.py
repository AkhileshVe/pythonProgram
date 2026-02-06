def display():
    print("hello display")

# display()


def addition(a,b,c):
    add = a + b
    print(add)
    c()
    

addition(4,5, display)