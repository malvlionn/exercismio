def commands(binary_str):
    kerjaan = []
    gerakan = ["reverse", "jump", "close your eyes", "double blink", "wink"]
    while len(binary_str) < 5:
        binary_str = "0" + binary_str
    i = 0
    if binary_str[0] == "1":
        for bin in binary_str[1:]:
            if bin == "1":
                kerjaan.append(gerakan[i+1])
            i+= 1
        return kerjaan
    else:
        for bin in binary_str:
            if bin == "1":
                kerjaan.append(gerakan[i])
            i+= 1
    return kerjaan[::-1]
