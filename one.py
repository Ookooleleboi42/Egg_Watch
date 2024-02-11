# pet program

from random import randrange
from typing import List


class Pet(object):
    """Virtual Pet"""
    excitement_reduce = 3
    excitement_max = 10
    excitement_warning = 3
    food_reduce = 2
    food_max = 10
    food_warning = 3
    vocab: list[str] = ['"Grrrrr...', '"Hi']

    def __init__(self, name, animal_type):
        self.name = name
        self.animal_type = animal_type
        self.food = randrange(self.food_max)
        self.excitement = randrange(self.excitement_max)
        self.vocab = self.vocab[:]

    def __clock_tick(self):
        self.excitement -= 1
        self.food -= 1

    def mood(self):
        if self.food > self.food_warning and self.excitement_warning:
            return "happy"
        elif self.food < self.food_warning:
            return "hungry"
        else:
            return "bored"

    def __str__(self):
        return "\nI'm" + self.name + "." + "\nIfeel" + self.mood() + "."

    def teach(self, word):
        self.vocab.append(word)
        self.__clock_tick()

    def talk(self):
        print(
            'I am a',
            self.animal_type,
            "named",
            self.name,
            ".",
            "I feel",
            self.mood(),
            " now. \n"
        )
        print(self.vocab[randrange(len(self.vocab))])
        self.__clock_tick()

    def feed(self):
        print("***MUNCH MUNCH MUNCH*** \n mmmm. Thank you!!")
        meal = randrange(self.food, self.food_max)
        self.food += meal

        if self.food < 0:
            self.food = 0
            print("I'm Still Hungry")
        elif self.food > self.food_max:
            self.food = self.food_max
            print("I'm full")
        self.__clock_tick()

    def play(self):
        print("LET'S GOOOOOOO!!!")
        fun: int = randrange(self.excitement, self.excitement_max)
        self.excitement += fun
        if self.excitement < 0:
            self.excitement = 0
            print("This sucks, I'm Bored")
        elif self.excitement > self.excitement_max:
            self.excitement = self.excitement_max
            print("I guess this is cool")
        self.__clock_tick()


def main() -> object:
    pet_name = input("what do you want to name your pet? ")
    pet_type = input("what type of animal is your pet? ")

    my_pet = Pet(pet_name, pet_type)

    input(
        "Hello! I am " +
        my_pet.name +
        " and I am new here!" +
        "\nPress ENTER to start. "
    )
    
    choice = None
    while choice != 0:
        print(
            """
            *** INTERACT WITH YOUR PET***
            1 - FEED YOUR PET
            2 - SPEAK WITH YOUR PET
            3 - TEACH YOUR PET A NEW WORD
            4 - PLAY WITH YOUR PET
            0 - NO INTERACTION
            """
        )
        choice = input("Choice: ")
        if choice  == "0":
            print("Laters bruv")
            
        elif choice == "1" :
            my_pet.feed()
        elif choice == "2":
            my_pet.talk()
        elif choice == "3":
            new_word =input("what word do you want to teach your pet?")
            my_pet.teach(new_word)
        elif choice == "4":
            my_pet.play()
        else:
            print("Yeah that's not a choice, try again")

main()
            
            
        