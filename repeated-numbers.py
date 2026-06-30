# Dado un array de números, devolver True si algún número aparece al menos dos veces, y False si todos son únicos.
numbers = [4,5,6,3,5,3]

def find_repetitions(numbers):
    return len(numbers) != len(set(numbers))
