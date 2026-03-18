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
    
    def age_increase(self, time):
        self.age += time

    def take_damage(self, amount):
        self.health -= amount
    
    def check_stats(self):
        if self.health < 30 or self.age > 20 or self.mess > 5:
            self.sick_probability += 0.01
        
        if self.hunger > 200:
            self.take_damage(10)

    def print_stats(self):
        print(f"{self.name}'s stats:\nHealth: {self.health} | Hunger: {self.hunger} | Mess: {self.mess} | Hapiness: {self.hapiness} | Age: {self.age} | Sick: {self.is_sick}")

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
        
        elif food_type == "snack":
            self.hunger  = max(self.hunger - 5, 0)
            self.hapiness += 15
            self.health -= 5
        
        print(f"You feed {self.name}")

    def play(self):
        self.hunger += 10
        self.hapiness += 20

        print(f"You play with {self.name}. Look how happy they are!")

pet = Tamagotchi(50, 50, 0, 50, input("What is your pet's name?\n> ").title())

while pet.health > 0:
    pet.print_stats()
    choice = input("What do you want to do? [feed | play]\n> ").lower()

    if choice == "feed":
        pet.feed(input("What do you want to feed your pet? [Food | snacks]\n> "))
    
    elif choice == "play":
        pet.play()