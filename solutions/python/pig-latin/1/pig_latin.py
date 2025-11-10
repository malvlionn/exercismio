def translate(text):
    vowel = "aiueo"
    if len(text.split()) == 1:
        if text[0] in vowel or text[0:2] == "xr" or text[0:2] == "yt":
            return text + "ay"
        if text[0] not in vowel:
            matijir = ""
            masibagus = ""
            for index, char in enumerate(text):
                if char == "q" and text[index+1] == "u":
                    matijir += "qu"
                    masibagus += str(text[(index+2):])
                    break
                if char not in vowel and text[index+1] == "y":
                    matijir += char
                    masibagus += str(text[(index+1):])
                    break
                if char not in vowel:
                    matijir += char
                else:
                    masibagus += str(text[index:])
                    break
            hasilakhir = masibagus + matijir + "ay"
            return hasilakhir
    else:
        jawabanakhir = []
        salahkocak = text.split()
        for word in salahkocak:
            if word[0] in vowel or word[0:2] == "xr" or word[0:2] == "yt":
                jawabanakhir.append(word + "ay")
            if word[0] not in vowel:
                matijir = ""
                masibagus = ""
                for index, char in enumerate(word):
                    if char == "q" and word[index+1] == "u":
                        matijir += "qu"
                        masibagus += str(word[(index+2):])
                        break
                    if char not in vowel and word[index+1] == "y":
                        matijir += char
                        masibagus += str(word[(index+1):])
                        break
                    if char not in vowel:
                        matijir += char
                    else:
                        masibagus += str(word[index:])
                        break
                jawabanakhir.append(masibagus + matijir + "ay")
        return " ".join(jawabanakhir)