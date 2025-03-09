# Author: Hamed Amiri
# Date: 09-Mar-2025
# Description: This program demonstrates Object-Oriented Programming (OOP) in Python by creating a 'Flower' class.
#              The class has an attribute 'name' and two methods: 'grow' and 'bloom'.
#              It then creates three flower objects and calls their respective methods.

# Defining the Flower class
class Flower:
    def __init__(self, name):
        """Constructor method to initialize the Flower object with a name attribute."""
        self.name = name  # Attribute: name of the flower

    def grow(self):
        """Method to print a message indicating that the flower is growing."""
        print("The " + self.name + " is growing.")

    def bloom(self):
        """Method to print a message indicating that the flower is blooming."""
        print("The " + self.name + " is blooming.")

# Main function to create flower objects and call their methods
def main():
    # Creating an instance of Flower with the name "Rose"
    flower1 = Flower("Rose")
    flower1.grow()  # Calling the grow method for Rose
    flower1.bloom()  # Calling the bloom method for Rose

    # Creating an instance of Flower with the name "Daisy"
    flower2 = Flower("Daisy")
    flower2.grow()  # Calling the grow method for Daisy
    flower2.bloom()  # Calling the bloom method for Daisy

    # Adding an additional flower object - "Tulip"
    flower3 = Flower("Tulip")
    flower3.grow()  # Calling the grow method for Tulip
    flower3.bloom()  # Calling the bloom method for Tulip

# Ensures the main function runs only if this script is executed directly
if __name__ == "__main__":
    main()
