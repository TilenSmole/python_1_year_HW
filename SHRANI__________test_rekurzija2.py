def  kolikokrat_ime(rodovnik, oseba, ime):
    st = 0
    if ime in oseba:
        st+=  1

    for en in rodovnik[oseba]:
        st += kolikokrat_ime(rodovnik, en, ime)

    return st

def faktoriela(n):

    if n == 0:
        return 1

    return n *  faktoriela(n-1)


def  zensk_v_rodbini(rodovnik, oseba):
    st = 0
    if oseba.split(" ")[0][-1] == "a":
        st += 1
    for potomec in rodovnik[oseba]:
        st += zensk_v_rodbini(rodovnik, potomec)


    return  st

def  najvec_otrok(rodovnik, oseba):
    st = len(rodovnik[oseba])
    for potomec in rodovnik[oseba]:
        if st < najvec_otrok(rodovnik, potomec):
            st = najvec_otrok(rodovnik, potomec)
    return st

def potomstvo(rodovnik, oseba):
    for potomec in rodovnik[oseba]:
        clan |= {potomec}
        clan |= potomstvo(rodovnik, potomec)

    print(clan)
    return clan


import unittest

class TestRekurzija(unittest.TestCase):
    def setUp(self):
        f = open("trgovina.txt", "w")
        f.write("""1;0;Racunalniki
2;0;Monitorji
3;0;Programska oprema
4;1;Prenosniki
5;1;Namizni racunalniki
6;1;Strezniki
7;3;Operacijski sistemi
8;3;Solske licence
9;3;Antivirusni programi
10;4;Prenosniki
11;4;Netbooki
""")
        f.close()

        self.slovar_izdelkov = {'0': {('1', 'Racunalniki'), ('2', 'Monitorji'), ('3', 'Programska oprema')},
                                '1': {('4', 'Prenosniki'), ('5', 'Namizni racunalniki'), ('6', 'Strezniki')},
                                '3': {('7', 'Operacijski sistemi'), ('8', 'Solske licence'),
                                      ('9', 'Antivirusni programi')},
                                '4': {('10', 'Prenosniki'), ('11', 'Netbooki')}}

        self.rodovnik = {'Ulrik I.': ['Viljem'], 'Margareta': [], 'Herman I.':
            ['Herman II.', 'Hans'], 'Elizabeta II.': [], 'Viljem': ['Ana Poljska'],
            'Elizabeta I.': [], 'Ana Poljska': [], 'Herman III.': ['Margareta'],
            'Ana Ortenburška': [], 'Barbara': [], 'Herman IV.': [], 'Katarina': [],
            'Friderik III.': [], 'Herman II.': ['Ludvik', 'Friderik II.', 'Herman III.',
            'Elizabeta I.', 'Barbara'], 'Ulrik II.': ['Herman IV.', 'Jurij',
            'Elizabeta II.'], 'Hans': [], 'Ludvik': [], 'Friderik I.': ['Ulrik I.',
            'Katarina', 'Herman I.', 'Ana Ortenburška'], 'Friderik II.': ['Friderik III.',
            'Ulrik II.'], 'Jurij': []}

    def test_najvec_otrok(self):
        self.assertEqual(najvec_otrok(self.rodovnik, 'Friderik I.'), 5)
        self.assertEqual(najvec_otrok(self.rodovnik, 'Friderik II.'), 3)
        self.assertEqual(najvec_otrok(self.rodovnik, 'Ulrik I.'), 1)
        self.assertEqual(najvec_otrok(self.rodovnik, 'Jurij'), 0)
        self.assertEqual(najvec_otrok(self.rodovnik, 'Ulrik II.'), 3)

    def test_zensk_v_rodbnin(self):
        self.assertEqual(zensk_v_rodbini(self.rodovnik, "Friderik II."), 1)
        self.assertEqual(zensk_v_rodbini(self.rodovnik, "Ulrik I."), 1)
        self.assertEqual(zensk_v_rodbini(self.rodovnik, "Ludvik"), 0)
        self.assertEqual(zensk_v_rodbini(self.rodovnik, "Friderik I."), 7)
        self.assertEqual(zensk_v_rodbini(self.rodovnik, "Katarina"), 1)

    def test_kolikokrat_ime(self):
        self.assertEqual(kolikokrat_ime(self.rodovnik, "Friderik I.", "Friderik"), 3)
        self.assertEqual(kolikokrat_ime(self.rodovnik, "Friderik II.", "Friderik"), 2)
        self.assertEqual(kolikokrat_ime(self.rodovnik, "Barbara", "Friderik"), 0)
        self.assertEqual(kolikokrat_ime(self.rodovnik, "Barbara", "Barbara"), 1)
        self.assertEqual(kolikokrat_ime(self.rodovnik, "Herman I.", "Barbara"), 1)
        self.assertEqual(kolikokrat_ime(self.rodovnik, "Herman I.", "Francelj"), 0)

    def test_faktoriela(self):
        self.assertEqual(faktoriela(0), 1)
        self.assertEqual(faktoriela(1), 1)
        self.assertEqual(faktoriela(5), 120)
        self.assertEqual(faktoriela(20), 2432902008176640000)
        self.assertEqual(faktoriela(21), 51090942171709440000)

    def test_potomstvo(self):
        self.assertEqual(potomstvo(self.rodovnik, "Friderik II."),
                         {"Friderik III.", "Ulrik II.", "Herman IV.", "Jurij", "Elizabeta II."})
        self.assertEqual(potomstvo(self.rodovnik, "Ulrik I."), {"Viljem", "Ana Poljska"})
        self.assertEqual(potomstvo(self.rodovnik, "Ludvik"), set())
        self.assertEqual(potomstvo(self.rodovnik, "Herman III."), {"Margareta"})



'''    def test_preberi_izdelke(self):
        self.assertDictEqual(preberi_izdelke('trgovina.txt'), self.slovar_izdelkov)

    def test_seznam_podizdelkov(self):
        self.assertEqual(seznam_izdelkov(self.slovar_izdelkov), [
            'Monitorji',
            'Programska oprema',
            'Programska oprema / Antivirusni programi',
            'Programska oprema / Operacijski sistemi',
            'Programska oprema / Solske licence',
            'Racunalniki',
            'Racunalniki / Namizni racunalniki',
            'Racunalniki / Prenosniki',
            'Racunalniki / Prenosniki / Netbooki',
            'Racunalniki / Prenosniki / Prenosniki',
            'Racunalniki / Strezniki'])

    def test_seznam_koncnih(self):
        self.assertEqual(seznam_koncnih(self.slovar_izdelkov), [
            'Monitorji',
            'Programska oprema / Antivirusni programi',
            'Programska oprema / Operacijski sistemi',
            'Programska oprema / Solske licence',
            'Racunalniki / Namizni racunalniki',
            'Racunalniki / Prenosniki / Netbooki',
            'Racunalniki / Prenosniki / Prenosniki',
            'Racunalniki / Strezniki'])'''

if __name__ == '__main__':
    unittest.main(verbosity=2)
