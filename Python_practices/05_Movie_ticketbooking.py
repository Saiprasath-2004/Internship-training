class MovieTicket:
    def __init__(self,movie_name,seatno,price):
        self.movie_name=movie_name
        self.seatno=seatno
        self.price=price
        self.bookingStatus=False
    

    def bookTicket(self):
        if self.bookingStatus:
            print("Seat already Booked!,Try another seat")

        else:
            self.bookingStatus=True
            print("Ticket Booked Successfully")

    def cancelTicket(self):
        if self.bookingStatus:
            self.bookingStatus=False
            print("Ticket Cancelled successfully")
        else:
            print("No Booking exist")

    def show_ticket(self):
        print("\n----Ticket----")
        print("Movie :", self.movie_name)
        print("Seat No:", self.seatno)
        print("price:", self.price)
        print("Booked:", self.bookingStatus)

ticket = MovieTicket(
    "karupu",
    'A34',
    240
)

ticket1 = MovieTicket(
    "jananayagan",
    'A14',
    260
)
ticket.bookTicket()
ticket1.bookTicket()

ticket.show_ticket()
ticket1.show_ticket()

ticket1.cancelTicket()