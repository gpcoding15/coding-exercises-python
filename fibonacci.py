
#  * Escribe un programa que imprima los 50 primeros números de la sucesión
#  * de Fibonacci empezando en 0.
#  * - La serie Fibonacci se compone por una sucesión de números en
#  *   la que el siguiente siempre es la suma de los dos anteriores.
#  *   0, 1, 1, 2, 3, 5, 8, 13...


def show_fibonacci_succesion():
 max_numbers = 50
 number_counter = 2

 previous_number_1 = 0
 print(previous_number_1)

 previous_number_2 = 1
 print(previous_number_2)

 while number_counter < max_numbers:
    next_number = previous_number_1 + previous_number_2
    print(next_number)

    previous_number_1 = previous_number_2
    previous_number_2 = next_number
    number_counter += 1
 