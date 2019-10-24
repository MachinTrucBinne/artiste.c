# 2019-10-23

import xml.etree.ElementTree as ET
import datetime

# Quand on importe le XML depuis un fichier :
tree = ET.parse('Musique.xml') # on lit depuis le disque
root = tree.getroot() 

#item = root[0]
#print(item) # <Element 'dict' at 0x109099d70>
#print(item.keys(),item.items()) # [] []

# Quand on importe depuis un string :
# root = ET.fromstring(country_data_as_string)

#print(tree) # <xml.etree.ElementTree.ElementTree object at 0x10fcc6c90>
#print(root) # <Element 'plist' at 0x10fcea350>
#print(type(tree)) # <class 'xml.etree.ElementTree.ElementTree'>
#print(type(root)) # <class 'xml.etree.ElementTree.Element'>
#print(type(root.tag)) # <class 'str'>
#print(type(root.attrib)) # <class 'dict'>
#print(*tree) # TypeError: print() argument after * must be an iterable, not ElementTree
#print(*root) # <Element 'dict' at 0x104ed3d70>
#print(**root) # TypeError: element indices must be integers

#print(root[0]) # <Element 'dict' at 0x104947d70>

#for child in root:
#	print("#", str(child.tag),str(child.attrib))
# donne :
# dict {}

#for child in root[0]:
#	print("#", str(child.tag),str(child.attrib))
# donne :
# key {}
# integer {}
# key {}
# integer {}
# key {}
# date {}
# key {}
# string {}
# key {}
# integer {}
# key {}
# true {}
# key {}
# string {}
# key {}
# string {}
# key {}
# dict {}
# key {}
# array {}


#for child in root[0][17]:
#	print("#", str(child.tag),str(child.attrib))
# donne tous les morceaux :
# key {}
# dict {}
# dict {}
# key {}
# dict {}
# key {}
# dict {}
# key {}
# dict {}
# key {}
# dict {}
# ...
# dict {}
# key {}
# dict {}
# key {}
# dict {}
# key {}
# dict {}
# key {}
# dict {}
# key {}
# dict {}


#for child in root[0][17][1]:
#	print("#", str(child.tag),str(child.attrib))
# donne les propriétés du premier morceau :
# key {}
# integer {}
# key {}
# string {}
# key {}		<--- c'est la clé Artist
# string {}		<--- c'est la valeur de la clé Artist
# key {}
# string {}
# key {}
# string {}
# key {}
# string {}
# key {}
# integer {}
# key {}
# integer {}
# key {}
# integer {}
# key {}
# integer {}
# key {}
# integer {}
# key {}
# integer {}
# key {}
# integer {}
# key {}
# date {}
# key {}
# date {}
# key {}
# integer {}
# key {}
# integer {}
# key {}
# integer {}
# key {}
# integer {}
# key {}
# date {}
# key {}
# integer {}
# key {}
# integer {}
# key {}
# string {}
# key {}
# string {}
# key {}
# string {}
# key {}
# integer {}
# key {}
# integer {}


#print(root[0][17][1]["Artist"]) # TypeError: element indices must be integers

#print(*root[0][17][1])
# donne :
# <Element 'key' at 0x10f850770>
# <Element 'integer' at 0x10f8507d0>
# <Element 'key' at 0x10f850830>
# <Element 'string' at 0x10f850890>
# <Element 'key' at 0x10f8508f0>
# <Element 'string' at 0x10f850950>
# <Element 'key' at 0x10f8509b0>
# <Element 'string' at 0x10f850a10>
# <Element 'key' at 0x10f850a70>
# <Element 'string' at 0x10f850ad0>
# <Element 'key' at 0x10f850b30>
# <Element 'string' at 0x10f850b90>
# <Element 'key' at 0x10f850bf0>
# <Element 'integer' at 0x10f850c50>
# <Element 'key' at 0x10f850cb0>
# <Element 'integer' at 0x10f850d10>
# <Element 'key' at 0x10f850d70>
# <Element 'integer' at 0x10f850dd0>
# <Element 'key' at 0x10f850e30>
# <Element 'integer' at 0x10f850e90>
# <Element 'key' at 0x10f850ef0>
# <Element 'integer' at 0x10f850f50>
# <Element 'key' at 0x10f850fb0>
# <Element 'integer' at 0x10f853050>
# <Element 'key' at 0x10f8530b0>
# <Element 'integer' at 0x10f853110>
# <Element 'key' at 0x10f853170>
# <Element 'date' at 0x10f8531d0>
# <Element 'key' at 0x10f853230>
# <Element 'date' at 0x10f853290>
# <Element 'key' at 0x10f8532f0>
# <Element 'integer' at 0x10f853350>
# <Element 'key' at 0x10f8533b0>
# <Element 'integer' at 0x10f853410>
# <Element 'key' at 0x10f853470>
# <Element 'integer' at 0x10f8534d0>
# <Element 'key' at 0x10f853530>
# <Element 'integer' at 0x10f853590>
# <Element 'key' at 0x10f8535f0>
# <Element 'date' at 0x10f853650>
# <Element 'key' at 0x10f8536b0>
# <Element 'integer' at 0x10f853710>
# <Element 'key' at 0x10f853770>
# <Element 'integer' at 0x10f8537d0>
# <Element 'key' at 0x10f853830>
# <Element 'string' at 0x10f853890>
# <Element 'key' at 0x10f8538f0>
# <Element 'string' at 0x10f853950>
# <Element 'key' at 0x10f8539b0>
# <Element 'string' at 0x10f853a10>
# <Element 'key' at 0x10f853a70>
# <Element 'integer' at 0x10f853ad0>
# <Element 'key' at 0x10f853b30>
# <Element 'integer' at 0x10f853b90>

# print(root[0][17][1].tag,root[0][17][1].attrib) # donne dict {}

#for child in root[0][17][1]:
#	print("#", str(child.tag),str(child.attrib),str(child.text))
# donne :
# key {} Track ID
# integer {} 2400
# key {} Name
# string {} When The Going Gets Tough, The Tough Get Karazzee
# key {} Artist
# string {} !!!
# key {} Album
# string {} Louden Up Now
# key {} Genre
# string {} Indie Rock
# key {} Kind
# string {} Fichier audio MPEG
# key {} Size
# integer {} 15629300
# key {} Total Time
# integer {} 376920
# key {} Disc Number
# integer {} 1
# key {} Disc Count
# integer {} 1
# key {} Track Number
# integer {} 1
# key {} Track Count
# integer {} 10
# key {} Year
# integer {} 2004
# key {} Date Modified
# date {} 2013-09-07T22:49:08Z
# key {} Date Added
# date {} 2015-07-04T02:29:00Z
# key {} Bit Rate
# integer {} 320
# key {} Sample Rate
# integer {} 44100
# key {} Play Count
# integer {} 1
# key {} Skip Count
# integer {} 3
# key {} Skip Date
# date {} 2018-08-30T16:05:26Z
# key {} Normalization
# integer {} 3030
# key {} Artwork Count
# integer {} 1
# key {} Persistent ID
# string {} F54D0BB9AC3D933B
# key {} Track Type
# string {} File
# key {} Location
# string {} file:///Users/nac/Music/iTunes/iTunes%20Media/Music/!!!/Louden%20Up%20Now/01%20When%20The%20Going%20Gets%20Tough,%20The%20Tough%20Get%20Karazzee.mp3
# key {} File Folder Count
# integer {} 5
# key {} Library Folder Count
# integer {} 1

#for child in root[0][17][1]:
#	if (str(child.text) == "Artist"):
#		print("#", str(child.tag),str(child.attrib),str(child.text))
# donne :
# key {} Artist

#for child in root[0][17][1]:
#	if (str(child.text) == "Artist"):
#		next_child = next(root[0][17][1])
#		print("#", str(next_child.tag),str(next_child.attrib),str(next_child.text))
# TypeError: 'xml.etree.ElementTree.Element' object is not an iterator

#for child in root[0][17][1]:
#	if (str(child.text) == "Artist"):
#		next_child = next(iter(root[0][17][1]))
#		print("#", str(next_child.tag),str(next_child.attrib),str(next_child.text))
# key {} Track ID


#iterate_this = iter(root[0][17][1])
#for child in iterate_this:
#	if (str(child.text) == "Artist"):
#		next_child = next(iterate_this)
#		print("#", str(next_child.tag),str(next_child.attrib),str(next_child.text))
# string {} !!!
# victoire !

#iterate_this = iter(root[0][17][1])
#for child in iterate_this:
#	if (str(child.text) == "Artist"):
#		next_child = next(iterate_this)
#		print("#",str(next_child.text))
# !!!


#iterate_this = iter(root[0][17][2])
#for child in iterate_this:
#	if (str(child.text) == "Artist"):
#		next_child = next(iterate_this)
#		print("#",str(next_child.text))
# rien ...

#for child in root[0][17][3]:
#	print("#", str(child.tag),str(child.attrib),str(child.text))
# ok
# il faut y aller sur les clés impaires seulement car on a :
# key
# dict		<--- on veut ça, i=1
# key
# dict		<--- on veut ça, i=3
# key
# dict		<--- on veut ça, i=5
# ...

#iterate_this = iter(root[0][17][3])
#for child in iterate_this:
#	if (str(child.text) == "Artist"):
#		next_child = next(iterate_this)
#		print("#",str(next_child.text))
# !!!

#iterate_this = iter(root[0][17][437])
#for child in iterate_this:
#	if (str(child.text) == "Artist"):
#		next_child = next(iterate_this)
#		print("#",str(next_child.text))
# All That Remains


#print(len(root[0][17][1::2]))

artistes = [];
for song in root[0][17][1::2]: # on ne regarde que les positions impaires
	iterate_this = iter(song)
	for child in iterate_this:
		if (str(child.text) == "Artist"):
			next_child = next(iterate_this)
			artist = str(next_child.text)
			if artist not in artistes:
				artistes.append(artist)
				#print(artist)

artistes.sort() # pour mettre les artistes en ordre alphabétique

write_file = open("artistes_extraits.txt","wt") # On ouvre le fichier d'écriture
write_file.write(str(datetime.date.today()) + "\n\nArtistes iTunes\n")
write_file.write("\nIl y a {} artistes trouvés :\n".format(len(artistes)))
for artiste in artistes:
    print(artiste)
    write_file.write("\n" + artiste)

write_file.close() # on ferme le fichier d'écriture












#		print("#", str(root[0][17][1][child+1].tag),str(root[0][17][1][child+1].attrib),str(root[0][17][1][child+1].text))







