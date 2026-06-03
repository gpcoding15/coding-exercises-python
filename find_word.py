# Ejercicio 3 - Encontrar palabras que empiezan con una letra

# Entrada:

# words = ["ana", "juan", "pedro", "alberto"]
# letter = "a"

# Salida:

# ["ana", "alberto"]

def find_word_starting_with_letter(words, letter):
    words_matching = []
    for word in words:
        if letter == word[0]:
            words_matching.append(word)
    return words_matching