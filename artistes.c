/*
PRODUIT PAR: NAC

Novembre 2014

UTILITÉ: extraire les artistes du fichier Musique.xml produit par iTunes. Fonctionne sur MAC OS (du moins 10.7)

À FAIRE :
1) Télécharger les Xcode command line tools si ce n'est pas déjà fait.
2) Télécharger Sublime Text pour compiler si ce n'est pas déjà fait (car gcc semble crasher à la compilation).
3) S'assurer que le nom du présent fichier .c soit nommé artistes.c (au pluriel).
4) Compiler le présent fichier artistes.c avec Sublime Text (cmd+b).
5) S'assurer d'avoir le fichier Musique.xml produit par iTunes dans le même dossier que l'exécutable.
6) Exécuter l'exécutable artistes.

Le fichier artistes_extraits.txt devrait contenir tous les artistes de votre librairie iTunes (dans l'ordre d'ajout chronologique).

Si ça bug, tant pis.

*/

#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <dirent.h>


int main(int argc, char *argv[], char PWD[])
{
    /***************************************************************************/
    /*************************** Préliminaires *********************************/
    /***************************************************************************/

    int d;
    char buffer_PWD[255]; // le string qui contiendra le chemin vers l'executable, le fichier de lecture et le fichier d'écriture.
    sprintf(buffer_PWD,"%s",*argv); // on met le path dans buffer_PWD
    int l = strlen(buffer_PWD); // simplement un entier qui nous informe de la longueur du path.

    /***************************************************************************/
    /************************* Un peu de politesse *****************************/
    /***************************************************************************/
    
    printf("\nBonjour. Nous allons extraire le nom des artistes d'un fichier XML produit par iTunes. Assurez-vous d'avoir le fichier  \"Musique.xml\"  dans le meme dossier que l'executable  \"artiste\".\n");

    /**************************************************************************/
    /********************Ouverture du fichier de lecture **********************/  
    /**************************************************************************/

    char nom_du_fichier_de_lecture [12];
    sprintf(nom_du_fichier_de_lecture, "Musique.xml");

    for(d=l-8;d<254;d++){buffer_PWD[d] = NULL;} // on efface les lettres en trop du path car contient "artiste" (le nom de l'executable) en trop.
    for(d=l-8;d<l+3;d++){buffer_PWD[d] = nom_du_fichier_de_lecture[d-(l-8)];} // on met "Musique.xml" dans le path du fichier de lecture.
    printf("\nVoici le fichier de lecture :\n%s\n",buffer_PWD);


    FILE *read_file; // Ouverture du fichier de lecture
    read_file = fopen(buffer_PWD, "rt");

    if(read_file==NULL)
        {
        printf("Erreur, le fichier de lecture n'a pu etre ouvert. Cause probable du problème : le nom du fichier .c ici présent doit être \"artistes.c\" et rien d'autre! (artistes au pluriel, pas au singulier!)\n");
        return 1;
        }
    else
       printf("Le fichier de lecture a ete ouvert correctement.\n");
  

    /**************************************************************************/
    /********************Ouverture du fichier d'écriture **********************/  
    /**************************************************************************/

    char nom_du_fichier_decriture [22];
    sprintf(nom_du_fichier_decriture, "artistes_extraits.txt");

    for(d=l-8;d<254;d++){buffer_PWD[d] = NULL;} // on efface les lettres en trop du path car contient encore "Musique.xml".
    for(d=l-8;d<l+13;d++){buffer_PWD[d] = nom_du_fichier_decriture[d-(l-8)];} // on met "artistes_extraits.txt" dans le path du fichier d'ecriture.
    printf("\nVoici le fichier d'ecriture :\n%s\n",buffer_PWD);

    
    FILE *write_file;// Ouverture du fichier d'écriture
    write_file = fopen(buffer_PWD, "wt+");

    if(write_file==NULL)
    {
        printf("Erreur, le fichier d'ecriture n'a pu etre ouvert\n");
        return 1;
    }
    else
        printf("Le fichier d'ecriture a ete ouvert correctement\n");

    /**************************************************************************/
    /***Poser toutes les variables qu'on aura besoin et allocation de mémoire**/  
    /**************************************************************************/

    // Poser les string qu'on va rechercher et transférer
    char artiste_debut[26]; sprintf(artiste_debut, "<key>Artist</key><string>"); //car les artistes du log sont précédés de <key>Artist</key><string>
    char artiste_debut_buffer[255]; //string qui bouffe du log et viendra se comparer à artiste_debut
    char artiste_fin[255]; sprintf(artiste_fin, "</string>"); //car les artistes du log sont suivit de </string>
    char artiste_fin_buffer[255]; // string qui bouffe du log par itération et viendra se comparer à artiste_fin
    char artiste_nouveau[255]; //un nouvel artiste trouvé!
    int n_nouveau=0;//longueur du vieil artiste
    char artiste_vieux[255]; //l'ancien artiste trouvé (viendra se comparer à artiste_nouveau pour s'assurer de ne pas avoir de doublons consécutifs)
    int n_vieux = 0;// longueur du nouvel artiste
    
    // Poser des entiers quelconques
    int i;
    int k;
    int Nombredartistes = 0;  // Compte le nombre d'artistes
        
    /**************************************************************************/
    /***** On charge le fichier de lecture dans un tableau de caractères ******/  
    /**************************************************************************/
    
    char * BufferLogFile;   // Tableau qui contient tout le fichier de lecture
    int LongueurLogFile = 0;    // Longueur en caractères du fichier de lecture
    
    // On lit le fichier une fois pour compter le nombre de caractères
    while(!feof(read_file))
    {
        fgetc(read_file);
        LongueurLogFile++;
    }
        
    rewind(read_file); // On revient au début du fichier de lecture
    
    if((BufferLogFile = (char *) malloc(LongueurLogFile*sizeof(char))) == NULL)
        printf("\nMémoire insuffisante pour BufferLogFile\n");
    else
        printf("\nMemoire OK pour BufferLogFile.\n");
        printf("Il y a %i caracteres dans le fichier de lecture.\n",LongueurLogFile);
  
    for(i = 0; i < LongueurLogFile; i++)
       BufferLogFile[i] = fgetc(read_file); // on transfert le fichier de lecture dans un buffer (plus facile à manier qu'un fichier de lecture)

    /**************************************************************************/
    /***** L'algorithme en puissance qui va faire le travail voulu ************/  
    /**************************************************************************/

    printf("\n\nVoici les artistes (selon l'ordre chronologique d'ajout dans la librairie iTunes) :\n\n");
    for (i = 0; i < LongueurLogFile-75; i++)
    { 
        for (k=0;k<25;k++){artiste_debut_buffer[k] = BufferLogFile[i+k];} // on bouffe une partie du log

        if (strcmp(artiste_debut_buffer,artiste_debut) == 0) // si la partie qu'on vient de copier est "<key>Artist</key><string>" alors on a trouvé un artiste!
        {
            n_vieux = n_nouveau;
            n_nouveau=0;

            for (k=0 ; k<256 ; k++){artiste_vieux[k] = NULL;} //on réinitialise le vieil artiste
            for (k=0 ; k<n_vieux ; k++){artiste_vieux[k] = artiste_nouveau[k];} //on envoie l'ancien nouveau artiste au vieil artiste
            for (k=0 ; k<256 ; k++){artiste_nouveau[k] = NULL;} //on réinitialise le nouvel artiste

            while (strcmp(artiste_fin_buffer,artiste_fin) != 0) // on cherche la fin du nouvel artiste
            {
                for (k=0 ; k<9 ; k++){artiste_fin_buffer[k] = BufferLogFile[i+k+n_nouveau+25];} // on bouffe du log, de plus en plus à droite jusqu'à ce qu'on ait trouvé la fin de l'artiste
                n_nouveau++;
            }

            for (k=0;k<n_nouveau-1;k++){artiste_nouveau[k] = BufferLogFile[i+k+25];} // on envoie l'artiste dans le string artiste_nouveau

            if (strcmp(artiste_nouveau,artiste_vieux) != 0) // pour s'assurer qu'on ne réécrit pas le même artiste deux fois
            {   
                Nombredartistes++; // le nombre d'artiste augmente
                for (k=0 ; k<n_nouveau ; k++)
                {
                    if (artiste_nouveau[k] == '#' && artiste_nouveau[k+1] == '3' && artiste_nouveau[k+2] == '8' && artiste_nouveau[k+3] == ';'){k=k+4;} // car le log XML produit par iTunes génère des & de marde (i.e. de la forme "&#38;")
                    printf("%c", artiste_nouveau[k]);
                    fprintf(write_file,"%c",artiste_nouveau[k]);
                }
                printf("\n");
                fprintf(write_file,"\n");
            }
        } 
    }

    /***************************************************************************/
    /************************** Le mot de la fin *******************************/
    /***************************************************************************/

    printf("\nTotal : %i artistes.\n\n",Nombredartistes);
    fprintf(write_file,"\nTotal : %i artistes.\n\n",Nombredartistes);

    /***************************************************************************/
    /************************* Fin des procédures ******************************/
    /***************************************************************************/

    if(BufferLogFile != NULL)free(BufferLogFile);

    fclose(write_file);
    fclose(read_file);

    return 0;
}
//EOF
