def my_sort(ma_liste): # Création de fonction
    nouvelle_liste = [] # Création d'une nouvelle liste
    compteur = 0 # Compteur de coup
    for nombre in ma_liste: # Boucle - Pour chaque nombre dans ma liste -
        index = 0 # Index de la nouvelle liste
        while index < len(nouvelle_liste) and nouvelle_liste[index] < nombre: 
            # Tant que l'index est < à la taille de la nouvelle liste et que l'index de la nouvelle liste < que le nombre à trier
            index += 1 # Incrémentation de l'index
            compteur += 1 # Incrémentation du compteur de coup
        nouvelle_liste.insert(index, nombre) # Ajout dans nouvelle liste à l'index n-1 ou n-2 en fonction 
    print("Nombre de coups : " + str(compteur)) # Affichage du nombre de coup
    return nouvelle_liste # Retour des résultats de la nouvelle liste
    

ma_liste = [22, 11, 12, 25, 95, 64, 90,] # Données à traiter = liste
resultat = my_sort(ma_liste) # Appel de la fonction
print(resultat) # Affichage de la fonction