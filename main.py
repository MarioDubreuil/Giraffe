# ex 1

# full_name = 'John Smith'
# age = 20
# is_new_patient = True
# print(full_name)
# print(age)
# print(is_new_patient)

# ex 2

# name = input('What is your name? ')
# color = input('What is your favourite color? ')
# print(name + ' likes ' + color)

# ex 3

# weight_lbs = input('Enter your weight in lbs: ')
# weight_kg = int(weight_lbs) / 2.205
# print('Your weight in kg is ' + str(weight_kg))

# ex 4

# good_credit = True
# price = 1_000_000
# if good_credit:
#     percentage = .1
# else:
#     percentage = .2
# down_payment = price * percentage
# print(down_payment)

# ex 5

# name = input('Name: ')
# name_length = len(name)
# if name_length < 3:
#     print('Name must be at least 3 characters')
# elif name_length > 50:
#     print('Name must not be greater than 50 characters')
# else:
#     print('Name looks good!')

# ex 6

# original_weight = input('Weight: ')
# lbs_or_kg = input('(L)bs or (K)g: ')
# if lbs_or_kg.upper() == 'L':
#     converted_weight = round(int(original_weight) / 2.205, 1)
#     print(f'You are {converted_weight} kilos')
# else:
#     converted_weight = round(int(original_weight) * 2.205, 1)
#     print(f'You are {converted_weight} lbs')

# ex 7

# car_started = False
# while True:
#     command = input('>').lower()
#     if command == 'quit':
#         break
#     if command == 'start':
#         if car_started:
#             print('Car is already running!')
#         else:
#             car_started = True
#             print('Car started...Ready to go!')
#     elif command == 'stop':
#         if not car_started:
#             print('Car is not running!')
#         else:
#             car_started = False
#             print('Car stopped.')
#     elif command == 'help':
#         print('start - to start the car')
#         print('stop - to stop the car')
#         print('quit - to quit')
#     else:
#         print('I don\'t understand that...')

# ex 8

# item_cost_list = [10, 20, 30]
# total = 0
# for item_cost in item_cost_list:
#     total += item_cost
# print(total)

# ex 9

# numbers = [2, 2, 2, 2, 5]
# for number in numbers:
#     x = ""
#     for i in range(number):
#         x += "X"
#     print(x)

# ex 10

# numbers = [7, 3, 2, 4, 8, 3]
# max_number = numbers[0]
# for number in numbers:
#     if number > max_number:
#         max_number = number
# print(max_number)

# ex 11

# numbers = [5, 2, 1, 7, 4, 1, 1, 1, 7, 3]
# unique_numbers = []
# for number in numbers:
#     if number not in unique_numbers:
#         unique_numbers.append(number)
# print(numbers)
# print(unique_numbers)

# ex 12

# translate = {
#     "0": "Zero",
#     "1": "One",
#     "2": "Two",
#     "3": "Three",
#     "4": "Four",
#     "5": "Five",
#     "6": "Six",
#     "7": "Seven",
#     "8": "Eight",
#     "9": "Nine",
# }
# phone = input('Phone: ')
# output = ""
# for digit in phone:
#     output += " " + translate.get(digit, "?")
# print(output[1:])

# ex 13

# emojis = {
#     ":)": "😀",
#     ":(": "😩",
#     ";)": "😜"
# }
# message = input('>')
# words = message.split(' ')
# output = ''
# for word in words:
#     output += ' ' + emojis.get(word, word)
# print(output[1:])

# ex 14

# def translate_emojis(message):
#     emojis = {
#         ":)": "😀",
#         ":(": "😩",
#         ";)": "😜"
#     }
#     words = message.split(' ')
#     output = ''
#     for word in words:
#         output += ' ' + emojis.get(word, word)
#     return output[1:]
#
#
# print(translate_emojis('simple text'))
# print(translate_emojis('hello world :)'))
# print(translate_emojis(';) hello :( world :)'))

# ex 15

# class Person:
#     def __init__(self, name):
#         self.name = name
#
#     def talk(self):
#         print(f'Hello {self.name}')
#
#
# steve = Person('Steve')
# steve.talk()
#
# mike = Person('Mike')
# mike.talk()

# ex 16

# class Mammal:
#     def walk(self):
#         print('walk')
#
#
# class Dog(Mammal):
#     def bark(self):
#         print('bark')
#
#
# class Cat(Mammal):
#     def be_annoying(self):
#         print('annoying')
#
#
# fido = Dog()
# fido.walk()
# fido.bark()
# silvester = Cat()
# silvester.walk()
# silvester.be_annoying()

# ex 17

# import converters
# from converters import kg_to_lbs
#
# print(converters.lbs_to_kg(160))
# print(converters.kg_to_lbs(72))
# print(kg_to_lbs(72))

# ex 18

# from utils import find_max
# print(find_max([7, 3, 2, 4, 8, 3]))

# ex 19

# import ecommerce.shipping
# from ecommerce import shipping
# from ecommerce.shipping import calc_shipping
#
# ecommerce.shipping.calc_shipping()
# shipping.calc_shipping()
# calc_shipping()

# ex 20

# import random
#
#
# class Dice:
#     def roll(self):
#         return random.randint(1, 6), random.randint(1, 6)
#
#
# print(Dice().roll())

# ex 21

# from pathlib import Path
#
# path = Path()
# for file in path.glob('*.py'):
#     print(file)
