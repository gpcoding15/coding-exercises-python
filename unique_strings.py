# Given a string, return True if all characters are unique. Otherwise return False.

# Ejemplos:

# "abcde" -> True
# "hello" -> False
# "" -> True
# "a" -> True
# "abca" -> False

def are_chars_unique(word):
    return len(word) == len(set(word))