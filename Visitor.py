class Visitor:
    def __init__(self,name,age,profession,id_card=None):
        self.name=name
        self.age=age
        self.profession=profession
        self.id_card=id_card
    
    def get_name(self):
        return self.name
    
    def get_age(self):
        return self.age
    
    def get_profession(self):
        return self.profession
    
    def get_id_card(self):
        return self.id_card
    
    def set_name(self,name):
        self.name=name
    
    def set_age(self,age):
        self.age=age
    
    def set_profession(self,profession):
        self.profession=profession
    
    def set_id_card(self,id_card):
        self.id_card=id_card

    def __str__(self):
        ret = f"Name:{self.name},Age:{self.age},Profession:{self.profession}"
        if(self.id_card):
            ret+=f",ID card={self.id_card}"
        return ret