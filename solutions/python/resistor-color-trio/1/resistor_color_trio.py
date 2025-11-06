warnanyakocak = ["black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white"]
def label(colors):
    hasileak = ""
    for i in colors[:2]:
        hasileak += str(warnanyakocak.index(i))
    if hasileak[0] == "0":
        hasileak = hasileak[1] + "0" * warnanyakocak.index(colors[2])
    else:
        hasileak += "0" * warnanyakocak.index(colors[2])
    if hasileak[:2] == "00":
        hasileak = "0 ohms"
    elif hasileak[-9:] == "0" * 9:
        hasileak = hasileak[:-9] + " gigaohms"
    elif hasileak[-6:] == "0" * 6:
        hasileak = hasileak[:-6] + " megaohms"
    elif hasileak[-3:] == "0" * 3:
        hasileak = hasileak[:-3] + " kiloohms"
    else:
        hasileak = hasileak + " ohms"
    return hasileak