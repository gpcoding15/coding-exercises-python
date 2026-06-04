# Dado un texto:

# text = "hola hola mundo hola mundo"

# Retornar:

# "hola"

# La palabra que más veces aparece.

def find_most_repeated_word(words):
    repetitions = {}

    for word in words:
        if word not in repetitions:
            repetitions[word] = 1
        else:
            repetitions[word] += 1
    
    most_repeated_word = list(repetitions.keys())[0]
    
    for word in list(repetitions.keys()):
        if repetitions[word] > repetitions[most_repeated_word]:
            most_repeated_word = word
    return most_repeated_word