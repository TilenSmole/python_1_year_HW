poteze = [("j", "a"), ("a", "b"), ("b", "j"), ("a", "b"), ("j", "a"),
          ("a", "b"), ("b", "j"), ("a", "b"), ("a", "j"), ("b", "a"),
          ("j", "a"), ("a", "j")]

a = 0
b = 0
j = None
c = 0
d = 0
zastavlen_vrč = 7
zastavlen_vrč_b = 4
trditev = True

for litri in poteze:
    odkje, kam = litri
    # iz jezera v vrč a
    if odkje == "j" and kam == "a":
        a = 7
    # iz jezera v vrč b
    elif odkje == "j" and kam == "b":
        b = 4
    # iz vrča b v jezero
    elif odkje == "b" and kam == "j":
        b = 0
    # iz vrča a v jezero
    elif odkje == "a" and kam == "j":
        a = 0
    # iz vrča a v vrč b
    elif odkje == "a" and kam == "b":
        prostor_b = zastavlen_vrč_b - b
        if a > prostor_b:
            b += prostor_b
            a -= prostor_b
        elif a < prostor_b:
            b += a
            a = 0
        else:
            b += a
            a = 0
    #iz vrča b v vrč a
    elif odkje == "b" and kam == "a":
        prostor_a = zastavlen_vrč - a
        if b > prostor_a:
            a += prostor_a
            b -= prostor_a
        elif b < prostor_a:
            a += b
            b = 0
        else:
            a += b
            b = 0
    print("a:", a, "b:", b)
