
from bl.Product.BaseProduct import product

class cellphone(product):

    def __init__(self,brand , model ,name , price, os  , color):
        super().__init__(brand , model ,name , price,os )
        self.__color = color
        


    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self , color ) -> list:
        
        self.__color = color 
        return self.__color