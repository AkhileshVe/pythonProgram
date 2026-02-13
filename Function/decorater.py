def display():

    def show():
        print("This is inner function")

    print("this is outer function")
    return show

ob = display()
ob()


add = lambda x,y : x+y
ob = lambda x,y : x if x > y else y