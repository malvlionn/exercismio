alphabet = "abcdefghijklmnopqrstuvwxyz"
digit = "1234567890"

def encode(plain_text):
    hasilnyajir = ""
    perkatajir = 0
    for char in plain_text.lower():
        if perkatajir < 5:
            if char in alphabet:
                hasilnyajir += alphabet[-1 * (alphabet.index(char)+1)]
                perkatajir += 1
            elif char in digit:
                hasilnyajir += char
                perkatajir += 1
        if perkatajir == 5:
            hasilnyajir += " "
            perkatajir = 0
    return hasilnyajir.strip()

def decode(ciphered_text):
    result = ""
    for i in ciphered_text.lower():
        if i in alphabet:
            result += alphabet[-1 * (alphabet.index(i)+1)]
        elif i in digit:
            result += i
    return result
