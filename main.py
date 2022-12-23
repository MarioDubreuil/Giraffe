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

# has_good_credit = True
# price = 1_000_000
# if has_good_credit:
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
