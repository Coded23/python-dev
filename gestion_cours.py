cours = [] #variable global

#fonction pour ajouter un cour
def ajouter_cours():
    etudiants = [] #liste vide
    titre = input("Entrez le titre: ")
    formateur = input("Entrez le formateur: ")
    duree = input("Entrez la duree: ")
    cours.append({"Titre":titre,"Formateur":formateur,"Duree":duree,"Etudiant":etudiants})
    print("cours ajouter avec succes")

#fonction pour afficher les cours
def afficher_cours():
    if not cours:
        print("Pas de cours enregistrer")
        return
    for i,c in enumerate(cours, start=1):
        print(f"{i}.Titre:{c['Titre']}, Formateur:{c['Formateur']} ,Duree:{c['Duree']}heures, Etudiants inscrits:{c['Etudiant']}")

#rechercher un cours par son titre
def rechercher_cours():
    if not cours:
        print("Il n'y a aucun cours enregistrer ")
        return
    titre_rechercher = input("Entre le titre du cours a rechercher")
    for c in cours:
        result = c['Titre']
        if titre_rechercher.upper() == result.upper():
            print(f"{titre_rechercher}, Formateur:{c['Formateur']},Duree: {c['Duree']}")
            return
    print(f"{titre_rechercher} n'existe pas.")

#inscrire un etudiant a un cours
def inscrire_etudiant():
    if not cours:
        print("il n'y a pas cours enregistrer. Veillez enregistrez un cours")
        return
    inscrit_au_cours = input("Entrez le titre du cours: ")
    for c  in cours:
        if inscrit_au_cours.upper() == c['Titre'].upper():
            etudiant_inscrit = input("Entrez le nom de l'etudiant a inscrit: ")
            c['Etudiant'].append(etudiant_inscrit)
            print("Etudiant inscire avec succes")
            return
    print(f"{inscrit_au_cours} n'existe pas veillez l'ajouter a la liste des cours")

#afficher les etudiants inscrits a un cours
def afficher_etudiant():
    if not cours:
        print("Aucun cour n'est enregistrer")
        return
    list_etudiant = input("Entrez le titre du cours vous voulez voir la liste des etudiants inscrits")
    for i,c in enumerate(cours,start=1):
        if list_etudiant.upper() == c["Titre"].upper():
            print(f"{i}.{c['Titre']},{c['Etudiant']}")
            return
    print(f"{list_etudiant} n'existe pas")

# Supprimer un cours
def supprimer_cours():
    if not cours:
        print("Aucun cours n'est enregistrer")
        return
    cours_supprimer = input("Entrez le titre du cours a supprimer")
    for c in cours:
        if cours_supprimer.lower() == c['Titre'].lower():
            cours.remove(c)
    print(f"{cours_supprimer} n'existe pas dans la liste des cours enregistrer")

#modifier les details d'un cours
def modifier_cours():
    if not cours:
        print("Aucun cours n'est enregistrer")
        return
    print("***** LAISSEZ LES CHAMPS VOUS ALLEZ CONSERVER VIDE EN TAPANT ENTRER *****")
    cours_modifier = input("Entrez le titre du cours: ")
    for c in cours:
        if cours_modifier.lower() == c['Titre'].lower():
            modifier_titre = input("Entrez le nouveau titre: ")
            modifier_formateur = input("Entrez le nouveau formateur: ")
            modifier_duree = input("Entrez la nouvelle duree: ")
            c['Titre'] = modifier_titre or c['Titre']
            c['Formateur'] = modifier_formateur or c['Formateur']
            c['Duree'] = modifier_duree or c['Duree']
            print("Modification effectuer avec succes")
            return
    print(f"{cours_modifier} n'est pas dans la liste de cours")

#Appel des fonction

while True:
    print("\n==== Gestion des cours Easylearn====")
    print("1.Ajouter un cours")
    print("2.Afficher tous les cours")
    print("3.Recherche un cour par le titre")
    print("4.inscrire un etudiant a un cours")
    print("5.Afficher les etudiants d'un cours")
    print("6.Supprimer un cours")
    print("7.Modifier les details d'un cours(titre,formateur,duree)")
    print("8.Quitter")
    choix = input("choix: ")
    if choix == "1":
        ajouter_cours()
    elif choix == "2":
        afficher_cours()
    elif choix == "3":
        rechercher_cours()
    elif choix == "4":
        inscrire_etudiant()
    elif choix == "5":
        afficher_etudiant()
    elif choix == "6":
        supprimer_cours()
    elif choix == "7":
        modifier_cours()
    elif choix == "8":
        print("MERCI D'AVOIR EASYLEARN")
        break
    else:
        print("choix invalide, veillez reessayer.")