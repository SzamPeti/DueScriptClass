# Tax calculation from income
print("Tax calculation from income\n")

age = int(input("How old are you?"))

if age > 25:
    child = input("Do you have 3 child and are you a woman?(yes/no)")
    while child not in ["yes", "Yes", "Y", "y", "No", "no", "n", "N"]:
        child = input("Error!! \nDo you have 3 child and are you a woman?(yes/no)")

incomeb = int(input("How much is your income (with tax)?"))

if age <= 25 or child in ["yes", "Yes", "Y", "y"]:
    if incomeb > 500000:
        SZJA = (incomeb-500000)*0.15
    else:
        SZJA = 0
else:
    SZJA = incomeb*0.15

print("TAX".center(40))
print("SZJA:".ljust(30, "_"), str(int(SZJA)).rjust(10, "_"), sep="")
print("Nyugdíj:".ljust(30, "_"), str(int(incomeb * 0.1)).rjust(10, "_"), sep="")
print("TB:".ljust(30, "_"), str(int(incomeb * 0.07)).rjust(10, "_"), sep="")
print("Munkanélküli:".ljust(30, "_"), str(int(incomeb * 0.015)).rjust(10, "_"), sep="")
print("")
print("Netto:".ljust(30, "_"), str(int(incomeb-(incomeb * 0.185)-SZJA)).rjust(10, "_"), sep="")
