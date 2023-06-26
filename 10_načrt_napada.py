def preberi(ime_datoteke) :
    s = []
    d1 = [] #keys
    d2 = [] #values
    d2_sub = []
    for vrstica in open(ime_datoteke.strip(), encoding="utf8"):
        s.append(vrstica)

    for ena in s:
        s_znakov = []
        for znak in ena:
            s_znakov.append(znak)
            if znak == ":":
                key = ("".join(s_znakov))
                key = key.replace(":", "")
                key = key.split(",")
                test = []
                for en in key:
                    test.append(float(en))
                d1.append((tuple((test))))
                s_znakov = []


            if znak == "|":
                values = ("".join(s_znakov))
                values = values.replace("|", "")
                values = values.strip()
                test2 = []
                values = values.split(",")
                for enw in values:
                    test2.append(float(enw))


                d2_sub.append(tuple(test2))
                s_znakov = []

            if znak == "\n":
                values = ("".join(s_znakov))
                values = values.strip()
                test3 = []
                values = values.split(",")
                for en3 in values:
                    test3.append(float(en3))
                d2_sub.append(tuple((test3)))
                d2.append(d2_sub)
                d2_sub = []
                s_znakov = []


    print (f"{d1} \n {d2}")
    slovar = {key:value for key, value in zip(d1, d2)}
    return slovar

def vrstica(i, ladja, marsovec):
    kor1, kor2 =ladja
    mark1, mark2 = marsovec
    if i != None:
        return (f"{i:>4}:{kor1:>11.4f}{kor2:>11.4f} ->{mark1:>11.4f}{mark2:>11.4f}")
    if i == None:
        return (f"{mark1:>41.4f}{mark2:>11.4f}")


def navodila(razpored, ime_datoteke):
    datoteka = open(ime_datoteke, "w")
    i = 1
    i_past = 1
    seznam = []
    for ladja, marsovc  in razpored.items():
        prejsna_ladja = "ladja"
        for en in marsovc:
            print( ladja,prejsna_ladja)
            print(i)
            if prejsna_ladja != ladja and i != None and seznam != []:
                i_past += 1
                prejsna_ladja = ladja
                seznam.append("f")
            i = i_past
            if prejsna_ladja == ladja:
                i = None
            t = vrstica(i, ladja, en)
            datoteka.write(t+ "\n")
            seznam.append("f")










import unittest
import random
import string
import os
import warnings

class Test(unittest.TestCase):
    def setUp(self):
        warnings.simplefilter("ignore", ResourceWarning)

    def test_preberi(self):
        self.assertEqual(
            {(4.25, 8.5): [(5.0, 5.0), (8.125, -7.5), (3.5, -6.75)],
             (6.0, 1.25): [(15.5, 5.5), (1.5, -1.25), (2.5, -9.5625), (-3.0, -3.0)],
             (8.0, 1.0):  [(-2.0, 5.0)]},
            preberi("jozica-kozjanc.txt"))
        try:
            fname = "".join(random.choice(string.ascii_lowercase) for _ in range(8))
            os.rename("jozica-kozjanc.txt", fname)
            self.assertEqual(
                {(4.25, 8.5): [(5.0, 5.0), (8.125, -7.5), (3.5, -6.75)],
                 (6.0, 1.25): [(15.5, 5.5), (1.5, -1.25), (2.5, -9.5625), (-3.0, -3.0)],
                 (8.0, 1.0):  [(-2.0, 5.0)]},
                preberi(fname), "Datoteka ima lahko poljubno ime!")
        finally:
            os.rename(fname, "jozica-kozjanc.txt")

    def test_vrstica(self):
        self.assertEqual("   3:    13.1800    35.5600 ->    75.2000   182.7000",
                         vrstica(3, (13.18, 35.56), (75.2, 182.7)))
        self.assertEqual("                                  75.2000   182.7000",
                         vrstica(None, (13.18, 35.56), (75.2, 182.7)))
        self.assertEqual("   1:  1234.0123 -3456.3457 ->  1234.0123 -3456.3457",
                         vrstica(1, (1234.01234, -3456.34567), (1234.01234, -3456.34567)))
        self.assertEqual("                                1234.0123 -3456.3457",
                         vrstica(None, (1234.01234, -3456.34567), (1234.01234, -3456.34567)))

    def test_navodila(self):
        fname = "".join(random.choice(string.ascii_lowercase) for _ in range(8))
        navodila({(0.248178, 0.316933): [(0.15224490098349647, 0.3027892234548336),
                                         (0.3973177864167832, 0.3654278922345483),
                                         (0.20545151426835478, 0.19569730586370837),
                                         (0.23769794656220833, 0.4038193343898574)],
                  (0.424727, 0.747726): [(0.35862206766415905, 0.8140015847860539),
                                         (0.3408865299025396, 0.6766006339144215),
                                         (0.5069556562158851, 0.6907448494453249),
                                         (0.4069917161049393, 0.7048890649762283),
                                         (0.5101802994452705, 0.8523930269413629)],
                  (0.64884, 0.245202): [(0.6165935260149872, 0.355324881141046),
                                        (0.6020826314827531, 0.18963549920760692),
                                        (0.6730247825292308, 0.22600633914421553),
                                        (0.6182058476296798, 0.26237717908082403),
                                        (0.6826987122173869, 0.14518225039619648),
                                        (0.7004342499790063, 0.2926862123613312)],
                  (0.786425, 0.568835): [(0.8326446223838057, 0.5957765451664025),
                                         (0.8003981900899522, 0.5553645007923931),
                                         (0.7262313958140891, 0.5553645007923931)]},
                 fname)
        self.assertEqual("""
   1:     0.2482     0.3169 ->     0.1522     0.3028
                                   0.3973     0.3654
                                   0.2055     0.1957
                                   0.2377     0.4038
   2:     0.4247     0.7477 ->     0.3586     0.8140
                                   0.3409     0.6766
                                   0.5070     0.6907
                                   0.4070     0.7049
                                   0.5102     0.8524
   3:     0.6488     0.2452 ->     0.6166     0.3553
                                   0.6021     0.1896
                                   0.6730     0.2260
                                   0.6182     0.2624
                                   0.6827     0.1452
                                   0.7004     0.2927
   4:     0.7864     0.5688 ->     0.8326     0.5958
                                   0.8004     0.5554
                                   0.7262     0.5554""".strip("\n"),
                         open(fname).read().strip("\n"))
        os.remove(fname)

        navodila({(1234.23456, -12.44): [(1, 2), (3, 4), (5, 6)]}, fname)
        self.assertEqual("""
   1:  1234.2346   -12.4400 ->     1.0000     2.0000
                                   3.0000     4.0000
                                   5.0000     6.0000""".strip("\n"),
                         open(fname).read().strip("\n"))
        os.remove(fname)

        navodila({(4.25, 8.5): [(5.0, 5.0), (8.125, -7.5), (3.5, -6.75)],
                  (6.0, 1.25): [(15.5, 5.5), (1.5, -1.25), (2.5, -9.5625), (-3.0, -3.0)],
                  (8.0, 1.0):  [(-2.0, 5.0)]}, fname)
        self.assertEqual("""
   1:     4.2500     8.5000 ->     5.0000     5.0000
                                   8.1250    -7.5000
                                   3.5000    -6.7500
   2:     6.0000     1.2500 ->    15.5000     5.5000
                                   1.5000    -1.2500
                                   2.5000    -9.5625
                                  -3.0000    -3.0000
   3:     8.0000     1.0000 ->    -2.0000     5.0000""".strip("\n"),
                         open(fname).read().strip("\n"))
        os.remove(fname)


if __name__ == "__main__":
    unittest.main()
