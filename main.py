import empruntMat
import cliennt
import materiel as M
from colorama import Fore, Style
import re
from termcolor import cprint

def choices(title):
    print('*'*36)
    print(Fore.GREEN + "            MENU "+title.upper()+Style.RESET_ALL)
    print(Fore.BLUE + "1. Lister les "+title+"s" + Style.RESET_ALL )
    print(Fore.BLUE + "2. Ajouter un "+title + Style.RESET_ALL)
    print(Fore.BLUE + "3. Modifier un "+title + Style.RESET_ALL)
    print(Fore.BLUE + "4. Retirer un "+title + Style.RESET_ALL)
    print(Fore.BLUE + "5. Rechercher un "+title + Style.RESET_ALL)
    print(Fore.RED + "6. Revenir au menu principal" + Style.RESET_ALL)
    print('*'*36)


def client():
        # Instructions pour client ici
        c = cliennt.Client()
        choices("client")
        #print("Entrez une commande ('a' pour afficher la liste des commandes disponibles, 'q' pour revenir au menu principal)")
        
        p = r"modifier\s(.+)"
        p1 = r"supprimer\s(.+)"
        p2 = r"chercher\s(.+)"

        while True:
            ch = input("[Client] Entrer votre choix(1-6): ").strip()

            if ch == 'a':
                print(Fore.GREEN+"a"+Style.RESET_ALL+" : lister tous les commandes disponibles")
                print(Fore.GREEN+"ajouter"+Style.RESET_ALL+" : lister tous les commandes disponibles")
                print(Fore.GREEN+"chercher"+Style.RESET_ALL+" [cle]: chercher des clients à partir id du client, nom, classe")
                print(Fore.GREEN+"lt"+Style.RESET_ALL+" : lister tous les matériels")
                print(Fore.GREEN+"modifier"+Style.RESET_ALL+" [id]: modifier les propriétés d'un client avec l'id entrée")
                print(Fore.GREEN+"supprimer"+Style.RESET_ALL+" [id]: supprimer les données d'un client avec l'id entrée")
                print(Fore.GREEN+"q"+Style.RESET_ALL+" : revenir au menu principal")
            elif ch == 'q' or ch == '6':
                break
            elif ch == 'ajouter' or ch == '2':
                id_client = input("Entrez l'idClient du nouveau client : ").title()
                c.c.execute("SELECT idClient FROM client where idClient = ?",(id_client,))
                ids = c.c.fetchall()
                if (id_client,) in ids:
                    cprint("[-]Cet ID est deja pris",'red')
                else:
                    nom_client = input("Entrez le nom du nouveau client : ").title()
                    classe_client = input("Entrez la classe du nouveau client : ").upper()
                    if c.inserer_client(id_client, nom_client, classe_client):
                        cprint("[+]Ajout de client effectué avec succès.", 'green')
                        c.afficher_clients()
                    else:
                        cprint("[-]Une erreur s'est produite", 'red')
                choices("client")
            elif re.match(p, ch) or ch == '3':
                id_materiel = (ch.split(" ")[1]).title()
                c.c.execute("SELECT idClient FROM client where idClient = ?",(id_materiel,))
                ids = c.c.fetchall()
                if (id_materiel,) in ids:
                    c.afficher_client_by_id(id_materiel)
                    nom_materiel = input("Entrez le nom du client : ").title()
                    classe_materiel = input("Entrez la classe du client : ").upper()
                    if c.modifier_client(id_materiel, nom_materiel, classe_materiel):
                        cprint("[+]Modification du client effectué avec succès.", 'green')
                    else:
                        cprint("[-]Une erreur s'est produite", 'red')
                else:
                    cprint("[-]Client non reconnu", 'red')
                choices("client")
            elif re.match(p1, ch) or ch == '4':
                if(ch=='4'):
                    id_materiel = input("Entrer l'ID du client: ")
                else:
                    id_materiel = (ch.split(" ")[1]).title()
                c.c.execute("SELECT idClient FROM client where idClient = ?",(id_materiel,))
                ids = c.c.fetchall()
                if (id_materiel,) in ids:
                    cprint("[!]Voulez-vous vraiment supprimer?(o/n)",'yellow')
                    resp = input(">>>").lower()
                    if resp == 'o':
                        if c.supprimer_client(id_materiel):
                            cprint("[+]Le client a été retiré avec succès.", 'green')
                        else:
                            cprint("[-]Une erreur s'est produite", 'red')
                    else:
                        pass
                else:
                    cprint("[-]Client non reconnu", 'red')
                choices("client")
            elif re.match(p2, ch) or ch == '5':
                if(ch == '5'):
                    key=input("Entrer le terme a chercher: ")
                else:
                    key = (ch.split(" ")[1]).title()
                c.afficher_client_by_key(key)
                choices("client")
            elif ch == 'lt' or ch == '1':
                c.afficher_clients()
                choices("client")
            else:
                cprint("[-]Choix invalide", 'red')
                choices("client")
                #cprint("[-]Commande introuvable ou incomplète.", 'red')
                #cprint("[!]Taper 'a' pour voir la liste des commandes valides",'yellow')


def materiel():
    
    # Instructions pour matériel ici
    m = M.Materiel()
    #print("Entrez une commande ('a' pour afficher la liste des commandes disponibles, 'q' pour revenir au menu principal)")
    choices("materiel")
    p = r"modifier\s(.+)"
    p1 = r"supprimer\s(.+)"
    p2 = r"chercher\s(.+)"

    while True:
        ch = input("[Materiel] Entrer votre choix(1-6): ").strip()

        if ch == 'a':
            print(Fore.GREEN+"a"+Style.RESET_ALL+" : lister tous les commandes disponibles")
            print(Fore.GREEN+"ajouter"+Style.RESET_ALL+" : lister tous les commandes disponibles")
            print(Fore.GREEN+"chercher"+Style.RESET_ALL+" [cle]: chercher des matériels à partir id du matériel, désignation, nombre")
            print(Fore.GREEN+"lt"+Style.RESET_ALL+" : lister tous les matériels")
            print(Fore.GREEN+"modifier"+Style.RESET_ALL+" [id]: modifier les propriétés de l'emprunt avec l'id entrée")
            print(Fore.GREEN+"supprimer"+Style.RESET_ALL+" [id]: supprimer les données d'un materiel avec l'id entrée")
            print(Fore.GREEN+"q"+Style.RESET_ALL+" : revenir au menu principal")
        elif ch == 'q' or ch == '6':
            break
        elif ch == 'ajouter' or ch == '2':
            idM = input("Entrez l'ID du matériel: ").title()
            m.c.execute("SELECT idMat FROM materiel where idMat = ?",(idM,))
            ids = m.c.fetchall()
            if (idM,) in ids:
                cprint("[-]Cet ID est deja pris",'red')
            else:
                des = input("Entrez la désignation du matériel: ").title()
                stock = int(input("Entrez le nombre de materiél à ajouter: "))
                if m.ajouter_materiel(idM,des,stock):
                    cprint("[+]Ajout de matériel effectué avec succès.", 'green')
                    m.afficher_materiel()
                else:
                    cprint("[-]Une erreur s'est produite", 'red')
            choices("materiel")
        elif re.match(p, ch) or ch == '3':
            if(ch=='3'):
                id_materiel = input("Entrer l'ID du materiel: ")
            else:
                id_materiel = (ch.split(" ")[1]).title()
            m.c.execute("SELECT idMat FROM materiel where idMat = ?",(id_materiel,))
            ids = m.c.fetchall()
            if (id_materiel,) in ids:
                m.afficher_materiel_by_id(id_materiel)
                nom_materiel = input("Entrez la nouvelle désignation du matériel : ")
                classe_materiel = input("Entrez le nouveau nombre en stock : ")
                if m.modifier_materiel(id_materiel, nom_materiel, classe_materiel):
                    cprint("[+]Modification du matériel effectué avec succès.", 'green')
                else:
                    cprint("[-]Une erreur s'est produite", 'red')
            else:
                cprint("[-]Matériel non reconnu", 'red')
            choices("materiel")
        elif re.match(p1, ch) or ch == '4':
            if(ch=='4'):
                id_materiel = input("Entrer l'ID du materiel: ")
            else:
                id_materiel = (ch.split(" ")[1]).title()
            m.c.execute("SELECT idMat FROM materiel where idMat = ?",(id_materiel,))
            ids = m.c.fetchall()
            if (id_materiel,) in ids:
                cprint("[!]Voulez-vous vraiment supprimer?(o/n)",'yellow')
                resp = input(">>>").lower()
                if resp == 'o':
                    if m.supprimer_materiel(id_materiel):
                        cprint("[+]Suppression du matériel effectué avec succès.", 'green')
                    else:
                        cprint("[-]Une erreur s'est produite", 'red')
                else:
                    pass
            else:
                cprint("[-]Matériel non reconnu", 'red')
            choices("materiel")
        elif re.match(p2, ch) or ch == '5':
            if(ch=='5'):
                key=input("Entrer le terme a chercher: ")
            else:
                key = (ch.split(" ")[1]).title()
            m.afficher_materiel_by_key(key)
            choices("materiel")
        elif ch == 'lt' or ch == '1':
            m.afficher_materiel()
            choices("materiel")
        else:
            cprint("[-]Choix invalide.", 'red')
            #cprint("[-]Commande introuvable ou incomplète.", 'red')
            #cprint("[!]Taper 'a' pour voir la liste des commandes valides",'yellow')
            choices("materiel")

def choicesEmprunt(title):
    print('*'*36)
    print(Fore.GREEN + "            MENU "+title.upper()+Style.RESET_ALL)
    print(Fore.BLUE + "1. Lister tous les "+title+"s" + Style.RESET_ALL )
    print(Fore.BLUE + "2. Lister tous les "+title+"s rendus" + Style.RESET_ALL )
    print(Fore.BLUE + "3. Lister tous les "+title+"s non rendus" + Style.RESET_ALL )
    print(Fore.BLUE + "4. Faire un "+title + Style.RESET_ALL)
    print(Fore.BLUE + "5. Rendre un "+title + Style.RESET_ALL)
    print(Fore.BLUE + "6. Modifier un "+title + Style.RESET_ALL)
    print(Fore.BLUE + "7. Retirer un "+title + Style.RESET_ALL)
    print(Fore.BLUE + "8. Rechercher un "+title + Style.RESET_ALL)
    print(Fore.RED + "9. Revenir au menu principal" + Style.RESET_ALL)
    print('*'*36)

def emprunte():
    # Instructions pour emprunt matériel ici
    m = empruntMat.emprunt("emprunt.db")
    choicesEmprunt("emprunt")
    #print("Entrez une commande ('a' pour afficher la liste des commandes disponibles, 'q' pour revenir au menu principal)")
    p = r'^rendre \d+$'
    p2 = r'^modifier \d+$'
    p3 = r'^supprimer \d+$'
    p4 = r"chercher\s(.+)"
    while True:
        sub_choice = input("[Emprunt] Entrez votre choix(1-9): ").strip()
        if sub_choice == 'a':
            print(Fore.GREEN+"a"+Style.RESET_ALL+" : lister tous les commandes disponibles")
            print(Fore.GREEN+"chercher"+Style.RESET_ALL+" [cle]: chercher des matériels non rendus à partir id du client, date d'emprunt, nombre, id du matériel")
            print(Fore.GREEN+"emprunter"+Style.RESET_ALL+" : effectuer un nouvel emprunt")
            print(Fore.GREEN+"lt"+Style.RESET_ALL+" : lister tous les emprunts")
            print(Fore.GREEN+"lr"+Style.RESET_ALL+" : lister les emprunts rendus")
            print(Fore.GREEN+"lnr"+Style.RESET_ALL+" : lister les emprunts non rendus")
            print(Fore.GREEN+"modifier"+Style.RESET_ALL+" [id]: modifier les propriétés de l'emprunt avec l'id entrée")
            print(Fore.GREEN+"rendre"+Style.RESET_ALL+" [id]: rendre le matériel avec l'id entrée")
            print(Fore.GREEN+"supprimer"+Style.RESET_ALL+" [id]: supprimer les données d'emprunt avec l'id entrée")
            print(Fore.GREEN+"q"+Style.RESET_ALL+" : revenir au menu principal")
        elif sub_choice == 'q' or sub_choice == '9':
            break
        elif sub_choice == 'lt' or sub_choice == '1':
            m.afficheTablee("emprunt")
            choicesEmprunt("emprunt")
        elif sub_choice == 'lnr' or sub_choice =='3':
            m.afficheNonRendus("emprunt")
            choicesEmprunt("emprunt")
        elif sub_choice == 'lr' or sub_choice == '2':
            m.afficheRendus("emprunt")
            choicesEmprunt("emprunt")
        elif sub_choice == 'emprunter' or sub_choice == '4':
            m.empruntmat("emprunt")
            m.afficheNonRendus("emprunt")
            choicesEmprunt("emprunt")
        elif re.match(p4, sub_choice) or sub_choice == '8':
            if(sub_choice == '8'):
                id = input("Entrer un terme a rechercher: ")
            else:
                id = sub_choice.split(" ")[1]
            m.chercherEmpruntNonRendu(id,"emprunt")
            choicesEmprunt("emprunt")
        elif re.match(p3, sub_choice) or sub_choice == '7':
            if(sub_choice =='7'):
                key = input("Entrer l'ID d'emprunt: ")
            else:
                id = sub_choice.split(" ")[1]
            cprint("[!]Voulez-vous vraiment supprimer?(o/n)",'yellow')
            resp = input(">>>").lower()
            if resp == 'o':
                m.supprimerempruntmat("emprunt",id)
            else:
                pass
            choicesEmprunt("emprunt")
        elif re.match(p2, sub_choice) or sub_choice == '6':
            if(sub_choice == '6'):
                key = input("Entrer l'ID d'emprunt: ")
            else:
                id = sub_choice.split(" ")[1]
            m.modifierempruntmat("emprunt",id)
            choicesEmprunt("emprunt")
        elif re.match(p, sub_choice) or sub_choice == '5':
            if(sub_choice == '5'):
                key = input("Entrer l'ID d'emprunt: ")
            else:
                id = sub_choice.split(" ")[1]
            m.rendreMateriel("emprunt",id)
            choicesEmprunt("emprunt")
        else:
            cprint("[-]Choix invalide.", 'red')
            #cprint("[-]Commande introuvable ou incomplète.", 'red')
            #cprint("[!]Taper 'a' pour voir la liste des commandes valides", 'yellow')
            choicesEmprunt("emprunt")



def quit_program():
    print("------------------------------------")
    print(Fore.CYAN + "Au revoir !" + Style.RESET_ALL)
    quit()


if __name__ == '__main__':
    cprint("Bienvenue dans le logiciel de gestion d'emprunt de materiels",'blue')

    options = {
        "1": emprunte,
        "2": materiel,
        "3": client,
        "4": quit_program,
    }

    while True:
        print('-'*38)
        print("|"+Fore.GREEN + "            MENU PRINCIPAL" + Style.RESET_ALL + "          |")
        print("|"+Fore.BLUE + "1. Emprunts" + Style.RESET_ALL + "                         |")
        print("|"+Fore.BLUE + "2. Matériels" + Style.RESET_ALL + "                        |")
        print("|"+Fore.BLUE + "3. Clients" + Style.RESET_ALL + "                          |")
        print("|"+Fore.RED + "4. Quitter" + Style.RESET_ALL + "                          |")
        print('-'*38)

        choice = input("Entrez votre choix (1-4): ")
        action = options.get(choice)
        if action:
            action()
        else:
            print(Fore.LIGHTRED_EX + "Choix invalide. Réessayez.\n" + Style.RESET_ALL)
