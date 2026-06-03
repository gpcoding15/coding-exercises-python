# numbers = [10, 5, 20, 15]

# Salida:

# 15

def find_second_biggest_number(numbers):
    biggest_number = numbers[0]

    for number in numbers:
        if number > biggest_number:
            biggest_number = number
    
    numbers.remove(biggest_number)

    second_biggest_number = numbers[0]

    for number in numbers:
        if number > second_biggest_number:
            second_biggest_number = number
    return second_biggest_number