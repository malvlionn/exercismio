"""Functions to help Azara and Rui locate pirate treasure."""

def get_coordinate(record):
    return record[1]

def convert_coordinate(coordinate):
    return tuple(coordinate)

def compare_records(azara_record, rui_record):
    return tuple(azara_record[1]) == rui_record[1]

def create_record(azara_record, rui_record):
    if tuple(azara_record[1]) == rui_record[1]:
        return azara_record + rui_record
    return "not a match"

def clean_up(combined_record_group):
    hasileak = []
    for tupel in combined_record_group:
        jadilist = list(tupel)
        jadilist.remove(jadilist[1])
        hasileak.append(tuple(jadilist))
    formatted = "\n".join(map(str, hasileak)) + "\n"
    return formatted