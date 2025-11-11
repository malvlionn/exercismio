def roman(number):
    roman = [(1000, "M"), (900, "CM"), (500, "D"), (400, "CD"), (100, "C"), (90, "XC"), (50, "L"), (40, "XL"), (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")]
    hasil = ""
    if number == 0:
        return number
    while number > 0:
        for kocak in roman:
            if kocak[0] <= number:
                jumlah = number//kocak[0]
                hasil += kocak[1] * jumlah
                number -= kocak[0] * jumlah
                break
    return hasil