

import json


class FilaManagering :



    @staticmethod
    def load_data(file_path):
        #file=r"file\user_pass.json"

            try:
                with open(file_path, "r",encoding="utf-8") as file_object:
                    return json.load(file_object)
                    
            except (FileNotFoundError, json.JSONDecodeError):
                return []  

    @staticmethod
    def save_data(list_data : list,file_path):
        # "file\request_login.json"
        # "file\user_pass.json"
        

            with open(file=file_path,mode='w', encoding="utf-8") as file_object:
                json.dump(list_data ,file_object,ensure_ascii=False, indent=4) 


   


        
