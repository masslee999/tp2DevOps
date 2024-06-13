def filtre(dico):
  dico_filtre = {}  # Dictionnaire vide pour stocker les éléments filtrés
  for key, valeur in dico.items():
    if len(valeur) > 5:  # Vérification de la longueur de la chaîne
      dico_filtre[key] = valeur  # Ajout au dictionnaire filtré
  return dico_filtre