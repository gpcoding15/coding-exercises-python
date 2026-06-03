# Ejercicio 5 - Palabras únicas

# Entrada:

# words = ["ana", "juan", "ana", "pedro", "juan"]

# Salida:

# ["ana", "juan", "pedro"]

def filter_unique_words(words):
    unique_words = []

    for word in words: 
        if word not in unique_words:
            unique_words.append(word)

    return unique_words