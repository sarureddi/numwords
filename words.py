value=int(input("enter the number from 1-9 seperated by commmos"))
def user_input(value):
    numbers = {}
    user_list = value.split(',')
    numbers = [(x.strip()) for x in user_list]
    return numbers
    print(numbers)

user_input(value)

numbers = user_input()

unit_number = {0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 
           5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine'}

def convert_n_to_w(numbers):
    i = len(str(numbers))

    if i == 0:
        return

    if i == 1:
        return unit_number[numbers]

    print(unit_number[numbers])
