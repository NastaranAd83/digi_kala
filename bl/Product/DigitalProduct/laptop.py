
from bl.Product.BaseProduct import Product


class laptop(Product):

    def __init__(self,brand , model ,name , price, os  , cpu ):
        super().__init__(brand , model ,name , price,os )
        self.__cpu = cpu
        


    @property
    def cpu(self):
        return self.__cpu

    @cpu.setter
    def cpu(self , cpu ) -> list:
        
            self.__cpu = cpu 
            return self.__cpu

  
                    




    


        
