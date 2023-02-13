enter = input("Rentrez un mot de passe : ")

def mdp(password):
    if len(password) < 8:
        print("Le mot de passe doit contenir au moins 8 caractères")

    maj = False
    min = False
    chi = False
    spe = False

    for i in range(len(password)):
        if password[i] >= "a" and password[i] <= "z":
            min = True

        if password[i] >= "A" and password[i] <= "Z":
            maj = True

        if password[i] >= "0" and password[i] <= "9":
            chi = True

        if password[i] == "!" or password[i] == "@" or password[i] == "#" or password[i] == "$" or password[i] == "%" or password[i] == "^" or password[i] == "&" or password[i] == "*":
            spe = True

    if min == False:
        print("Le mot de passe doit contenir au moins une lettre minuscule")

    if maj == False:
        print("Le mot de passe doit contenir au moins une lettre majuscule")

    if chi == False:
        print("Le mot de passe doit contenir au moins un chiffre")

    if spe == False:
        print("Le mot de passe doit contenir au moins un caractère spécial")

    if len(password) > 8 and min and maj and chi and spe == True:
        print("Le mot de passe respecte toutes les normes")
    
mdp(enter)