# README

---

Pour afficher la liste des artistes dans une librairies iTunes sur macOS il suffit d'ouvrir un terminal et de faire :
```cd ~/Music/iTunes/iTunes\ Media/Music ; ls```

Ici il s'agit d'afficher les artistes d'une manière différente. D'abord, iTunes peut produit un fichier XML en allant dans le menu :
```Fichier/Bibliothèque/Exporter la bibliothèque...```

Maintenant qu'on a un fichier XML il faut extraire les artistes du fichier. Voici deux codes similaires pour faire cela :

1. *artistes.c*, en langage C,
2. *artistes.py*, en langage Python 3.

Il faut mettre le fichier XML dans le répertoire du code.

Le code en C ne sort pas les artistes en ordre alphabétique mais en ordre d'ajout à la librairie.

Le code en Python sort les artistes en ordre alphabétique.

Le nombre d'artistes calculé par le code Python est bon mais celui en C pas toujours, selon l'ordre d'ajout des artistes dans la librairie.

