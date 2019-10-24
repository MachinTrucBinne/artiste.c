# 2019-10-20
# Extraction des artistes du fichier Musique.XML produit par iTunes
# Le fichier Musique.XML doit être dans le directory du code Python
# rouler avec :
#    python3 artistes.py

# ici on utilise les ReGeX

import re # pour les ReGeX
import datetime # pour la date

# Ouverture des fichiers de lecture et d'écriture
read_file  = open("Musique.xml","rt") # On ouvre le fichier de lecture
write_file = open("artistes_extraits.txt","wt") # On ouvre le fichier d'écriture

artistes = re.findall(r'<key>Artist</key><string>.+</string>', read_file.read())
artistes_reduit = []
for artiste in artistes: # pour ne pas avoir de doublons
    if artiste not in artistes_reduit:
        artistes_reduit.append(artiste)

for i in range(len(artistes_reduit)):
    artistes_reduit[i] = re.sub("&#38;","&",artistes_reduit[i]) # il faut changer les &#38 en &

artistes_reduit.sort() # pour mettre les artistes en ordre alphabétique

print("Les artistes sans doubles :")

write_file.write(str(datetime.date.today()) + "\n\nArtistes iTunes\n")
write_file.write("\nIl y a {} artistes trouvés :\n".format(len(artistes_reduit)))
for artiste in artistes_reduit:
    print(artiste[25:-9])
    write_file.write("\n" + artiste[25:-9])

# On ferme les fichiers de lecture et d'écriture :
read_file.close()
write_file.close()

