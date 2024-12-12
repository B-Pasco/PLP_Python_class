class Superhero:
    """
    A class to represent a superhero with unique abilities and attributes.
    """
    def __init__(self, name, alias, power, weakness):
        self.name = name
        self.alias = alias
        self.power = power
        self.weakness = weakness

    def display_identity(self):
        return f"I am {self.alias}, also known as {self.name}!"

    def use_power(self):
        return f"{self.alias} uses {self.power}!"

    def reveal_weakness(self):
        return f"{self.alias}'s weakness is {self.weakness}."

class Villain(Superhero):
    """
    A class to represent a villain, inheriting from Superhero.
    """
    def __init__(self, name, alias, power, weakness, good_plan):
        super().__init__(name, alias, power, weakness)
        self.good_plan = good_plan

    def enact_plan(self):
        return f"{self.alias} is executing their good plan: {self.good_plan}!"

# Demonstration of Superhero and Villain
superhero = Superhero("Clark Kent", "Superman", "Super Strength", "Kryptonite")
villain = Villain("Lex Luthor", "Lex", "Brilliant Mind", "Arrogance", "Saving the world")

print(superhero.display_identity())
print(superhero.use_power())
print(superhero.reveal_weakness())
print(villain.display_identity())
print(villain.enact_plan())

# Activity 2: Polymorphism Challenge
class Vehicle:
    """
    A base class for vehicles.
    """
    def move(self):
        raise NotImplementedError("Sub_classes must override the move() method.")

class Car(Vehicle):
    def move(self):
        return "Driving"

class Plane(Vehicle):
    def move(self):
        return "Flying"

class Boat(Vehicle):
    def move(self):
        return "Sailing"

class Bicycle(Vehicle):
    def move(self):
        return "Pedaling"

# Demonstrating Polymorphism
vehicles = [Car(), Plane(), Boat(), Bicycle()]
for vehicle in vehicles:
    print(vehicle.move())
