from Ticket import Ticket
from Visitor import Visitor
from Artifacts import Artifacts
import Event

min_group_num=3

class Museum:
    def __init__(self):
        self.artifacts=[]
        self.events=[]
        self.tickets=[]

    def add_artifacts(self,artifact:Artifacts):
        fil=[i for i in self.artifacts if i.get_title()==artifact.get_title() and i.get_artist()==artifact.location()]
        if(len(fil)>0):
            return "Cannot add Artifact as it is already present"
        else:
            self.artifacts.append(artifact)
            for i in self.get_exhibition():
                i.set_artifacts(self.artifacts)
            return "Artifact successfully added"
        
    def add_events(self,event):
        fil=[i for i in self.events if (i.get_location()==event.get_location() and i.get_date_time()==event.get_date_time() )]
        if(len(fil)>0):
            return "Cannot add Artifact as it is already present"
        else:
            self.events.append(event)
            return "Artifact successfully added"
    
    def add_tickets(self,ticket:Ticket):
        self.tickets.append(ticket)
        
    def get_exhibition(self):
        fil=[ i for i in self.events if isinstance(i,Event.Exhibition) ]
        return fil
    
    def get_artifacts(self):
        return self.artifacts
    
    def get_tour(self):
        fil=[ i for i in self.events if isinstance(i,Event.Tour) ]
        return fil
    
    def get_special(self):
        fil=[ i for i in self.events if isinstance(i,Event.Special) ]
        return fil
    
    def get_ticket(self,name):
        fil=[i for i in self.tickets if i.get_visitor().get_name()==name]
        return fil
    
def buy_ticket(name,age,profession,event,museum:Museum,id_card=None):
    ticket=Ticket(Visitor(name,age,profession,id_card),event.get_name(),event.get_location(),event.get_date_time())
    museum.add_tickets(ticket)
