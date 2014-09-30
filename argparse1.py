import argparse
import logging
parser = argparse.ArgumentParser()

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
        if (verifPositif(pct) == False):
            print ("Le pourcentage doit être positive !")
            exit(1)
        elif (verifInfCent(pct) == False):
            print ("Le pourcentage doit être inférieur à 100 !")
            exit(1)
        else:
            return pct
    except ValueError:
        print (pct + " n'est pas un entier !")
        exit(1)


'''Fonction qui vérifie que le pourcentage est positif'''
def verifPositif(pct):
    if pct > 0:
        return True
    else:
        return False


'''Fonction qui vérifie que le pourcentage est inférieur à 100'''
def verifInfCent(pct):
    if pct < 100:
        return True
    else:
        return False


'''Si les attributs sont renseignés on va vérifier le pourcentage'''
if args.genre:
    verifPourcentage(args.genre[1])

if args.sousgenre:
    verifPourcentage(args.sousgenre[1])

if args.artiste:
    verifPourcentage(args.artiste[1])


'''Affichage'''
print("Test")
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
    print("La playlist contient le titre " + (args.titre))