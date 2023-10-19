# Login

def regist():
    ok_reg = True
    user_email = user()
    # generating a password automaticly
    user_psw = psw()
    if not psw_auth(user_psw, 3, "Password again: "):
        ok_reg = False

    if ok_reg:
        with open("psw.txt", "a", encoding="UTF-8") as fajl:
            fajl.write(user_email + ";" + user_psw + "\n")
    return ok_reg


def user():
    user_email = input("E-mail address: ")
    while " " in user_email or "@" not in user_email or "." not in user_email:
        user_email = input("Error!\nE-mail address again: ")
    return user_email


def psw():
    user_psw = input("Password (contain 1 number, minimum 8 caracter and contain a capital letter): ")
    ok_psw = True
    while ok_psw:
        if len(user_psw) < 8:
            ok_psw = False

        van = 0
        for i in range(len(user_psw)):
            if user_psw[i].isnumeric():
                van += 1
        if van == 0:
            ok_psw = False

        van = 0
        for i in range(len(user_psw)):
            if user_psw[i].isupper():
                van += 1
        if van == 0:
            ok_psw = False

        van = 0
        for i in range(len(user_psw)):
            if user_psw[i].islower():
                van += 1
        if van == 0:
            ok_psw = False

        if not ok_psw:
            user_psw = input("Error!\nPassword (must contain 1 number, a capital letter and minimum 8 caracter): ")
            ok_psw = True
        else:
            ok_psw = False
        return user_psw


def psw_auth(user_psw, attempts, msg):
    i = 1
    psw2 = input(msg)
    while psw2 != user_psw and i < attempts:
        psw2 = input(msg)
        i += 1
    if psw2 == user_psw:
        ok_psw = True
    else:
        ok_psw = False
    return ok_psw


def user_auth(user):
    password = ""
    with open("psw.txt", "r", encoding="UTF-8") as fajl:
        for line in fajl:
            lista = line.strip("\n")
            felhasz = lista.split(";")
            if felhasz[0] == user:
                password = felhasz[1]
    return password


def login():
    ok_login = True
    jelszo = user_auth(user())
    if jelszo == "":
        print("Not found any user!")
        ok_login = False
    else:
        if not psw_auth(jelszo, 3, "Give a password: "):
            ok_login = False
    return ok_login


# Base of the program
if __name__ == "__main__":
    user_email = ""
    user_psw = ""
    if regist():
        print("Registery is succesful.")
        if login():
            print("Login succesfull!")
        else:
            print("Try again.")
    else:
        print("Error!!")
