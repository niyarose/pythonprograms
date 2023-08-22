class mobile(object):
    name: str
    price:int
    display:str


    def __init__(self,**kwargs):
        self.name=kwargs.get("name")
        self.price=kwargs.get("price")
        self.display=kwargs.get("display")


    def __str__(self):
        return self.name
    @property #=> decorator 

    def get_price(self):
        return self.price
    @property #the class method works as a attribute 
    def get_dis_price(self):
        return self.price-1000
    

obj=mobile(name="oneplus",price=30000,display="amoled")
# print(obj)
# print(obj.get_price)
print(obj.get_dis_price)
        