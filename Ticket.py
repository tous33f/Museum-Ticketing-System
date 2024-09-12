from Visitor import Visitor
import datetime

class Ticket:
    def __init__(self,visitor:Visitor,event,location,date_time:datetime.datetime,group=False,price=None):
        self.visitor=visitor
        self.event=event
        self.location=location
        self.date_time=date_time
        if not price:
            price=(63+(63*0.1))
        if group:
            self.price=price*0.5
        else:
            if visitor.get_age()>=18 and visitor.get_age()<=60:
                self.price=price
            else:
                if visitor.get_id_card():
                    self.price=0
                else:
                    self.price=price
        
    def get_visitor(self):
        return self.visitor

    def get_price(self):
        return f"{self.price} AED"
    
    def get_price_num(self):
        return self.price
    
    def __str__(self):
        return f"{self.visitor.__str__()},Event:{self.event},Location:{self.location},Date:{self.date_time.date()},Time:{self.date_time.time()}"
