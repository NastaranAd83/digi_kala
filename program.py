
from os import system
from time import sleep
from bl.sign_up import SignUp
from bl.person import Person
from dal.textmanager import FilaManagering
from common.utility import Utility
from bl.user_pass import UserPass
from dal.sql import DatabaseManager
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
                    print("1.list request")
                    print("2.exit\n")


                    choice4 = input("your choice : ")
                    if choice4 in ("1","L","l"):

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

                    if choice4 in ("2","e","E"):
                        break


            if choice1 in ("2","u","U"):

                current_user = []
                products = []

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
                    db = DatabaseManager(host="127.0.0.1",user="root",password="",database="mysql_helper")

                    welcome = " Welcome "
                    print(welcome.center(50, '-'),end="\n")



                    print("1.personal information")
                    print("2.shopping")
                    print("3.shopping cart")
                    print("4.factors")
                    print("5.increase account balance")
                    print("6.exit")

                    choice3 = input("your choice :")

                    if choice3 in ("1","P","p"):

                        print(Utility.printing(current_user), end= "\n")


                    if choice3 in ("2","s","S"):

                        while(True):

                           
                            db.read_records("cellphone")
                            db.read_records("laptop")


                            print ("\n which one do you want ?")
                            print ("please enter the id of the ")

                            while(True):

                                id_ = input("id : ")

                                try :
                                    id_ = int (id_)

                                except:
                                    print("invalid value for id ")
                                    sleep(2)
                                    system("cls")


                                else :
                                    products.append(id_)
                                    break
                            
                            done = input("are you done(y-etc)?")

                            if done in ("y","Y","yes"):
                                break

                    if choice3 in ("3","c","C"):

                        sum_= db.return_id_name(products)

                        done = input("are you done(yes-etc) ?")

                        if done in ("y","Y","yes"):
                            balance = current_user[0].get("account_balance")
                            if balance - sum_ < 0 :
                                print("unsuccessful shop !!")
                                print(f"you need to increase your balance , atleast :{abs(balance - sum_)}")
                                print(f"your current balance -> {balance}")
                                sleep(2.5)

                            else :
                                balance = balance - sum_ 
                                current_user[0]["account_balance"] = balance
                                db.update_record(products)
                                db.delete_record()
                                
                                products = []
                                print("successful shop ")

                        





                    if choice3 in ("4","F","f"):
                        pass


                    if choice3 in ("5","i","I") :

                        while(True):

                            amount = input("how much do you want to increase your balance ?")

                            try:
                                amount = float(amount)

                            except:

                                print("invalid amount")

                            else:
                                balance = current_user[0].get("account_balance")
                                current_user[0]["account_balance"]= current_user[0].get("account_balance") + amount
                                print("your current balance : " , current_user[0].get("account_balance"))

                                sleep(2)
                                break




                        

                    



                        


                            




                            


                                




                            
                        



                        

                        









            


                    
                    
                


                

                



            if choice1 in ("3","e","E"):
                break



                        


                


                    

    if choice in ("3","e"):
        break

