class Notification:
    def send(self):
        pass

class Email(Notification):
    def send(self):
        print("The email notification was send")

class SMS(Notification):
    def send(self):
        print("The Sms notification was send")

class Push(Notification):
    def send(self):
        print("The Push notification was send")


Notifications = [
    Email(),
    SMS(),
    Push()
]

for n in Notifications:
    n.send()