
class Ninja:
    
    def  __init__(self, first_name, last_name, treats, pet_food, pet):
        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.pet_food = pet_food
        self.pet = pet

    def walk(self):
        self.pet.play()
        return self

    def feed(self):
        self.pet.eat()
        return self

    def bathe(self):
        self.pet.noise()
        return self


class Pet:
    def __init__(self,name, type, tricks, sound):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.sound = sound
        self.health = 0
        self.energy = 0
    
    def sleep(self):
        self.energy += 25
        return self

    def eat(self):
        self.energy += 5
        self.health += 10
        return self

    def play(self):
        self.health += 5
        return self

    def noise(self):
        print(self.sound)
        return self


# class Dog(Pet):
#     def __init__(self, name, type, tricks, sound, coat_type ):
#         super().__init__()(name, type, tricks, sound)
#         self.coat_type = coat_type

#     def play(self):
#         self.noise()
#         super().play()
#         return self

logan = Ninja("Logan", "Domingo", "greenies", "zignature", Pet("Arlo", "dog", "sit", "woof!"))

logan.feed().walk().bathe()




