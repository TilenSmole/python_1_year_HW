zacetki = [3, 12, 11, 8]
potek = [(-1, 'a'), (15, 'n'), (10, 'a'), (1, 'A'), (9, 'l'), (4, 'i'), (-1, 'a'), (6, 't'),
         (2, 'D'), (0, 'k'), (16, 'n'), (5, 'C'), (14, 'B'), (7, 'r'), (13, 'e'), (-1, 'a'), (-1, 'i')]


st1 = 0
besedilo = []
str = ""
ime = []

for začetek in zacetki:
    indeks = potek[začetek]
    for haha in potek:
        if st1 != -1:
            st1, crka = indeks
            crka1 = crka
            ime.append(crka1)
            indeks = potek[st1]
            imena_real = "".join(ime)
    besedilo.append(imena_real)

    if st1 == -1:
        st1 = 0
        ime = []

print(besedilo)



