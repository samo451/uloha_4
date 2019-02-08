def znaky(text):
    """
    Na vstupe sa vkladá zoznam znakov, získaný z textu. Následne pridá každý znak do slovníka aj s odpovedajúcou hodnotou,
    koľko krát sa daný znak vyskytuje v danom zozname. Následne pomocou počtu je usporiadaný slovník a funkcia vracia
    zoznam znakov usporiadaný podľa početnosti výskytu, od najviac sa vyskytujúci znak, po najmenej.
    """
    slovnik = {}
    for znak in text:
        if znak in slovnik:
            slovnik[znak] += 1
        else:
            slovnik[znak] = 1
    slovnik_usporiadany = dict(sorted(slovnik.items(), key=lambda x: x[1], reverse=True))
    zoznam_podla_poctu = []
    for k, v in slovnik_usporiadany.items():
        zoznam_podla_poctu.append(k)
    return zoznam_podla_poctu

def tvorba_zoznamu_znakov():
    """
    Pomocou uživateľom zadaného textového vstupu vytvára zoznam znakov, ktorý vracia.
    V prípade nesprávne zadaného vstupu končí program s chybou.
    """
    filename = input("Zvoľte súbor: ")
    try:
        f = open(filename)
    except:
        print("Súbor nenájdený/Nesprávne vložený súbor/Súbor neexistuje")
        quit(1)
    b = f.read()
    f.close()
    return list(b)

print(znaky(tvorba_zoznamu_znakov()))
