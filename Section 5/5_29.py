password = ""
realPassword = "python123"
while password!= realPassword:
    password = raw_input("Enter password: ")
    if password == realPassword:
        print("You are logged in")
    else:
        print("Sorry, try again :(")