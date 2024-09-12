import datetime

class Artifacts:
    def __init__(self,title,artist,date:datetime.datetime,signif,location):
        self.title=title
        self.artist=artist
        self.date=date
        self.signif=signif
        self.location=location
    
    def get_title(self):
        return self.title
    
    def get_artist(self):
        return self.artist
    
    def get_signif(self):
        return self.signif

    def get_date(self):
        return self.date
    
    def get_location(self):
        return self.location

    def __str__(self):
        return f"Title:{self.title},Artist:{self.artist},Historical significance:{self.signif},Date:{self.date.date()},Location:{self.location}"

