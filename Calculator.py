# Calculator
def adatkeres(tipus):
    valasz = 0
    if tipus == "sz":
        valasz = input("Kérek egy számot: ")
        while not valasz .isnumeric():
            print("Rossz érték!!")
            valasz = input("Kérek egy számot: ")
        valasz = int(valasz)
    elif tipus == "m":
        valasz = input("Kérem a műveleti jelet (+, -, *, /)")
        while valasz not in ["+", "-", "*", "/"]:
            print("Nem érvényes a jel!")
            valasz = input("Kérem a műveleti jelet (+, -, *, /)")
    return valasz


def szamolas():
    global eredmeny
    if muvelet == "+":
        eredmeny = nmb1 + nmb2
    elif muvelet == "-":
        eredmeny = nmb1 - nmb2
    elif muvelet == "*":
        eredmeny = nmb1 * nmb2
    elif muvelet == "/":
        eredmeny = nmb1 / nmb2
    return eredmeny


print("Calculator")
nmb1 = adatkeres("sz")
nmb2 = adatkeres("sz")
muvelet = adatkeres("m")
eredmeny = szamolas()
szamolas()


print(str(nmb1).rjust(50))
print(muvelet, end="")
print(str(nmb2).rjust(49))
print("".rjust(50, "_"))
print(str(eredmeny).rjust(50))
