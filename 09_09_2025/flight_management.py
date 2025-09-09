class Flight:
    def __init__(self, flight_number, airline):
        self.flight_number = flight_number
        self.airline = airline

    def display_flight_details(self):
        print(f"flight number = {self.flight_number}, airline = {self.airline}")

class ScheduledFlight(Flight):
    def __init__(self, flight_number, airline, schedule_time, deprarture_time):
        super().__init__(flight_number, airline)
        self.schedule_time = schedule_time
        self.deprarture_time = deprarture_time
    
    def display_schedule_flight_details(self):
        self.display_flight_details()
        print(f"Schedule = {self.schedule_time}, airline = {self.deprarture_time}")

schedule_flight = ScheduledFlight("AI110", "Air India", "13:20 AM", "08::40 PM")
schedule_flight.display_schedule_flight_details()

class Person:
    def __init__(self, name, id):
        self.name = name
        self.id = id

class CrewMember(Person):
    def __init__(self, name, id, role):
        super().__init__(name, id)
        self.role = role

    def display_crew_member_details(self):
        print(f"Crew member details = {self.name}, airline = {self.id}, role = {self.role}")

class Pilot(CrewMember):
    def __init__(self, name, id, role, license, rank):
        super().__init__(name, id, role)
        self.license = license
        self.rank = rank

    def display_pilot_member_details(self):
        print(f"Pilot member details = {self.name}, airline = {self.id}, role = {self.role}, license = {self.license}, rank = {self.rank}")

print("#" * 80)
crew = CrewMember("Sam","123","Pilot")
crew.display_crew_member_details()

print("#" * 80)
pilot = Pilot("Ram","345","Captain","Yes","A+")
pilot.display_pilot_member_details()

class Service:
    def __init__(self):
        pass
    def service_info():
        print("Service info")

class SecurityService(Service):
    def __init__(self):
        super().__init__()

class BaggageService(Service):
    def __init__(self):
        super().__init__()


################################################################
class PassengerDetails:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def display_passenger_details(self):
        print(f"Name = {self.name}")
        print(f"Age = {self.age}")

class TicketDetails:
    def __init__(self,ticke_number,seat_number):
        self.ticket_number = ticke_number
        self.seat_number = seat_number
    
    def display_Ticket(self):
        print(f"Ticket number = {self.ticket_number}")
        print(f"Seat number = {self.seat_number}")

class Booking(PassengerDetails, TicketDetails):
    def __init__(self, name, age, ticke_number, seat_number):
        PassengerDetails.__init__(self,name, age)
        TicketDetails.__init__(self,ticke_number, seat_number)

    def display_all_info(self):
        self.display_passenger_details()
        self.display_Ticket()
        
print("#" * 80)
print("Booking details:")
book = Booking("Ram", "30", "S100", "A20")
book.display_all_info()
