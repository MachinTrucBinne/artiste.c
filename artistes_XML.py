# 2019-10-23
# Extraction des artistes du fichier Musique.XML produit par iTunes
# Le fichier Musique.XML doit être dans le directory du code Python
# rouler avec :
#    python3 artistes.py

# ici on utilise la librairie XML de Python

import xml.etree.ElementTree as ET
import datetime

# On importe le XML depuis un fichier :
tree = ET.parse('Musique.xml') # on lit depuis le disque
root = tree.getroot() 

artistes = [];
for chanson in root[0][17][1::2]: # on ne regarde que les positions impaires
	iterate_this = iter(chanson)
	for child in iterate_this:
		if (str(child.text) == "Artist"):
			next_child = next(iterate_this)
			artiste = str(next_child.text)
			if artiste not in artistes:
				artistes.append(artiste)
				#print(artiste)
			break

artistes.sort() # pour mettre les artistes en ordre alphabétique

write_file = open("artistes_extraits.txt","wt") # On ouvre le fichier d'écriture
write_file.write(str(datetime.date.today()) + "\n\nArtistes iTunes\n")
write_file.write("\nIl y a {} artistes trouvés :\n".format(len(artistes)))
for artiste in artistes:
    print(artiste)
    write_file.write("\n" + artiste)

write_file.close() # on ferme le fichier d'écriture




