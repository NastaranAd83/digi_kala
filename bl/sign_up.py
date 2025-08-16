
from bl.user_pass import UserPass
from dal.textmanager import FilaManagering
from bl.person import Person


class SignUp(UserPass):

    def __init__(self, name, family, phone, username, password , account_balance=0):
            super().__init__(name, family, phone, username, password,account_balance)
    
    def request_for_admin(self,file_path,amount:float|int=0):
        
        list_request =  {"name": self.name, "family": self.family,"phone":self.phone,"username":self.username,"password":self.password,"account_balance":self.balance,"amount":amount}

        data_request = FilaManagering.load_data(file_path)
        if not isinstance(data_request,list):
            data_request = [data_request]
              

        data_request.append(list_request)

        FilaManagering.save_data(list_data=data_request,file_path=file_path)

        print("your request It has sent to the admin")


    def admin_login(username , password):

        pass
    













        
        
        