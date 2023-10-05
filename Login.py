# Login

def regist():
    ok_reg = True
    user()
    psw()
    cycle = 1
    while not psw_auth():
        cycle += 1
        if cycle > 3:
            ok_reg = False
            break
    return ok_reg


def user():
    user_email = input("E-mail address: ")
    while " " in user_email or "@" not in user_email or "." not in user_email:
        user_email = input("Error!\nE-mail address again: ")


def psw():
    user_psw = input("Password (contain 1 number, minimum 8 caracter and contain a capital letter): ")
    ok_psw = True
    while ok_psw:
        if len(user_psw) < 8:
            ok_psw = False
        nmb = 0
        for i in range(len(user_psw)):
            if user_psw[i].isnumeric():
                nmb += 1
        if nmb == 0:
            ok_psw = False
        if not ok_psw:
            user_psw = input("Error!\nPassword (contain 1 number, minimum 8 caracter and contain a capital letter): ")
            ok_psw = True
        else:
            ok_psw = False


def psw_auth():
    ok_psw = True
    return ok_psw


def login():
    pass


# Start of the program
user_email = ""
user_psw = ""
if regist():
    login()
