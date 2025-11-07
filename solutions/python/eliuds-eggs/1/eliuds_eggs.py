def egg_count(display_value):
    binary = ""
    while display_value > 0:
        binary = str(display_value % 2) + binary
        display_value = display_value//2
    egg = 0
    for i in binary:
        if i == "1":
            egg += 1
    return egg