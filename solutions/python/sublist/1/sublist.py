"""This exercise stub and the test suite contain several enumerated constants."""

EQUAL = 1
UNEQUAL = 2
SUBLIST = 3
SUPERLIST = 4

def sublist(list_one, list_two):
    if len(list_one) == 0 and len(list_two) == 0:
        return EQUAL
        
    if len(list_two) == 0:
        return SUPERLIST
        
    if len(list_one) == 0:
        return SUBLIST
        
    if len(list_one) == len(list_two):
        for i in range(len(list_one)):
            if list_one[i] != list_two[i]:
                return UNEQUAL
        return EQUAL
        
    if len(list_one) < len(list_two):
        stringsatu = []
        stringdua = []
        for i in list_one:
            stringsatu.append(str(i))
        for e in list_two:
            stringdua.append(str(e))
        strsatu = ",".join(stringsatu)
        strdua = ",".join(stringdua)
        if strsatu in strdua:
                return SUBLIST
        return UNEQUAL
        
    if len(list_one) > len(list_two):
        stringsatu = []
        stringdua = []
        for i in list_one:
            stringsatu.append(str(i))
        for e in list_two:
            stringdua.append(str(e))
        strsatu = ",".join(stringsatu)
        strdua = ",".join(stringdua)
        if strdua in strsatu:
                return SUPERLIST
        return UNEQUAL
    
    