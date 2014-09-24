import argparse
parser = argparse.ArgumentParser()

"""argument positionnel"""
parser.add_argument("temps", help="durer de la playlist en minute", type=int)
parser.add_argument("nomfichier", help="nom donner a la playlist")
parser.add_argument("formatfichier", help="extension de la playlist", choices=['m3u', 'xspf', 'pls'])

"""argument optionnel"""
parser.add_argument("-G", "--genre", help="genre et pourcentage du genre voulu dans la playlist", nargs=2)
parser.add_argument("-g", "--sousgenre", help="sous genre et pourcentage du sous genre voulu dans la playlist", nargs=2)
parser.add_argument("-A", "--artiste", help="artiste et pourcentage de l'artiste voulu dans la playlist", nargs=2)
parser.add_argument("-a", "--album", help="album voulu dans la playlist")
parser.add_argument("-t", "--titre", help="titre voulu dans la playlist")

args = parser.parse_args()

def verifPourcentage(arg):
    try:
        return int(arg)
    except ValueError:
        print (arg + " n'est pas un entier !")

verifPourcentage(args.genre[1])
verifPourcentage(args.sousgenre[1])
verifPourcentage(args.artiste[1])


"""
print (args.temps)
print (args.nomfichier)
print (args.formatfichier)

if args.genre:
    print(args.genre)
if args.sousgenre:
    print(args.sousgenre)
if args.artiste:
    print(args.artiste)
if args.album:
    print(args.album)
if args.titre:
    print(args.titre)
"""