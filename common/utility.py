 
from os import system
from time import sleep
from dal.textmanager import FilaManagering


class Utility:

    @staticmethod
    def sarching(key:str, value:str)-> None|str:

        errors = []

        data = FilaManagering.load_data(r"file\user_pass.json")
        target_data = next(( item for item in data if item[key] == value), None)

        if target_data:
            errors.append(f"{key} exists!!")
            return errors[0] , target_data

        else:
            return None , None



       


    def unique_request(key:str, data : list )-> None|str:

        unique_requests = []
        seen_data = set()
        for record in data :
            if record[key] not in seen_data:
                seen_data.add(record[key])
                unique_requests.append(record)
        
        data_request = unique_requests

        return data_request
                


    def printing(dict_data:dict) -> str :

        headers = list(dict_data.keys())
        print("   ,   ".join(headers))
        print("--"*48)
        print("   ,   ".join(str(dict_data.get(h, "")) for h in headers)) 


    def get_valid_input(prompt, validators):
        while True:

            system("cls")
            value = input(prompt)
            errors = []

            for validator in validators:
                result = validator(value)
    
                if isinstance(result, list):
                    errors.extend(result)
                
                elif isinstance(result, tuple):
                    err, _ = result
                    if err:  
                        errors.append(err)

                elif isinstance(result, str):
                    errors.append(result)

            if not errors:
                return value

            for err in errors:
                print(err)
            sleep(2)

    def get_fixed_input(prompt, correct_value, error_message):
        
        while True:
            
            system("cls")
            value = input(prompt)
            if value == correct_value:
                return value
            print(error_message)
            sleep(2)
            


                        
            

       

        

    