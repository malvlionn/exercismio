def is_isogram(string):
    uniquestring = []
    isogram = True
    loweredstring = string.lower()
    for char in loweredstring:
        if char.isalpha():
            if char not in uniquestring:
                uniquestring.append(char)
            else:
                isogram = False
        else:
            continue
    return isogram
