# Calculator
print("Calculator")

nmb1 = input("Kérek egy számot: ")
while not nmb1 .isnumeric():
    print("Rossz érték!!")
    nmb1 = input("Kérek egy számot: ")
nmb1 = int(nmb1)

nmb2 = input("Kérek egy számot: ")
while not nmb2 .isnumeric():
    print("Rossz érték!!")
    nmb2 = input("Kérek egy számot: ")
nmb2 = int(nmb2)

muvelet = input("Kérem a műveleti jelet (+, -, *, /)")
while muvelet not in ["+", "-", "*", "/"]:
    print("Nem érvényes a jel!")
    muvelet = input("Kérem a műveleti jelet (+, -, *, /)")

eredmeny = 0
if muvelet == "+":
    eredmeny = nmb1 + nmb2
elif muvelet == "-":
    eredmeny = nmb1 - nmb2
elif muvelet == "*":
    eredmeny = nmb1 * nmb2
elif muvelet == "/":
    eredmeny = nmb1 / nmb2

print(str(nmb1).rjust(50))
print(muvelet, end="")
print(str(nmb2).rjust(49))
print("".rjust(50, "_"))
print(str(eredmeny).rjust(50))
