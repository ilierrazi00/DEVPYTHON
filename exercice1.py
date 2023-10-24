# Demander les informations personnelles
prenom = input("Entrez votre prénom : ")
nom = input("Entrez votre nom : ")
nom = nom.upper()  # Convertir le nom en majuscules
age = input("Entrez votre âge : ")
taille = input("Entrez votre taille en centimètres : ")
fruits_pref = input("Entrez vos fruits préférés : ").split(',') 
message_personnalise = input("Entrez un message de salutation personnalisé : ")

# Demander les propriétés d'un produit
nom_produit = input("Entrez le nom du produit : ")
prix_produit = input("Entrez le prix du produit : ")


# Afficher les informations saisies
print("\nInformations personnelles :")
print(f"Prénom : {prenom}")
print(f"Nom : {nom}")
print(f"Âge : {age} ans")
print(f"Taille : {taille} cm")
print(f"Fruits préférés : {', '.join(fruits_pref)}")
print(f"Message de salutation : {message_personnalise}")

print("\nPropriétés du produit :")
print(f"Nom du produit : {nom_produit}")
print(f"Prix du produit : {prix_produit}")

