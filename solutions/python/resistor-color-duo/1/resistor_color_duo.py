warnanyakocak = ["black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white"]
def value(colors):
    hasileak = ""
    for warna in colors[:2]:
        hasileak += str(warnanyakocak.index(warna))
    return int(hasileak)
