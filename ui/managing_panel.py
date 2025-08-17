
from os import system
from time import sleep
from dal.textmanager import FilaManagering
from common.utility.utility_ui import Utility
from common.utility.admin_utility import Admin_Utility
class Managing:

    @staticmethod
    def managing_access_request() :

        data_request = FilaManagering.load_data(r"file\request_login.json")  or []
        data_request = Admin_Utility.unique_request("username",data_request)

        data_user = FilaManagering.load_data(r"file\user_pass.json") or []
        if not isinstance(data_user, list):
            data_user = [data_user]

        remaining_requests = []

        if data_request :
            for item in data_request:
                print(f"User '{item['username']}'  wants to enter.")
                answer = input("Accept this user? (y/n): ").strip().lower()

                if answer in ("y", "yes"):
                    data_user.append(item)

                elif answer not in ("n","no"):
                    remaining_requests.append(item)

            FilaManagering.save_data(data_user, r"file\user_pass.json")
            FilaManagering.save_data(remaining_requests, r"file\request_login.json")
            print("Requests processed successfully!")


        else :
            print("you do not have any request")

                
       

    
    def managing_credit_increase_request ():

        data_request = FilaManagering.load_data(r"file\request_credit_increase.json")  or []
        data_user = FilaManagering.load_data(r"file\user_pass.json") or []
        if not isinstance(data_user, list):
            data_user = [data_user]


        remaining_requests = []

        if data_request :

            for item in data_request:
                print(f"User '{item['username']}' wants to increase account balance (amount : {item['amount']}).")
                answer = input("Do you accept this request ? (y/n): ").strip().lower()

                if answer in ("y", "yes"):
                    for user in data_user:
                        if user['username'] == item["username"]:
                            user['account_balance'] += item['amount'] 
                

                elif answer not in ("n","no"):
                    remaining_requests.append(item)


            FilaManagering.save_data(data_user,r"file\user_pass.json")
            FilaManagering.save_data(remaining_requests, r"file\request_credit_increase.json")
            print("Requests processed successfully!")

        else:
            print("you do not have any request")

        
    def login_user():

        while True:
            system("cls")
            username = input("username: ").strip()
            
            _ , current_user = Utility.sarching("username", username)

            if not current_user:  
                print("We do not have this user.\n")
                want_to_signup = input("Do you want to sign up? (y/n): ").lower()
                if want_to_signup in ("y", "yes"):
                    return None  
                continue

            while True:
                system("cls")
                password = input("password: ").strip()

                if current_user["password"] == password:
                    print("Login successful!")
                    return current_user 
                else:
                    print("Invalid password for this username.")
                    sleep(1.5)

            



