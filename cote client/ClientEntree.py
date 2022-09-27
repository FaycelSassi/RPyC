import rpyc

c=rpyc.connect("IP", 18861)

print("Choix de l'action a effectuer :\n 1: Ajoutar una entree dans la repertoire\n 2: Afficher le numero de telephone d'une personne\n 3: Afficher le nombre de numeros enregistres dans le repertoire \n 4. Afficher le contenu de tout le repertoire \n 5: Supprimer du repertoire une personne et son numero\n 6: Effacer tout le contenu du repertoire\n 0: Quitter le programme")
a=input(' ')
if a.isdigit():a=int(a)
ver=0
while a!=0:
    if a==1 :
        print(' Veuillez saisir les informations:')
        nom=input('  nom ? ')
        tel=input('  num de tel ? ')
        while len(tel)!=8 or ver==0:
            tel=input('  num de tel ? ')
            if tel.isdigit():
                ver=1
        ajout=c.root.exposed_ajouterEntree(nom,tel)
        if ajout ==0:
            print(" Element ajoutee")
        else: print(" Element existe deja avec le numero",ajout)
    if a==4:
        print(' Les elements ajoutees sont :',c.root.exposed_afftous())
    if a==2:
        nom=input(' nom ? ')
        Element=c.root.exposed_trouverNumero(nom)
        if Element==0 : print(nom," n'existe pas")
        else : print(nom,' a le numero :',Element)
    if a==3:
        nbre=c.root.exposed_nbNumeros()
        print(" Le nombre des numeros est ",nbre)
    if a==5:
        nom=input(' nom ? ')
        supp=c.root.exposed_supprimerEntree(nom)
        if supp==0:
            print(" le numero de ",nom," n'existe pas")
        else:print(" le numero de ",nom," est supprimee")
    if a==6:
        b=int(input(' Voulez vous vraiment supprimer tous les numeros? 1/0 \n'))
        if b==1:
            Element=c.root.exposed_supprimerTout()
            print('Tous les elements ont ete supprime')
    a=input(' ')
    if a.isdigit():a=int(a)
    
