import random

class Tamagotchi:
    def __init__(self, health, hunger, mess, hapiness, name, age = 0, is_sick = False):
        self.health = health
        self.hunger = hunger
        self.mess = mess
        self.hapiness = hapiness
        self.name = name
        self.age = age
        self.is_sick = is_sick

        self.sick_probability = 0
    
    # ====== BACKGROUND METHODS ====== #
    
    def age_increase(self, time):
        self.age += time

    def take_damage(self, amount):
        self.health -= amount
    
    def check_stats(self):
        if self.health < 30 or self.age > 20 or self.mess > 30:
            self.sick_probability += 0.01
        
        if self.hunger > 200:
            self.take_damage(10)
        
        if self.health <= 0:
            self.die()
            return
        
        if self.is_sick:
            self.hapiness -= 10
            self.health -= 5

    def print_stats(self):
        print(f"{self.name}'s stats:\nHealth: {self.health} | Hunger: {self.hunger} | Mess: {self.mess} | Hapiness: {self.hapiness} | Age: {self.age} | Sick: {self.is_sick}")

    def roll_sickness(self):
        roll = random.random()

        if roll <= self.sick_probability:
            self.is_sick = True
    
    # ======================== #

    def clean(self):
        if self.mess == 0:
            print(f"{self.name} is already clean...")
            return
        
        print(f"You clean {self.name}. They are now shiny as a gold coin!")

        self.mess -= 10

    def feed(self, option: str):
        if not option:
            option = "food"
        
        elif option.lower() not in ("food", "snack"):
            print(f"{option} is not an option.")
            return
        
        food_type = option.lower()

        if food_type == "food":
            self.hunger = max(self.hunger - 10, 0)
            self.hapiness += 10
            self.health += 5
        
        elif food_type == "snacks":
            self.hunger = max(self.hunger - 5, 0)
            self.hapiness += 20
            self.health -= 5
        
        self.mess += 10
        
        print(f"You feed {self.name}")

    def play(self):
        self.hunger += 10
        self.hapiness += 20

        print(f"You play with {self.name}. Look how happy they are!")
    
    def die(self):
        print(f"{self.name} died at age {self.age}. RIP ☠️")
    
    def give_meds(self):
        print(f"You give {self.name} their meds. They feel better!")

        self.is_sick = False

pet = Tamagotchi(50, 50, 0, 50, input("What is your pet's name?\n> ").title())

while pet.health > 0:
    pet.print_stats()

    meds_option = " | meds" if pet.is_sick == True else ""
    choice = input(f"What do you want to do? [feed | play | clean{meds_option}]\n> ").lower()

    if choice in ["feed", "f"]:
        pet.feed(input("What do you want to feed your pet? [Food | snacks]\n> "))
    
    elif choice in ["play", "p"]:
        pet.play()
    
    elif choice in ["clean", "c"]:
        pet.clean()
    
    elif choice in ["meds", "m"] and pet.is_sick:
        pet.give_meds()
    
    pet.hapiness -= 5
    pet.hunger += 5
    
    pet.check_stats()
    pet.age_increase(1)
    pet.roll_sickness()