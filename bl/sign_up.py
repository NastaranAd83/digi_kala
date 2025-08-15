
from bl.user_pass import UserPass
from dal.textmanager import FilaManagering
from bl.person import Person


class SignUp(UserPass):

    def __init__(self, name, family, phone, username, password , account_balance=0):
            super().__init__(name, family, phone, username, password,account_balance)
    
    def request_for_admin(self):

        
        list_request =  {"name": self.name, "family": self.family,"phone":self.phone,"username":self.username,"password":self.password,"account_balance":self.balance}

        data_request = FilaManagering.load_data(r"file\request_login.json")
        if isinstance(data_request,list):
                data_request.append(list_request)

        else :
            data_request = [data_request]
            data_request.append(list_request)
                    
        #list_request.append(f"this user {self.name} , {self.family} wants to sign up (username :{self.username}) ")

        FilaManagering.save_data(list_data=data_request,file_path=r"file\request_login.json")

        print("your request It has sent to the admin")


    def admin_login(username , password):

        pass
    













        
        
        