
#     Your task is to create slightly different animals, which should have the same properties and methods,
# but should implement the talk() method in different ways. For example.
# should a cat (when talking) say "Moew", a dog "Woff", a fish "Blub" and a Cow "Muuu".
# They should all share the following (private) properties: name (string), age (number),
# food (list of strings), and have the functions get_name, set_name, get_age, set_age, get_food,
# add_food, remove_food. Finally, all the animals must have the talk function, but that function must, 
# as I said, be implemented in each animal, as the animals have different sounds.

# When you have made the classes, create instances of the classes and put in a 
# list - loop through the list - and let all the animals talk! :)

import winsound

class Animal:
    
    def __init__(self) -> None:
        self.__name = None
        self.__age = None
        self.__food = list()
    
    def get_name(self):
        if self.__name:
            return self.__name
        return "Name not set!"
    
    def set_name(self, name: str):
        if self.__name:
            self.__name = name
            return f"Name changed from {self.__name} to {name}"
            
        self.__name = name
            
            
    def set_age(self, age):
        if self.__age:
            self.__age = age
            return f"Age changed from {self.__age} to {age}"
        
        self.__age = age
        
    def get_age(self):
        if self.__age:
            return self.__age
        else:
            return "Age not set!"
    
    def add_food(self, item):
        self.__food.append(item)
    
    def remove_food(self, item=None):

        if not len(self.__food) == 0:
            if not item == None:
                self.__food.remove(item)
            self.__food.pop()
            
        return "No food item in list"
    
    def get_food(self):
        if not (self.__food) == 0:
            return self.__food
        
        return "No foods available"
    

class Dog(Animal):
    
    def __init__(self):
        Animal().__init__()
        
    def talk(self):
        # winsound.PlaySound(dog, winsound.SND_FILENAME)
        print("Dog says BOOOO!!!")
        
class Cat(Animal):
    def __init__(self):
        Animal().__init__() 
        
    def talk(self):
        # winsound.PlaySound(cat, winsound.SND_FILENAME)
        print("Cat says MEOOWWW!")
        
class Cow(Animal):
    def __init__(self):
        Animal().__init__()
        
    def talk(self):
        # winsound.PlaySound(cow, winsound.SND_FILENAME)
        print("Cow says MOOO")
        
dog = Dog()
cat = Cat()
cow = Cow()

animals = [dog, cat, cow]

for animal in animals:
    animal.talk()
    
    

            
                