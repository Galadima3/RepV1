Data = {"John": 5045, "Jones": 5001}
print("Welcome to Student Info System:")
print('Press 1 to Login | Press 2 to Register')

Input = int(input('Enter your choice >>> '))


class System:

    if (Input == 1):
        Username = input('Enter your username:')

        def Login(username):

            if username in Data.keys():
                password = int(input('Enter your Password:'))
                if (username, password) in Data.items():
                    print("Login Successful!")
                else:
                    print("Password is incorrect!")

            else:
                print('user not found! Kindly register')

                exit()

        Login(Username)

    elif (Input == 2):
        def Register():
            Username = input('Enter your preferred username... ')
            if Username in Data.keys():
                print('Sorry this username has been picked')
                exit()

            Password = int(input('Enter your password'))

            Data[Username] = Password

            print('Welcome! Registration Successful')
        
        Register()


print(Data)
