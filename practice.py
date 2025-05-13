# class Animal():
#     def __init__(self, name):
#         self.name = name

#     def display(self):
#         return f"{self.name} has been called"
    
#     def speak(self):
#         return f"{self.name} makes a sound"


# zebra = Animal("Zebra")
# lion = Animal("Lion")
# # print(zebra.display())
# # print(lion.display(),lion.speak())

# class Dog(Animal):
#     def __init__(self, name):
#         super().__init__(name)

#     def speak(self):
#         return f"{self.name} says woof!"

# dog = Dog("Rocky")
# # print(dog.display())
# # print(dog.speak())

# class Cat(Animal):
#     def __init__(self, name):
#         super().__init__(name)

#     def speak(self):
#         return f"{self.name} says meow!"
    
# cat = Cat("Milo")
# # print(cat.display())
# # print(cat.speak())

# animals = [lion, zebra, dog, cat]

# for animal in animals:
#     print(animal.display())
#     print(animal.speak())



import pygame

vector1 = pygame.Vector2(1,0)
vector2 = vector1.rotate(180)
print(vector2)
