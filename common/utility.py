 
from dal.textmanager import FilaManagering


class Utility:

    @staticmethod
    def sarching(key:str, value:str)-> None|str:

        errors = []

        data = FilaManagering.load_data(r"file\user_pass.json")
        target_data = next(( item for item in data if item[key] == value), None)

        if target_data:
            errors.append(f"{key} exists!!")

        return errors , target_data


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


            

       

        

    