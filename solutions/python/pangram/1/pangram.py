def is_pangram(sentence):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    pangram = True
    for char in alphabet:
        if char not in sentence.lower():
            pangram = False
    return pangram

            