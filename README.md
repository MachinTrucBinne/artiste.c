# README

---

## Introduction

Le but ici est d'afficher la liste des artistes dans une librairies iTunes sur macOS.
Une manière simple et efficace est d'ouvrir un terminal et de faire :
```cd ~/Music/iTunes/iTunes\ Media/Music ; ls```

Ici il s'agit d'afficher les artistes à partir du fichier *Musique.xml* produit par iTunes en allant dans le menu :
```Fichier/Bibliothèque/Exporter la bibliothèque...```

Il y a plusieurs manières d'extraire les artistes du fichier *Musique.xml*.

Dans tous les cas, il faut mettre le fichier *Musique.xml* dans le répertoire du code.

---

## Méthode 1

Via le code *artistes.c* en langage C.



---

## Méthode 2

Via le code  *artistes1.py* en langage Python 3.


---

## Méthode 3

Via le code *artistes2.py* en Python 3.


---

## Méthode 4

Via le code *artistes3.py*, en Python 3.
Il crée un nouveau fichier *Musique_extraite.xml* à partir du fichier *Musique.xml*. 
Ensuite il faut ouvrir une session Postgres et importer les données du fichier *Musique_extraite.xml* à l'aide des commandes dans le fichier *artistes3.sql*.

---

## Méthode 5

Via le code *artistes4.py*, en Python 3.
Il met les informations du fichier *Musique.xml* dans un *data frame* Pandas.
C'est utile pour afficher diverses statistiques, e.g. le nombre de morceaux par an. 

---

### Remarque :

1. Le code *artistes.c* ne sort pas les artistes en ordre alphabétique mais en ordre d'ajout à la librairie. Aussi, l enombre d'artistes calculé n'est pas bon, selon l'ordre d'ajout des artistes dans la librairie.
2. Les codes *artistes1.py* et *artistes2.py* sortent les artistes en ordre alphabétique et donnent le bon nombre d'artistes.
3. Pour la méthode 4, les informations sont extraites via des commandes SQL.

---