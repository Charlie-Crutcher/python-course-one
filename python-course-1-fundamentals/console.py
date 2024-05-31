def main_screen():
    print("====================")
    print("Python Progress")
    print("1. 'Hello World'")
    print("2. 'Control Flow'")

    user_choice=input("Select an Option")
    if user_choice == "1":
        module_1()
    elif user_choice == "2":
        module_2()
    else:
        print("Please select a valid choice!")
        main_screen()


def module_1():
    print("====================")


def module_2():
    print("====================")


main_screen()