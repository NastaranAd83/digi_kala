
from os import system
from time import sleep
from bl.sign_up import SignUp
from bl.person import Person
from dal.textmanager import FilaManagering
from common.utility import Utility
from bl.user_pass import UserPass

while(True):

    print("MAIN MENU\n")

    print("1.sign up")
    print("2.sign in")
    print("3.exit")

    choice = input("\n your choice : ")

    if choice in ("1","up"):
                
                while(True):

                    system("cls")
                    errors = []
                    name = input("name :")

                    errors = Person.validation(name)

                    if not errors:
                        break
                    else:
                        for error in errors:
                            print(error)
                        sleep(2)

                while(True):

                    system("cls")
                    errors = []
                    family = input("family :")

                    errors = Person.validation(family)

                    if not errors:
                        break
                    else:
                        for error in errors:
                            print(error)
                        sleep(2)


                while(True):

                    system("cls")
                    errors = []
                    phone = input("Phone :")

                    errors = Person.validation(phone,True)
                    errors.append(Utility.sarching())

                    if not errors:
                        break
                    else:
                        for error in errors:
                            print(error)
                        sleep(2)

                while(True):

                    system("cls")
                    errors = []
                    username = input("username :")

                    errors , user = Utility.sarching("username",username)

                    if not errors:
                        break
                    else:
                        for error in errors :
                            print(error)
                        sleep(2)

                while(True):

                    system("cls")
                    errors = []
                    password = input("password :")

                    errors = UserPass.check_validation(password)

                    if not errors:
                        break
                    else:
                        for error in errors:
                            print(error)
                        sleep(2)

                    
                # data = {
                # "user": {"name": name, "family": family, "phone": phone,"username":username,"password":password},
                #     }
                
                # FilaManagering.save_data(data)


                sign_up = SignUp(name=name,family=family,
                phone=phone,username=username,password=password)
                

                sign_up.request_for_admin()


    if choice in ("2","in"):
         while(True):

            print("1.admin")
            print("2.user")
            print("3.exit\n")

            choice1 = input("your choice : ")

            if choice1 in ("1,a,A"):
                while(True):

                    print("1.add products")
                    print("2.list request")
                    print("3.exit\n")


                    choice4 = input("your choice : ")

                    if choice4 in ("1","a","A"):
                        pass


                    if choice4 in ("2","L","l"):

                        while(True):

                            system("cls")
                            errors = []
                            username = input("username :")

                            if username=="admin":
                                break
                            else:
                                print("invalid username for admin")
                                sleep(2)

                        while(True):

                            system("cls")
                            errors = []
                            password = input("password :")

                            if password == "140724N/a":
                                break

                            else:
                                print("invalid password for admin")
                                sleep(2)


                        data_request = FilaManagering.load_data(r"file\request_login.json")

                        data_request = Utility.unique_request("username",data_request)

                        for item in data_request :
                            
                            print (f"this user {item['name']}, {item['family']} wants to enter",end='\n')

                            answer = input("do you want to accept this user (y - ect) ?")

                            if answer in ("y", "Y" , "yes"):


                                    data_user = FilaManagering.load_data(r"file\user_pass.json")
                                    if isinstance(data_user,list):
                                            data_user.append(item)
                
                                    else :
                                            data_user = [data_user]
                                            data_user.append(item)

                                    FilaManagering.save_data(data_user,r"file\user_pass.json") 



                            data_request = [record for record in data_request if record["username"] !=  item['username']] 
                            FilaManagering.save_data(data_request,r"file\request_login.json")  

                        print("Done !")

                    if choice4 in ("3","e","E"):
                        break


            if choice1 in ("2","u","U"):

                current_user = []

                while(True):

                    system("cls")
                    valid = []
                    username = input("username :")

                    valid , current_user  = Utility.sarching("username",username)

                    if valid:
                        break
                    else:
                        print("we do not have this user\n")
                        want_to_signup = input("do you want to sign up (y-ect) ?")

                        if want_to_signup in ("y","Y"):
                            break
                

                while(True):

                    system("cls")
                    valid = []
                    password = input("password :")

                    valid , current_user = Utility.sarching("username",username)

                    if valid["password"] == password:
                        
                        break

                    else:
                        print("invalid password for this username")


                while(True):

                    welcome = " Welcome "
                    print(welcome.center(50, '-'),end="\n")

                    print("1.personal information")
                    print("2.shopping")
                    print("3.factors")
                    print("4.shopping cart")
                    print("5.exit")

                    choice3 = input("your choice :")

                    if choice3 in ("1","P","p"):

                        print(Utility.printing(current_user), end= "\n")


                    if choice3 in ("2","s","S"):

                        
                        pass

                        









                            




                    
                    
                


                

                



            if choice1 in ("3","e","E"):
                break



                        


                


                    

    if choice in ("3","e"):
        break

