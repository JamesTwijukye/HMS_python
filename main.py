
from getpass import getpass
from colored import fg


#important variables
normal_color =fg('white')
error_color = fg('red')
success_color = fg('green')
info_color = fg('yellow')

error_code = False

patient_data = {}


while error_code != True:
    
    print(info_color + "====================================\n WELCOME TO HMS PLEASE REGISTER HERE \n ====================================")


    try:
        patient_username = input(normal_color + "enter your username :\n")
        patient_firstname = input(normal_color + "enter your firstname :\n")
        patient_lastname = input(normal_color + "enter your lastname :\n")
        patient_age = int(input(normal_color + "enter your age :\n"))
        patient_address = input(normal_color + "enter your address:\n")
        patient_password = getpass(normal_color + "enter your password :\n")
        confirm_password = getpass(normal_color + "confirm your password : \n")


    


        while confirm_password!=patient_password:
            print(error_color + "passwords do not match")

            patient_password = getpass("enter your password :\n")
            confirm_password = getpass("confirm your password : \n")
        else:

            patient_data = {

                'username': patient_username,
                'firstname': patient_firstname,
                'lastname': patient_lastname,
                'age': patient_age,
                'address': patient_address,
                'password': patient_password,

            }

        print(success_color + 'registered successfully')
        error_code = True

    except:
        print(error_color+'invalid data format,please enter correct data format')

