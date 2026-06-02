def countWords(text):
    words = text.split(" ")
    words_quantity = {}

    for word in words:
        if word not in words_quantity:
            words_quantity[word] = 1
        else:
            words_quantity[word] += 1
    return words_quantity
