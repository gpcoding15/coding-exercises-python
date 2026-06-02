# Ejercicio 2 (10 min)

# Verificar si una palabra es palíndromo.

# Entrada:

# "radar"

# Salida:

# True

# Entrada:

# "python"

def verify_equality(word):
    word_on_reverse = []

    for letter in word[::-1]:
        word_on_reverse.append(letter)
    
    reversed_word ="".join(word_on_reverse)

    return reversed_word == word


