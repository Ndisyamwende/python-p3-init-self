#!/usr/bin/env python3

class Dog:
    def __init__(self, name, breed="Mutt"):
        self.name = name
        self.breed = breed

my_dog = Dog(name="Buddy", breed="Labrador")
other_dog = Dog(name="Max")

print(f"My dog's name is {my_dog.name} and the breed is {my_dog.breed}")
print(f"Other dog's name is {other_dog.name} and the breed is {other_dog.breed}")
