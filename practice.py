class User:
    #use self and as many additional parameters as want passed
    def __init__(self, user_id, username):
    #init attributes-- what object has , variable---
        self.id = user_id
        self.username = username
        # using a default value so don't have to pass 0 in parameters
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1

      
# ex. same
# my_car.seats = 5
# my_car = seats(5)


# user_1 = User(input("id: "), input("username: "))
user_1 = User("001", "Alice")
user_2 = User("002", "John")

user_1.follow(user_2)

print(user_1.following)

# constructor- part of blueprint specifying what should happen when constructed (initialize)
# init function


