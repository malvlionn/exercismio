def sum_of_multiples(limit, multiples):
    gabungan = []
    jawaban = 0
    if len(multiples) == 0:
        return 0
    else:
        for kanan in multiples:
            if kanan == 0:
                continue
            atiati = kanan
            pisahan = []
            while atiati < limit:
                pisahan.append(atiati)
                atiati += kanan
            gabungan += pisahan
    for item in set(gabungan):
        jawaban += item
    return jawaban