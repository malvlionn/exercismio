def recite(start_verse, end_verse):
    hadiah = ("twelve Drummers Drumming","eleven Pipers Piping","ten Lords-a-Leaping","nine Ladies Dancing","eight Maids-a-Milking","seven Swans-a-Swimming","six Geese-a-Laying","five Gold Rings","four Calling Birds","three French Hens","two Turtle Doves", "and a Partridge in a Pear Tree.")
    hari = ("first", "second", "third", "fourth", "fifth", "sixth", "seventh", "eighth", "ninth", "tenth", "eleventh", "twelfth")
    hasil = []
    for kocak in range(start_verse-1, end_verse):
        awalan = f"On the {hari[kocak]} day of Christmas my true love gave to me: "
        if kocak == 0:
            awalan += "a Partridge in a Pear Tree."
        else:
            awalan += ", ".join(hadiah[-(kocak+1):])
        hasil.append(awalan)
    return hasil