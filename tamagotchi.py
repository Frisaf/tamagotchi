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

        self.discipline = 0
        self.sick_probability = 0

        self.has_played = False
        self.been_fed = False
    
    # ====== BACKGROUND METHODS ====== #
    
    def age_increase(self, time):
        self.age += time

    def take_damage(self, amount):
        self.health -= amount
    
    def check_stats(self):
        if self.health < 30 or self.age > 20 or self.mess > 30:
            self.sick_probability += 0.01
        
        if self.hunger > 200:
            print(f"{self.name} is really hungry... They will start to take damage unless fed enough!")
            self.take_damage(10)
        
        if self.health <= 0:
            self.die()
            return
        
        if self.is_sick:
            print(
                "========================\n"+
                f"{self.name.upper()} IS SICK!\n"+
                "They will become unhappy and less healthy unless treated.\n"+
                "========================"
            )
            self.hapiness -= 10
            self.health -= 5
        
        self.has_played = False
        self.been_fed = False
        self.hapiness -= 5 if self.has_played == False else 0
        self.hunger += 5 if self.been_fed == False else 0

    def print_stats(self):
        print(f"{self.name}'s stats:\nHealth: {self.health} | Hunger: {self.hunger} | Mess: {self.mess} | Hapiness: {self.hapiness} | Age: {self.age} | Discipline: {self.discipline} | Sick: {self.is_sick}")

        if self.is_sick or self.hunger > 150:
            print("(O ~ O)")
        
        elif self.hapiness < 30 or self.health < 30:
            print("(O ∩ O)")
        
        elif self.hapiness > 100:
            print("(=^v^=)")
        
        else:
            print("(° - °)")

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
        
        elif option.lower() not in ("food", "snacks"):
            print(f"{option} is not an option.")
            return
        
        roll = random.randint(1, self.discipline + (10 if self.discipline <= 3 else 0))

        if self.discipline <= 5 and roll >= self.discipline:
            input(f"{self.name} refuses to eat. Press ENTER to discipline!")

            if not self.train(True):
                return print(f"{self.name} did not eat anything.")
        
        food_type = option.lower()

        if food_type == "food":
            self.hunger = max(self.hunger - 10, 0)
            self.hapiness += 5
            self.health += 5
        
        elif food_type == "snacks":
            self.hapiness += 30
            self.health -= 5
        
        self.mess += 10
        self.been_fed = True
        
        print(f"You feed {self.name}")

    def play(self):
        trivia = [
            {
                "question": "Is the earth flat?",
                "answers": ["no", "nope", "n", "nah"]
            },
            {
                "question": "Who is the bestest pet?",
                "answers": ["you"]
            },
            {
                "question": "Am I adopted?",
                "answers": ["yes", "no", "maybe"]
            },
            {
                "question": "Can I have some food pwease...",
                "answers": ["maybe"]
            }
        ]

        trivia_dict = random.choice(trivia)
        answer = input(trivia_dict["question"] + "\n> ")

        if answer not in trivia_dict["answers"]:
            return print(f"You try to play with {self.name}, but they don't have the energy.")

        self.hapiness += 20
        self.has_played = True

        print(f"You play with {self.name}. Look how happy they are!")
    
    def die(self):
        print(f"{self.name} died at age {self.age}. RIP ☠️")
    
    def give_meds(self):
        print(f"You give {self.name} their meds. They feel better!")

        self.is_sick = False
        self.sick_probability -= 0.1
    
    def train(self, discipline = False):
        if self.age > 20 and not discipline:
            return print(f"{self.name} is old and is too tired to learn something new.")
        
        if discipline:
            if random.randint(1, 10) >= 3:
                self.discipline += 1
                return discipline
            
            else:
                return False
        
        print(f"You train with {self.name}. They learned a new trick!")

        self.discipline += 1
        self.hunger += 20

pet = Tamagotchi(50, 10, 0, 50, input("What is your pet's name?\n> ").title())

while pet.health > 0:
    pet.print_stats()

    meds_option = " | meds" if pet.is_sick == True else ""
    choice = input(f"What do you want to do? [feed | play | clean | train{meds_option}]\n> ").lower()

    if choice in ["feed", "f"]:
        pet.feed(input("What do you want to feed your pet? [Food | snacks]\n> "))
        been_fed = True
    
    elif choice in ["play", "p"]:
        pet.play()
    
    elif choice in ["clean", "c"]:
        pet.clean()
    
    elif choice in ["train", "t"]:
        pet.train()
    
    elif choice in ["meds", "m"] and pet.is_sick:
        pet.give_meds()
    
    else:
        print("Your pet looks at you, puzzled. Time passes...")
    
    pet.check_stats()
    pet.age_increase(1)
    pet.roll_sickness()