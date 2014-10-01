#!/usr/bin/python3
# -*- coding: utf-8 -*-

import argparse
import logging
logging.basicConfig(filename="monLog.log", level=logging.DEBUG)
parser = argparse.ArgumentParser()

logging.info("***** Démarrage du programme *****")

'''argument positionnel'''
parser.add_argument("temps", help="durer de la playlist en minute", type=int)
parser.add_argument("nomfichier", help="nom donner a la playlist")
parser.add_argument("formatfichier", help="extension de la playlist", choices=['m3u', 'xspf', 'pls'])

'''argument optionnel'''
parser.add_argument("-G", "--genre", help="genre et pourcentage du genre voulu dans la playlist", nargs=2)
parser.add_argument("-g", "--sousgenre", help="sous genre et pourcentage du sous genre voulu dans la playlist", nargs=2)
parser.add_argument("-A", "--artiste", help="artiste et pourcentage de l'artiste voulu dans la playlist", nargs=2)
parser.add_argument("-a", "--album", help="album voulu dans la playlist")
parser.add_argument("-t", "--titre", help="titre voulu dans la playlist")

args = parser.parse_args()


'''Fonction de vérification des poucentages'''
def verifPourcentage(arg):
    try:
        pct=int(arg)
        if pct<0:
            pct = abs(pct)
            logging.warning('La quantité saisie doit etre positive')
            logging.info('Nombre négatif transformé en positif: ' + str(pct))
        elif pct>100:
            pct = None
            logging.warning('La quantité saisie est supérieur à 100')
            logging.info('Nombre supérieur à 100 transformé en : ' + str(pct))
        return True
    except ValueError:
        logging.error('Impossible de convertir ' + arg + ' en nombre entier !')
        logging.info("***** Fin du programme *****")
        exit(1)

'''Vérifications'''
'''Vérification d'un temps positif'''
logging.info("Utilisation de la fonction pour vérifier que le temps est un entier positif")
if args.temps<0 :
    print ("Le temps doit être positive !")
    logging.error("le temps " + str(args.temps) + " n'est pas un entier positif")
    exit(1)

'''Si les attributs sont renseignés on va vérifier le pourcentage'''
if args.genre:
    logging.info("Utilisation de la fonction pour vérifier que le pourcentage est entre 0 et 100")
    verifPourcentage(args.genre[1])

if args.sousgenre:
    logging.info("Utilisation de la fonction pour vérifier que le pourcentage est entre 0 et 100")
    verifPourcentage(args.sousgenre[1])

if args.artiste:
    logging.info("Utilisation de la fonction pour vérifier que le pourcentage est entre 0 et 100")
    verifPourcentage(args.artiste[1])


'''Affichage
print("Création de la playlist " + (args.nomfichier) + "." + (args.formatfichier) + " d'une durée de " + str(args.temps) + " minutes")
if args.genre:
    print("La playlist contient " + str(args.genre[1]) + "% du genre " + (args.genre[0]))
if args.sousgenre:
    print("La playlist contient " + str(args.sousgenre[1]) + "% du sous genre " + (args.sousgenre[0]))
if args.artiste:
    print("La playlist contient " + str(args.artiste[1]) + "% de l'artiste " + (args.artiste[0]))
if args.album:
    print("La playlist contient l'album " + (args.album))
if args.titre:
    print("La playlist contient le titre " + (args.titre))'''

logging.info("Tout est bon !!!")
logging.info("***** Fin du programme *****")