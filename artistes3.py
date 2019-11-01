# 2019-10-27
# Pour mettre les informations du fichier Musique.XML produit par iTunes dans un autre fichier .XML
# Le fichier Musique.XML doit être dans le directory du code Python.

import xml.etree.ElementTree as ET

# On importe les données XML :
tree = ET.parse('Musique.xml')
root = tree.getroot() 

# On ouvre un fichier d'écriture
write_file = open("Musique_extraite.xml","wt")
write_file.write("<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<librairie>\n") # en tête XML

# La liste des propriétés d'un morceau qu'on veut
proprietes =             ["Name","Artist","Album","Genre","Kind","Size","Total Time","Disc Number","Disc Count","Track Number","Track Count","Year","Bit Rate","Sample Rate"]
proprietes_sans_espace = {"Name":"Name","Artist":"Artist","Album":"Album","Genre":"Genre","Kind":"Kind","Size":"Size","Total Time":"Total_Time","Disc Number":"Disc_Number","Disc Count":"Disc_Count","Track Number":"Track_Number","Track Count":"Track_Count","Year":"Year","Bit Rate":"Bit_Rate","Sample Rate":"Sample_Rate"}
nombre_de_proprietes = len(proprietes)

for chanson in root[0][17][1::2]: # on ne regarde que les positions impaires
	dictionnaire = {"Name":"","Artist":"","Album":"","Genre":"","Kind":"","Size":"","Total_Time":"","Disc_Number":"","Disc_Count":"","Track_Number":"","Track_Count":"","Year":"","Bit_Rate":"","Sample_Rate":""}
	i=1
	chanson_iterable = iter(chanson)
	for propriete in chanson_iterable:
		i+=1
		if (i%2 == 0):
			if propriete.text in proprietes:
				i+=1
				propriete_suivante = next(chanson_iterable)
				dictionnaire[proprietes_sans_espace[propriete.text]] = propriete_suivante.text
	i=0
	write_file.write("<morceau>")
	for j in range(nombre_de_proprietes):
		write_file.write("<"+ proprietes_sans_espace[proprietes[j]] + " value=\"" + dictionnaire[proprietes_sans_espace[proprietes[j]]].replace("&", "&amp;").replace("\"","&quot;") + "\"/>") # on met les propriétés dans le nouveau fichier .XML
	write_file.write("</morceau>\n")

write_file.write("</librairie>\n") # fin du XML
write_file.close()








