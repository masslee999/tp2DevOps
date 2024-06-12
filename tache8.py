def viceversa(D1):
    dictionnaire = {}
    for cle, valeur in D1.items():
        dictionnaire[valeur] = cle
    return dictionnaire