def delete_duplications(numbers):
    newList = []

    for number in numbers:
        if number not in newList:
            newList.append(number)
    return newList

