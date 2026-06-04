# Dada una lista:

# numbers = [1, 2, 2, 3, 4, 4, 5]

# Retornar:

# [1, 3, 5]

def filter_repeated_numbers(numbers):
    repeated_numbers = []

    for number in numbers:
        if number not in repeated_numbers:
            repeated_numbers.append(number)
    return repeated_numbers