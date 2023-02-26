# Add an attribute called number_served with a default value of 0 = DONE
# Create an instance called restaurant from this class
# Print the number of the customers the restaurant has served, and then change this value and print it again.
# Add a method called set_number_served() that lets you set the number of the customers that have been served
# Call this method with a new number and print the value again
# Create a method called increment_number_served() that lets you increment the number of customers who've been served.
# Call this method with any number you like that could represent how many customers were served in, say, a day of business.

class Restaurant():
    """ A class representing a restaurant"""

    def __init__(self, name, cuisine_type):
        """Initilaze the restaurant"""
        self.name = name.title()
        self.cuisine_type = cuisine_type
        self.number_served = 0


    def describe_restaurant(self):
        """Display a summary of the restaurant"""
        msg = f"{self.name} servers wonderful food {self.cuisine_type}"
        print(msg)

    def open_restaurant(self):
        """Display a message  that the restaurant is open"""
        print(f"My {self.name} chinese  restaurant is the best restaurant in the world ")

samuel_restaurant = Restaurant('restaurant','chinese')
samuel_restaurant.describe_restaurant()
samuel_restaurant.open_restaurant()          

bara_restaurant = Restaurant('muto','italian')
bara_restaurant.describe_restaurant()

jakub_restaurant = Restaurant('ouioui','french')
jakub_restaurant.describe_restaurant()        