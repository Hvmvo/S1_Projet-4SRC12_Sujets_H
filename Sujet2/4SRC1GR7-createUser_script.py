# Import des modules
import os, sys, csv

# Vérification de l'existance de l'utilisateur
def verifUser(username):
    with open('/etc/passwd', mode='r', encoding='utf-8-sig') as passwd:
        for line in passwd:
            return line.startswith(username + ':')
    
# Vérification de l'existance du groupe
def verifGroup(groupname):
    with open('/etc/group', mode='r', encoding='utf-8-sig') as group:
        for line in group:
            return line.startswith(groupname + ':')

# Création de l'utilisateur
def createUser(username):
    os.system ('useradd -N ' + username )

# Création du groupe
def createGroup(groupname):
    os.system('groupadd ' + groupname)

# Assignation de l'utilisateur dans le groupe
def assignUser(username,groupname):
    os.system('usermod -a -G ' + groupname + " " + username)
    if verifUser(username):
        print("L'utilisateur " + username + " est ajouté dans le groupe " + groupname)

# === MAIN ===

# Lecture du CSV d'utilisateur avec délimiter ':'
with open(sys.argv[1], mode='r', encoding='utf-8-sig') as fichier:
    lecture = csv.reader(fichier, delimiter=':')

    # Traitement ligne par ligne sur le CSV
    for ligne in lecture:

        # Traitement index par index sur la ligne
        for i in range (len(ligne)):
            if (i == 0):
                if (verifUser(ligne[i]) == False):
                    createUser(ligne[i])
            elif (i == 1):
                if (verifGroup(ligne[i]) == False):
                    createGroup(ligne[i])

        # Appel de la fonction d'assignation
        assignUser(ligne[0],ligne[1])
