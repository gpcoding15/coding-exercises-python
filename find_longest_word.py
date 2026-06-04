# Dada una lista:

# words = ["react", "python", "sql", "javascript"]

# Retornar:

# "javascript"

# La palabra más larga.

def find_longest_word(words):
    len_longest_word = len(words[0])
    longest_word = words[0]

    for word in words:
        if len(word) > len_longest_word:
            longest_word = word
    return longest_word
