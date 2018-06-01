def console():
    while True:
        ## Show menu ##
        print(30 * '-')
        print(" Commandline App")
        print(30 * '-')
        print("1. login")
        print("2. Create Account")
        print("3. logout")
        print("4. create comment")
        print("5. Edit comment")
        print("6 Delete Comment")
        print(30 * '-')

        ## Get input ###
        choice = input('Enter your choice [1-5] : ')

        ### Convert string to int type ##
        choice = int(choice)

        ### Take action as per selected menu-option ###
        if choice == 1:
            # function
            print('function')
        elif choice == 2:
            print('function')
        elif choice == 3:
            print('function')
        elif choice == 9:
            break
        else:
            print('function')


console()
