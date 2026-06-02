# text = "python"

# Salida:

# "nohtyp"

def invert_string(text):
    inverted_string = ""

    for letter in text[::-1]:
        inverted_string += letter
    return inverted_string
