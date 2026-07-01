
#  * Crea un programa que cuente cuantas veces se repite cada palabra
#  * y que muestre el recuento final de todas ellas.
#  * - Los signos de puntuación no forman parte de la palabra.
#  * - Una palabra es la misma aunque aparezca en mayúsculas y minúsculas.
#  * - No se pueden utilizar funciones propias del lenguaje que
#  *   lo resuelvan automáticamente.
import re

def count_repeated_words(phrase):
    words = re.split(r"[,.!?¿¡;:\s]+", phrase)
    repetitions = {}

    for word in words:
       if word != "":
        lower_word =  word.lower()
        if lower_word not in repetitions:
            repetitions[lower_word] = 1
        else:
            repetitions[lower_word] +=1

    return repetitions

repetitions = count_repeated_words("hola si hola dije hola todo bien si")
print(repetitions)


       