from dal.textmanager import FilaManagering
from bl.person import Person


class Admin_Utility(Person):



    def request_for_admin(self,file_path : str ,amount:float|int=0):
        
        list_request =  {
        "name": self.name,
        "family": self.family,
        "phone":self.phone,
        "username":self.username,
        "password":self.password,
        "account_balance":self.account_balance,
        "amount":amount}

        data_request = FilaManagering.load_data(file_path)

        if not isinstance(data_request,list):
            data_request = [] if data_request is None else [data_request]
           
              

        data_request.append(list_request)

        FilaManagering.save_data(list_data=data_request,file_path=file_path)

        print("your request It has sent to the admin")




    def unique_request(key:str, data : list[dict] )-> list[dict]:

        unique_requests = []
        seen_data = set()
        for record in data :
            if record[key] not in seen_data:
                seen_data.add(record[key])
                unique_requests.append(record)
        
        data_request = unique_requests

        return data_request