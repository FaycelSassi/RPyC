def init():
    Element={}
    return Element
def ajouterEntree(a,b,Element):
    if a in Element:
        return Element[a]
    else :
        print("un utilisateur a ajouté ",a," avec le numero ",b)
        Element[a]=b
        return 0

def afftous(Element):
    return Element

def trouverNumero(nom,Element):
    if nom in Element:
        return Element[nom]
    else : return 0
    

def nbNumeros(Element):
    i=0
    for key in Element.keys():
        i=i+1
    return i

def supprimerEntree(nom,Element):   
    if nom in Element:
        print("un utilisateur a supprime ",nom," avec le numero ",Element[nom])
        Element.pop(nom)
        return 1
    else : return 0
    
def supprimerTout(Element):
    print("un utilisateur a supprime tous les elements")
    Element.clear()
    return Element
