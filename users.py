# Make a class called User. 
# Create two attributes called first_name and last_name, 
# and then create several other attributes that are typically stored in a user profile. 
# Make a method called describe_user() that prints a summary of the user’s information. 
# Make another method called greet_user() that prints a personalized greeting to the user.

class User():
    """A class representing a simple user profile"""

    def __init__(self, first_name, last_name, username, email, location):
        """Initialize the user"""
        self.first_name = first_name.title()
        self.last_name = last_name
        self.username = username
        self.email = email
        self.location = location.title()

    def describe_user(self  ):
        """Display a summary of the users information"""
        print(f"Your first name is {self.first_name}")
        print(f"Your last name: {self.last_name}")
        print(f"Username: {self.username}")
        print(f"Email: {self.email}")
        print(f"Location: {self.location}")

    def greet_user(self):   
        """Display a personalized greeting to the user""" 
        print(f"Welcome, {self.username}")

jakub = User('jakub','harancik','fake_jakub','jakub.harancik@gmail.com','Czech')
jakub.describe_user()

