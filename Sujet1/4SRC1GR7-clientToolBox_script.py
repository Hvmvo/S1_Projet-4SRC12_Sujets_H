import os

# Créer un tube nommé pour envoyer les requêtes au serveur
request_pipe = os.open('request_pipe', os.O_WRONLY)

while True:
    # Afficher les options de menu
    print("1) Sortir de la boite à outils")
    print("2) Informations sur la mémoire")
    print("3) Informations sur les processus")
    print("4) Informations sur l'occupation du/des processeurs")

    # Lire l'option de menu sélectionnée par l'utilisateur
    choice = input("Entrez votre choix: ")

    # Envoyer la requête au serveur
    os.write(request_pipe, choice.encode())

    # Quitter le programme si l'utilisateur choisit l'option 1
    if choice == "1":
        break

    # Lire la réponse du serveur
    response_pipe = os.open('response_pipe', os.O_RDONLY)
    data = os.read(response_pipe, 1024)
    os.close(response_pipe)

    # Afficher la réponse du serveur
    print(data.decode())