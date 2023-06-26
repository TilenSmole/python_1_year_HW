def v_zaporedje(signal):

    v0 = signal.replace("---", "d")
    v2 = v0.replace("-", ".")

    v3 = v2.replace("d ", "-")
    v4 = v3.replace(". ", ".")
    v10 = v4.replace("      ", "   ")
    v5 = v10.replace("  ", " ")
    return  v5

def vrni_znak(zaporedje, abeceda, morse):
    for m_crka in (morse):
        if m_crka == zaporedje:
            m_crka = m_crka
            break
    for i in (morse):
        indeks_crke = morse.index(m_crka)
    for st, crka in enumerate(abeceda):
        if st == indeks_crke:
            return (crka)

def v_besedo(zaporedje, abeceda, morse):
    s = []
    for x in zaporedje.split(" "):
        niz = vrni_znak(x, abeceda, morse)
        s.append(niz)
    s = "".join(s)
    return  (s)

def v_znake(zaporedje, abeceda, morse):
    seznam_besed = []
    for y in zaporedje.split("   "):
        niz_znakov = v_besedo(y, abeceda, morse)
        seznam_besed.append(niz_znakov)
    seznam_besed = " ".join(seznam_besed)

    return (seznam_besed)

def preberi(signal, abeceda, morse):
    pretvorba = v_zaporedje(signal)

    koncno= v_znake(pretvorba, abeceda, morse)

    return (koncno)


import unittest
import random


class Test(unittest.TestCase):
    eng = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    #           A      B       C      D      E     F      G        H      I
    eng_mor = ['.-', '-...', '-.-.', '--.', '.', '..-.', '--.', '....', '..',
               #             J      K       L     M     N      O      P       Q       R
               '.---', '-.-', '.-..', '--', '-.', '---', '.--.', '--.-', '.-.',
               #             S    T     U      V       W       X       Y      Z
               '...', '-', '..-', '...-', '.--', '-..-', '-.--', '--..']

    slo = "ABCČDEFGHIJKLMNOPRSŠTUVZŽ"
    #           A      B       C       Č       D      E     F      G        H
    slo_mor = ['.-', '-...', '-.-.', '-.--.', '--.', '.', '..-.', '--.', '....',
               #  I     J      K       L     M     N      O      P        R
               '..', '.---', '-.-', '.-..', '--', '-.', '---', '.--.',  '.-.',
               #  S     Š       T     U      V      Z       Ž
               '...', '---.-', '-', '..-', '...-', '--..', '--..-']


class TestObvezna(Test):
    def test_01_v_zaporedje(self):
        self.assertEqual(
            "..-. .-. ..   ..- .-..",
            v_zaporedje("- - --- -   - --- -   - -      - - ---   - --- - -"))

        self.assertEqual(
            "...- ... ---.-   ..-. .-. ..   ..- .-..",
            v_zaporedje("- - - ---   - - -   --- --- --- - ---      - - --- -   - --- -   - -      - - ---   - --- - -"))

    def test_02_vrni_znak(self):
        self.assertEqual("A", vrni_znak(".-", self.eng, self.eng_mor))
        self.assertEqual("Y", vrni_znak("-.--", self.eng, self.eng_mor))
        self.assertEqual("Č", vrni_znak("-.--.", self.slo, self.slo_mor))

        n = random.choice(self.eng)
        self.assertEqual(n, vrni_znak(".-", [n], [".-"]))

    def test_03_v_besedo(self):
        self.assertEqual("VSŠ",  v_besedo("...- ... ---.-", self.slo, self.slo_mor))
        self.assertEqual("FRI",  v_besedo("..-. .-. ..", self.slo, self.slo_mor))
        self.assertEqual("UL",  v_besedo("..- .-..", self.slo, self.slo_mor))

    def test_04_v_znake(self):
        self.assertEqual(
            "VSŠ FRI UL",
            v_znake("...- ... ---.-   ..-. .-. ..   ..- .-..", self.slo, self.slo_mor))

    def test_05_preberi(self):
        self.assertEqual(
            "VSŠ FRI UL",
            preberi("- - - ---   - - -   --- --- --- - ---      - - --- -   - --- -   - -      - - ---   - --- - -", self.slo, self.slo_mor))


"""class TestDodatna(Test):
    def test_zapisi(self):
        self.assertEqual(
            "- - - ---   - - -   --- --- --- - ---      - - --- -   - --- -   - -      - - ---   - --- - -",
            zapisi("VSŠ FRI UL", self.slo, self.slo_mor))"""


if __name__ == "__main__":
    unittest.main()
