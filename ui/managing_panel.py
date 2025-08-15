
from dal.textmanager import FilaManagering
from common.utility import Utility
class managing:

    @staticmethod
    def managing_access_request() :

        data_request = FilaManagering.load_data(r"file\request_login.json")  or []
        data_request = Utility.unique_request("username",data_request)

        data_user = FilaManagering.load_data(r"file\user_pass.json") or []
        if not isinstance(data_user, list):
            data_user = [data_user]

        remaining_requests = []

        
        for item in data_request:
            print(f"User '{item['name']} {item['family']}' wants to enter.")
            answer = input("Accept this user? (y/n): ").strip().lower()

            if answer in ("y", "yes"):
                data_user.append(item)
            else:
                remaining_requests.append(item)

        FilaManagering.save_data(data_user, r"file\user_pass.json")
        FilaManagering.save_data(remaining_requests, r"file\request_login.json")


        print("Requests processed successfully!")
