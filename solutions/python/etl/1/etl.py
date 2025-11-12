def transform(legacy_data):
    dictbaru = {}
    listhuruf = []
    for huruf in legacy_data.values():
        for char in huruf:
            listhuruf.append(char.lower())
    listhuruf = sorted(listhuruf)
    for isi in listhuruf:
        for nilai, huruf2 in legacy_data.items():
            if isi.upper() in huruf2:
                dictbaru[isi] = nilai
    return dictbaru