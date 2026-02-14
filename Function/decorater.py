def display():

    def show():
        print("This is inner function")

    print("this is outer function")
    return show

ob = display()
ob()

