def find(search_list, value):
    final = sorted(search_list)
    kiri, kanan = 0, len(final) - 1

    if value not in search_list:
        raise ValueError("value not in array")
    else:
        while kiri <= kanan:
            tengah = (kiri + kanan) // 2
            
            if final[tengah] == value:
                return tengah
            elif final[tengah] < value:
                kiri = tengah + 1
            else:
                kanan = tengah - 1