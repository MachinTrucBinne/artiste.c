# 2019-10-27
# Pour mettre les informations du fichier Musique.XML produit par iTunes dans un data frame Pandas
# Le fichier Musique.XML doit être dans le directory du code Python.

import xml.etree.ElementTree as ET
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# On importe les données XML :
tree = ET.parse('Musique.xml')
root = tree.getroot() 

# La liste des propriétés d'un morceau qu'on veut
proprietes = ["Name","Artist","Album","Genre","Kind","Size","Total Time","Disc Number","Disc Count","Track Number","Track Count","Year","Bit Rate","Sample Rate"]
dictionnaire = {"Id":[],"Name":[],"Artist":[],"Album":[],"Genre":[],"Kind":[],"Size":[],"Total Time":[],"Disc Number":[],"Disc Count":[],"Track Number":[],"Track Count":[],"Year":[],"Bit Rate":[],"Sample Rate":[]}
nombre_de_proprietes = len(proprietes)
id=0 # le id de la chanson

for chanson in root[0][17][1::2]: # on ne regarde que les positions impaires
	id=id+1
	dictionnaire["Id"].append(id)
	for prop in proprietes[:]:
		dictionnaire[prop].append("")
	i=1
	chanson_iterable = iter(chanson)
	for propriete in chanson_iterable:
		i+=1
		if (i%2 == 0):
			if propriete.text in proprietes:
				i+=1
				propriete_suivante = next(chanson_iterable)
				dictionnaire[propriete.text][id-1] = propriete_suivante.text
	i=0


df = pd.DataFrame(data=dictionnaire,columns=proprietes) # on met le dictionnaire dans un data frame Pandas
del dictionnaire # on efface libère la mémoire de dictionnaire désormais inutile

print(df.shape) # on regarde la taille du data frame
#df.info() # on regarde les informations du df
#print(df.head()) # on regarde les premières données du df
#print(df.tail()) # on regarde les dernières données du df
#print(df.columns) # pour avoir le nom des colonnes
#print(df.dtypes) # on regarde le type de données dans les colonnes

# On change le type de données vers des colonnes de nombres :
df[df.columns.values.tolist()[5:]] = df[df.columns.values.tolist()[5:]].apply(pd.to_numeric) # pas joli mais ça marche
#print(df.dtypes) # on regarde le type de données dans les colonnes
#print(df["Year"].mean()) # pour avoir une moyenne sur les années

print(*df["Artist"].drop_duplicates().sort_values().values) # pour afficher tous les artistes
print(df['Year'].describe()) # pour avoir des informations sur les années (count, mean, std, min, 25%, 50%, 75%, max)


# Pour avoir le nombre d'éléments par année, ordonnée selon l'année :
nombre_de_tounes_par_an = df['Year'].value_counts(normalize=False, sort=True, ascending=False, bins=None, dropna=True).sort_index()
print(nombre_de_tounes_par_an)
nombre_de_tounes_par_an.plot(kind='bar')
plt.show()

# Pour avoir la durée moyenne (en minutes) des tounes selon l'année :
#duree_moyenne_par_an = df.groupby('Year')['Total Time'].mean()/60000
#print(duree_moyenne_par_an)
#duree_moyenne_par_an.plot(kind='bar')
#plt.show()
# Il ne semble pas y avoir de corrélation entre l'année et la durée de la toune.

# Pour avoir le bit rate moyen (en kbps) des tounes selon l'année :
#bitrate_moyen_par_an = df.groupby('Year')['Bit Rate'].mean()
#print(bitrate_moyen_par_an)
#bitrate_moyen_par_an.plot(kind='bar')
#plt.show()







