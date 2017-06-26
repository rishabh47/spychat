from datetime import datetime
#spy class to reuse the code
class Spy:

#constructor of the class to initialize the values
    def __init__(self, name, salutation, age, rating):
        self.name = name
        self.salutation = salutation
        self.age = age
        self.rating = rating
        self.is_online = True
        self.chats = []
        self.current_status_message = None

#chatmessage class to reuse the code
class ChatMessage:

    # constructor of the class to initialize the values
    def __init__(self,message,sent_by_me):
        self.message = message
        self.time = datetime.now()
        self.sent_by_me = sent_by_me
#our predefined spy
spy = Spy('bond', 'Mr.', 24, 2.1)
#oyr predefined friends
friend_one = Spy('Ankush', 'Mr.', 21, 2.7)
friend_two = Spy('Tanya', 'Ms.', 18, 2.1)
friend_three = Spy('Karan', 'Prof.', 33, 3.7)

#adding our predefined friends to a list
friends = [friend_one, friend_two, friend_three]
