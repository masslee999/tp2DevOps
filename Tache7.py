def calcul(D2):
    valeurs = list(D2.values())
    maximum = max(valeurs)
    minimum = min(valeurs)
    somme = sum(valeurs)
    moyenne = sum(valeurs) / len(valeurs)
    return f'maximum = {maximum}, minimum = {minimum}, somme = {somme}, moyenne = {moyenne: .2f}'