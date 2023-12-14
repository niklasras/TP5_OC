nom1=input("Entrez le nom de la 1ere personne: ")
prenom1=input("Entrez le prenom de la 1ere personne: ")
nom2=input("Entrez le nom de la 2eme personne: ")
prenom2=input("Entrez le prenom de la 2eme personne: ")


print ("")
print ("L'ordre alphabetique des noms et prenoms sont les suivants:")
print ("")


if nom1<nom2:
    print (prenom1.capitalize())
    print (nom1.upper())
    print ("")
    print (prenom2.capitalize())
    print (nom2.upper())

elif nom1>nom2:
    print (prenom2.capitalize())
    print (nom2.upper())
    print ("")
    print (prenom1.capitalize())
    print (nom1.upper())

else:
    if prenom1<prenom2:
        print (prenom1.capitalize())
        print (nom1.upper())
        print ("")
        print (prenom2.capitalize())
        print (nom2.upper())
    else:
        print (prenom2.capitalize())
        print (nom2.upper())
        print ("")
        print (prenom1.capitalize())
        print (nom1.upper())