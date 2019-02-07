f = open("text.txt")
b = f.read()
f.close()

text = list(b)
slovnik = {}


def znaky(text):
    for znak in text:
        if znak in slovnik:
            slovnik[znak] += 1
        else:
            slovnik[znak] = 1

    slovnik_usporiadany = dict(sorted(slovnik.items(), key=lambda x: x[1], reverse=True))

    zoznam_podla_poctu = []

    for k, v in slovnik_usporiadany.items():
        #print(k, v)
        zoznam_podla_poctu.append(k)

    return zoznam_podla_poctu