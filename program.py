
from os import system
from time import sleep
from bl.person import Person
from common.utility.utility_ui import Utility
from dal.sql import DatabaseManager
from common.utility.utility_ui import Utility
from ui.managing_panel import Managing
from common.utility.admin_utility import Admin_Utility
while(True):


    system("cls")
    
    menu = "MAIN MENU"
    print(menu.center(50,"-"),end="\n")

    print("1.sign up")
    print("2.sign in")
    print("3.exit")

    choice = input("\n your choice : ")

    if choice in ("1","up"):


                # region validation

                
                name = Utility.get_valid_input("name : ",[
                lambda v :Person.validation(v)])
                

                family = Utility.get_valid_input("family : ",[
                lambda v :Person.validation(v)])
                

                phone = Utility.get_valid_input("phone : ",[
                lambda v : Person.validation(v, True),
                lambda v : Utility.sarching("phone",v)])

                username = Utility.get_valid_input("username : ",[
                lambda v : Utility.sarching("username",v)
                ])
                password = Utility.get_valid_input("password : ",[
                lambda v : Person.check_validation(v) ])
                
                # endregion
                 

                admin = Admin_Utility(name=name,family=family,
                phone=phone,username=username,password=password)
                

                admin.request_for_admin(r"file\request_login.json")
                sleep(2)

    if choice in ("2","in"):

         while(True):

            system("cls")
            menu = "SIGN IN MENU"
            print(menu.center(50,"-"),end="\n")

            print("1.admin")
            print("2.user")
            print("3.exit\n")

            choice1 = input("your choice : ")

            if choice1 in ("1,a,A"):

                # region log in  for admin 
                username = Utility.get_fixed_input("username: ", "admin", "invalid username for admin")
                password = Utility.get_fixed_input("password: ", "140724N/a", "invalid password for admin")
                # endregion
                
                welcome = "Welcome , Admin"
                print(welcome.center(50,"-"))
                print("1.list access request ")
                print("2.list increase account balance")
                print("3.exit\n")
            
                    
                choice4 = input("your choice : ")

                # region admin chioces
                if choice4 in ("1","L","l"):

                    Managing.managing_access_request()

                if choice4 in ("2","ab","Ab"):

                    Managing.managing_credit_increase_request()

                if choice4 in ("3","e","E"):
                    break
                # endregion 

            if choice1 in ("2","u","U"):

                current_user = []
                products = []
                factors = []

                current_user = Managing.login_user()

                if not current_user :
                    break 

                while(True):

                    db = DatabaseManager(host="127.0.0.1",user="root",password="",database="mysql_helper")

                    #  region user menu
                    welcome = f" Welcome , {current_user['username']} "
                    print(welcome.center(50, '-'),"Wallet",current_user['account_balance'],end="\n")

                    
                    print("1.personal information")
                    print("2.shopping")
                    print("3.shopping cart")
                    print("4.factors")
                    print("5.increase account balance")
                    print("6.exit")

                    # endregion 

                    choice3 = input("your choice :")

                    if choice3 in ("1","P","p"):

                        Utility.printing(current_user)


                    if choice3 in ("2","s","S"):

                        while(True):

                           
                            db.read_records("cellphone")
                            db.read_records("laptop")


                            print ("\n which one do you want ?")
                            print ("please enter the id of the ")

                            id_ = input("id : ")

                            try :
                                id_ = int (id_)

                            except:
                                print("invalid value for id ")

                                sleep(2)
                               
                            else :
                                products.append(id_)
                                done = input("are you done(y-etc)?")
                                if done in ("y","Y","yes"):
                                    break

                            finally:
                                system("cls")

                            
                            
                    if choice3 in ("3","c","C"):

                        sum_ , factors = db.return_id_name(products)

                        done = input("are you done(yes-etc) ?")

                        if done in ("y","Y","yes"):
                            balance = current_user.get("account_balance")
                            if balance - sum_ < 0 :
                                print("unsuccessful shop !!")
                                print(f"you need to increase your balance , atleast :{abs(balance - sum_)}")
                                print(f"your current balance -> {balance}")
                                sleep(2.5)

                            else :
                                balance = balance - sum_ 
                                current_user["account_balance"] = balance
                                db.update_record(products)
                                db.delete_record()
                                for i,factor in enumerate(factors) :
                                    my_dict = {'username': current_user["username"], **factor}
                                    factors[i] = my_dict

                                db.add_factors("factors",factors)
                                factors = []
                                products = []
                                print("successful shop")
                                sleep(2)


                    if choice3 in ("4","F","f"):

                        print ("products that you have bought\n")
                        db.read_records("factors",current_user["username"])
                        sleep(2)


                    if choice3 in ("5","i","I") :

                        while(True):

                            amount = input("how much do you want to increase your balance ?")
                            Utility.validate_number(amount,min_value=10.0)

                            try:
                                amount = float(amount)

                            except:

                                print("invalid amount")

                            else:
                                
                                sign_up = Person(current_user['name'],current_user['family'],current_user['phone'],current_user['username'],current_user['password'],current_user['account_balance'])
                                Admin_Utility.request_for_admin(r"file\request_credit_increase.json",amount)
                               
                                sleep(2)
                                system("cls")

                                break
                    
                    if choice3 in ("E","e","6"):
                        break


            if choice1 in ("3","e","E"):
                break

    if choice in ("3","e"):
        break

