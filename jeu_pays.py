import random
def jeu_capital():
    pays_capital = {"France":"Paris","Germany" : "Berlin","italy" :"Rome","Cameroon" : "Yaounde","Zimbabwe" : "Harare","Canada" : "Ottowa","Russia" : "Moscow","Morocco" : "Rabat","Gabon" : "Librevile","Mali" : "Kigali"}
    pays = list(pays_capital.keys())
    deja_choisi = []
    score, nbre = 0,1
    nbre_question = 10
    for i in range(0,nbre_question):
        choix_pays = random.choice(pays)
        while choix_pays in deja_choisi:
            choix_pays = random.choice(pays)
        deja_choisi.append(choix_pays)
        answer = input(f"{nbre}. what is the capital of {choix_pays}? ")
        nbre+=1
        if(answer.lower() == pays_capital[choix_pays].lower()):
            print("Bonne reponse!!!")
            score+=1
        else:
            print(f"Mauvaise reponse. La bonne reponse est {pays_capital[choix_pays].upper()}") #retourne la capital du pays choisis
    print(f"Jeu terminer votre score {score}/{i+1}")
jeu_capital()
