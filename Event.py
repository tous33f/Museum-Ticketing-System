import datetime

class Event:
    def __init__(self,name,location,date_time:datetime.datetime):
        self.name=name
        self.location=location
        self.date_time=date_time
    
    def get_name(self):
        return self.name
    
    def get_location(self):
        return self.location
    
    def get_date_time(self):
        return self.date_time
    
class Exhibition(Event):
    def __init__(self, name, location, date_time: datetime.datetime,artifacts,capacity):
        super().__init__(name, location, date_time)
        self.artifacts=[i for i in artifacts if location==i.get_location()]
        self.capacity=capacity
    
    def get_capacity(self):
        return self.capacity
    
    def set_capacity(self,capacity):
        self.capacity=capacity

    def set_artifacts(self,artifacts):
        del self.artifacts
        self.artifacts=[i for i in artifacts if self.location==i.get_location()]
    
    def __str__(self):
        artifacts=""
        for i in self.artifacts:
            artifacts+=i.get_title()
        return f"Event name:{self.name},Location:{self.location},Date:{self.date_time.date()},Time:{self.date_time.time()},Tickets left={self.capacity}\nArtifacts={artifacts}"

class Tour(Event):
    def __init__(self, name, date_time: datetime.datetime,guide):
        self.location="Museum"
        self.guide=guide
        super().__init__(name, self.location, date_time)

    def get_guide(self):
        return self.guide
    
    def __str__(self) -> str:
        return f"Event name:{self.name},Location:{self.location},Date:{self.date_time.date()},Time:{self.date_time.time()},Guide:{self.guide}"
        
class Special(Event):
    def __init__(self, name, location, date_time: datetime.datetime,capacity):
        super().__init__(name, location, date_time)
        self.capacity=capacity
        
    def get_capacity(self):
        return self.capacity
    
    def set_capacity(self,capacity):
        self.capacity=capacity
    
    def __str__(self) -> str:
        return f"Event name:{self.name},Location:{self.location},Date:{self.date_time.date()},Time:{self.date_time.time()},Tickets left={self.capacity}"
