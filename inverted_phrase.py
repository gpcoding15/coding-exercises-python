
#  * Crea un programa que invierta el orden de una cadena de texto
#  * sin usar funciones propias del lenguaje que lo hagan de forma automática.
#  * - Si le pasamos "Hola mundo" nos retornaría "odnum aloH"

def invert_string(phrase):
    inverted_phrase = ""

    for char in phrase:
        inverted_phrase = char + inverted_phrase
        
    return inverted_phrase
    