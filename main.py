from tkinter import *
from tkinter import messagebox
import Museum
from Artifacts import Artifacts
from Visitor import Visitor
from Ticket import Ticket
import datetime
import Event

tour_min=2
tour_max=5

class main_menu:
    def __init__(self):
        self.root=Tk()
        self.root.title("Museum")
        self.root.geometry("852x560")
        self.museum=Museum.Museum()
        self.museum.add_artifacts(Artifacts("Pyrmaid","James",datetime.datetime(1850,5,12),"lorem ahjsdhasid","Outdoor spaces"))
        self.museum.add_events(Event.Exhibition("Mona Lisa","Exhibition halls",datetime.datetime(2000,3,4),self.museum.artifacts,12))
        self.museum.add_events(Event.Tour("Mona Lisa",datetime.datetime(2000,3,4),"Sam Smith"))

    def menu(self):
        self.clear()
        Label(self.root,text="The Louvre Museum",font=('Arial',20,'bold')).pack(pady=10)
        Button(self.root, padx=10,pady=5 , text="View artifacts",command= self.view_artifacts_gui ).pack(padx=50,pady=5)
        Button(self.root, padx=10,pady=5 , text="Add artifacts",command= self.add_artifacts_gui ).pack(padx=50,pady=5)
        Button(self.root, padx=10,pady=5 , text="View Exhibition events",command= self.view_exhibition_event_gui ).pack(padx=50,pady=5)
        Button(self.root, padx=10,pady=5 , text="Add Exhibition Event",command= self.add_exhibition_event_gui ).pack(padx=50,pady=5)
        Button(self.root, padx=10,pady=5 , text="View Special Event",command= self.view_special_event_gui ).pack(padx=50,pady=5)
        Button(self.root, padx=10,pady=5 , text="Add Special Event",command= self.add_special_event_gui ).pack(padx=50,pady=5)
        Button(self.root, padx=10,pady=5 , text="View Tour Event",command= self.view_tour_event_gui ).pack(padx=50,pady=5)
        Button(self.root, padx=10,pady=5 , text="Add Tour Event",command= self.add_tour_event_gui ).pack(padx=50,pady=5)
        Button(self.root, padx=10,pady=5 , text="Buy exhibition events ticket",command= self.view_exhibition_ticket ).pack(padx=50,pady=5)
        Button(self.root, padx=10,pady=5 , text="Buy tour ticket",command= self.view_tour_ticket ).pack(padx=50,pady=5)
        Button(self.root, padx=10,pady=5 , text="Buy special events ticket",command= self.view_special_ticket ).pack(padx=50,pady=5)

# exhibition event functions

    def view_exhibition_event_gui(self):
        self.clear()
        for i in self.museum.get_exhibition():
            Label(self.root,text=f"-> {i.__str__()}").pack(pady=5)
        Button(self.root, padx=10,pady=5 , text="Back",command= self.menu ).pack(padx=50,pady=5)

    def add_exhibition_event_gui(self):
        self.clear()

        # event name
        Label(self.root,text="Event name:").pack()
        self.exhibition_event_name=Entry(self.root,width=50,highlightthickness=2,borderwidth=0)
        self.exhibition_event_name.pack(padx=50,pady=5,ipadx=5,ipady=3)

        # date
        Label(self.root,text="Eevnt Date(Year-Month-Day):").pack()
        self.exhibition_event_date=Entry(self.root,width=50,highlightthickness=2,borderwidth=0)
        self.exhibition_event_date.pack(padx=50,pady=5,ipadx=5,ipady=3)

        #  capacity
        Label(self.root,text="Event maximum capacity:").pack()
        self.exhibition_event_capacity=Entry(self.root,width=50,highlightthickness=2,borderwidth=0)
        self.exhibition_event_capacity.pack(padx=50,pady=5,ipadx=5,ipady=3)

        # location
        location_options=[
            "Permanent galleries",
            "Exhibition halls",
            "Outdoor spaces"
        ]
        self.exhibition_event_location=StringVar()
        self.exhibition_event_location.set(None)
        Label(self.root,text="Event Location:").pack()
        for i in location_options:
            Radiobutton(self.root, text=f"{i}", variable=self.exhibition_event_location, value=f"{i}" ).pack()

        # add button
        Button(self.root, padx=10,pady=5 , text="Add event",command= self.add_exhibition_event).pack(padx=20,pady=5)

    def add_exhibition_event(self):
        artifacts=[i for i in self.museum.artifacts if i.get_location()==self.exhibition_event_location.get()]
        date=self.exhibition_event_date.get().split("-")
        if(len(date)<3):
            messagebox.showerror("Error","Date format in incorrect.Please try again")
        else:
            self.museum.add_events(Event.Exhibition(
                self.exhibition_event_name.get()
                ,self.exhibition_event_location.get(),
                datetime.datetime( int(date[0]) , int(date[1]) , int(date[2]) ) ,
                artifacts ,
                int(self.exhibition_event_capacity.get())
                ) )
        self.menu()

# special event functions

    def view_special_event_gui(self):
        self.clear()
        for i in self.museum.get_special():
            Label(self.root,text=f"-> {i.__str__()}").pack(pady=5)
        Button(self.root, padx=10,pady=5 , text="Back",command= self.menu ).pack(padx=50,pady=5)

    def add_special_event_gui(self):
        self.clear()

        # event name
        Label(self.root,text="Event name:").pack()
        self.special_event_name=Entry(self.root,width=50,highlightthickness=2,borderwidth=0)
        self.special_event_name.pack(padx=50,pady=5,ipadx=5,ipady=3)

        # date
        Label(self.root,text="Eevnt Date(Year-Month-Day):").pack()
        self.special_event_date=Entry(self.root,width=50,highlightthickness=2,borderwidth=0)
        self.special_event_date.pack(padx=50,pady=5,ipadx=5,ipady=3)

        #  capacity
        Label(self.root,text="Event maximum capacity:").pack()
        self.special_event_capacity=Entry(self.root,width=50,highlightthickness=2,borderwidth=0)
        self.special_event_capacity.pack(padx=50,pady=5,ipadx=5,ipady=3)

        # location
        location_options=[
            "Permanent galleries",
            "special halls",
            "Outdoor spaces"
        ]
        self.special_event_location=StringVar()
        self.special_event_location.set(None)
        Label(self.root,text="Event Location:").pack()
        for i in location_options:
            Radiobutton(self.root, text=f"{i}", variable=self.special_event_location, value=f"{i}" ).pack()

        # add button
        Button(self.root, padx=10,pady=5 , text="Add event",command= self.add_special_event).pack(padx=20,pady=5)

    def add_special_event(self):
        date=self.special_event_date.get().split("-")
        if(len(date)<3):
            messagebox.showerror("Error","Date format in incorrect.Please try again")
        else:
            self.museum.add_events(Event.Special(
                self.special_event_name.get()
                ,self.special_event_location.get(),
                datetime.datetime( int(date[0]) , int(date[1]) , int(date[2]) ) ,
                int(self.special_event_capacity.get())
                ) )
        self.menu()

# tour event functions

    def view_tour_event_gui(self):
        self.clear()
        for i in self.museum.get_tour():
            Label(self.root,text=f"-> {i.__str__()}").pack(pady=5)
        Button(self.root, padx=10,pady=5 , text="Back",command= self.menu ).pack(padx=50,pady=5)

    def add_tour_event_gui(self):
        self.clear()

        # event name
        Label(self.root,text="Event name:").pack()
        self.tour_event_name=Entry(self.root,width=50,highlightthickness=2,borderwidth=0)
        self.tour_event_name.pack(padx=50,pady=5,ipadx=5,ipady=3)

        # date
        Label(self.root,text="Eevnt Date(Year-Month-Day):").pack()
        self.tour_event_date=Entry(self.root,width=50,highlightthickness=2,borderwidth=0)
        self.tour_event_date.pack(padx=50,pady=5,ipadx=5,ipady=3)

        #  guide
        Label(self.root,text="Event guide name:").pack()
        self.tour_event_guide=Entry(self.root,width=50,highlightthickness=2,borderwidth=0)
        self.tour_event_guide.pack(padx=50,pady=5,ipadx=5,ipady=3)

        # add button
        Button(self.root, padx=10,pady=5 , text="Add event",command= self.add_tour_event).pack(padx=20,pady=5)

    def add_tour_event(self):
        date=self.tour_event_date.get().split("-")
        if(len(date)<3):
            messagebox.showerror("Error","Date format in incorrect.Please try again")
        else:
            self.museum.add_events(Event.Tour(
                self.tour_event_name.get(),
                datetime.datetime( int(date[0]) , int(date[1]) , int(date[2]) ) ,
                self.tour_event_guide.get()
                ) )
        self.menu()

# tour tickets functions 

    def view_tour_ticket(self):
        self.clear()

        self.visitor=None
        self.visitors=[]
        tour=[i for i in self.museum.events if isinstance(i,Event.Tour)]
        if len(tour)==0:
            messagebox.showinfo("Sorry","There are currently no Group Tours")
            self.menu()
        else:
            event=IntVar()
            event.set(0)
            cnt=0
            for value in tour:
                Radiobutton(self.root, text=f"{value.__str__()}", variable=event, value=f"{cnt}" ).pack()
                cnt+=1
            self.total_visitors=Label(self.root,text=f"Total visitors:{len(self.visitors)}(Min={tour_min},Max={tour_max})")
            self.total_visitors.pack()
            Button(self.root, padx=10,pady=5 , text="Enter Visitors Information",command= (
                lambda: self.get_visitor( 1 )
            ) ).pack(padx=20,pady=5)
            Button(self.root, padx=10,pady=5 , text="Buy ticket",command= (lambda: self.buy_tour_ticket(tour[event.get()])) ).pack(padx=20,pady=5)
        
    def buy_tour_ticket(self,event):
        if len(self.visitors)<tour_min or len(self.visitors)>tour_max:
            messagebox.showerror("Error","Incorrect number of visitors.Please try again")
            self.menu()
        else:
            price=0
            out=""
            for i in self.visitors:
                ticket=Ticket(i,event.get_name(),event.get_location(),event.get_date_time(),True)
                self.museum.add_tickets(ticket)
                messagebox.showinfo("Ticket Successfull",f"{ticket.__str__()}")
                price+=ticket.get_price_num()
            messagebox.showinfo("Ticket Successfull",f"Total Bill:{price} AED")
            self.menu()


# exhibition tickets functions 

    def view_exhibition_ticket(self):
        self.clear()

        self.visitor=None
        exhibition=self.museum.get_exhibition()
        if len(exhibition)==0:
            messagebox.showinfo("Sorry","There are currently no Exhibition events")
            self.menu()
        else:
            event=IntVar()
            event.set(0)
            cnt=0
            for value in exhibition:
                Radiobutton(self.root, text=f"{value.__str__()}", variable=event, value=f"{cnt}" ).pack()
                cnt+=1
            Button(self.root, padx=10,pady=5 , text="Enter Visitor Information",command= self.get_visitor).pack(padx=20,pady=5)
            Button(self.root, padx=10,pady=5 , text="Buy ticket",command= (lambda: self.buy_exhibition_ticket(exhibition[event.get()])) ).pack(padx=20,pady=5)
        
    def buy_exhibition_ticket(self,event):
        if self.visitor==None and event.get_capacity()>0:
            messagebox.showerror("Error","Please enter visitor information")
            self.menu()
        else:
            ticket=Ticket(self.visitor,event.get_name(),event.get_location(),event.get_date_time())
            self.museum.add_tickets(ticket)
            event.set_capacity(event.get_capacity()-1)
            messagebox.showinfo("Ticket Successfull",f"{ticket.__str__()},Total Bill:{ticket.get_price()}")
            self.menu()

# special tickets functions
            
    def view_special_ticket(self):
        self.clear()

        self.visitor=None
        special=self.museum.get_special()
        if len(special)==0:
            messagebox.showinfo("Sorry","There are currently no Special events")
            self.menu()
        else:
            event=IntVar()
            event.set(0)
            cnt=0
            for value in special:
                Radiobutton(self.root, text=f"{value.__str__()}", variable=event, value=f"{cnt}" ).pack()
                cnt+=1
            Button(self.root, padx=10,pady=5 , text="Enter Visitor Information",command= self.get_visitor).pack(padx=20,pady=5)
            Button(self.root, padx=10,pady=5 , text="Buy ticket",command= (lambda: self.buy_special_ticket(special[event.get()])) ).pack(padx=20,pady=5)
        
    def buy_special_ticket(self,event):
        if self.visitor==None and event.get_capacity()>0:
            messagebox.showerror("Error","Please enter visitor information")
            self.menu()
        else:
            ticket=Ticket(self.visitor,event.get_name(),event.get_location(),event.get_date_time())
            self.museum.add_tickets(ticket)
            event.set_capacity(event.get_capacity()-1)
            messagebox.showinfo("Ticket Successfull",f"{ticket.__str__()},Total Bill:{ticket.get_price()}")
            self.menu()
            
# tickets helper functions

    def get_visitor(self,tour=None):
        new_window=Toplevel(self.root)
        new_window.title("Visitor Information")
        new_window.geometry("852x520")

        # name
        Label(new_window,text="Visitor name:").pack()
        self.visitor_name=Entry(new_window,width=50,highlightthickness=2,borderwidth=0)
        self.visitor_name.pack(padx=50,pady=5,ipadx=5,ipady=3)

        # age
        Label(new_window,text="Visitor age:").pack()
        self.visitor_age=Entry(new_window,width=50,highlightthickness=2,borderwidth=0)
        self.visitor_age.pack(padx=50,pady=5,ipadx=5,ipady=3)

        # profession
        Label(new_window,text="Visitor profession:").pack()
        self.visitor_profession=Entry(new_window,width=50,highlightthickness=2,borderwidth=0)
        self.visitor_profession.pack(padx=50,pady=5,ipadx=5,ipady=3)

        # id_card
        Label(new_window,text="Visitor ID card(Optional):").pack()
        self.visitor_id_card=Entry(new_window,width=50,highlightthickness=2,borderwidth=0)
        self.visitor_id_card.pack(padx=50,pady=5,ipadx=5,ipady=3)

        Button(new_window, padx=10,pady=5 , text="Next",command= (lambda: self.assign_visitor(new_window,tour))).pack(padx=20,pady=5)
        new_window.mainloop()

    def assign_visitor(self,new_window,tour=None):
        if self.visitor_id_card.get()=="":
            self.visitor_id_card=None
        else:
            self.visitor_id_card=self.visitor_id_card.get()
        self.visitor=Visitor(self.visitor_name.get(),int(self.visitor_age.get()),self.visitor_profession.get(),self.visitor_id_card)
        new_window.destroy()
        if tour:
            self.visitors.append(self.visitor)
            self.total_visitors.config(text=f"Total visitors:{len(self.visitors)}(Min={tour_min},Max={tour_max})")

# artifacts functions 
    def view_artifacts_gui(self):
        self.clear()
        for i in self.museum.get_artifacts():
            Label(self.root,text=f"-> {i.__str__()}").pack(pady=5)
        Button(self.root, padx=10,pady=5 , text="Back",command= self.menu ).pack(padx=50,pady=5)

    def add_artifacts_gui(self):
        self.clear()

        # title
        Label(self.root,text="Artifact Title:").pack()
        self.artifact_name=Entry(self.root,width=50,highlightthickness=2,borderwidth=0)
        self.artifact_name.pack(padx=50,pady=5,ipadx=5,ipady=3)

        # artist
        Label(self.root,text="Artifact Artist:").pack()
        self.artifact_artist=Entry(self.root,width=50,highlightthickness=2,borderwidth=0)
        self.artifact_artist.pack(padx=50,pady=5,ipadx=5,ipady=3)

        # date
        Label(self.root,text="Artifact Date(Year-Month-Day):").pack()
        self.artifact_date=Entry(self.root,width=50,highlightthickness=2,borderwidth=0)
        self.artifact_date.pack(padx=50,pady=5,ipadx=5,ipady=3)

        #  historical significance
        Label(self.root,text="Artifact historical significance:").pack()
        self.artifact_signif=Entry(self.root,width=50,highlightthickness=2,borderwidth=0)
        self.artifact_signif.pack(padx=50,pady=5,ipadx=5,ipady=3)

        # location
        location_options=[
            "Permanent galleries",
            "Exhibition halls",
            "Outdoor spaces"
        ]
        self.artifact_location=StringVar()
        self.artifact_location.set(None)
        Label(self.root,text="Artifact Location:").pack()
        for i in location_options:
            Radiobutton(self.root, text=f"{i}", variable=self.artifact_location, value=f"{i}" ).pack()

        # add button
        Button(self.root, padx=10,pady=5 , text="Add artifacts",command= self.add_artifact).pack(padx=20,pady=5)

    def add_artifact(self):
        date=self.artifact_date.get().split("-")
        if(len(date)<3):
            messagebox.showerror("Error","Date format in incorrect.Please try again")
        else:
            self.museum.add_artifacts(Artifacts(self.artifact_name.get(),self.artifact_artist.get(),datetime.datetime( int(date[0]) , int(date[1]) , int(date[2]) ) , self.artifact_signif.get() , self.artifact_location.get() ) )
        self.menu()

    def clear(self):
        for i in self.root.pack_slaves():
            i.destroy()

    def run(self):
        self.root.mainloop()

menu=main_menu()
menu.menu()
menu.run()