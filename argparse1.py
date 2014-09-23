import argparse
parser = argparse.ArgumentParser()

"""argument positionnel"""
parser.add_argument("temps", help="durer de la playlist en minute", type=int)
parser.add_argument("nomfichier", help="nom donner a la playlist")
parser.add_argument("formatfichier", help="extension de la playlist", choices=['m3u', 'xspf', 'pls'])

"""argument optionnel"""
parser.add_argument("--genre", help="genre voulu dans la playlist")
parser.add_argument("--pctgenre", help="pourcentage du genre voulu dans la playlist", type=float)
parser.add_argument("--sousgenre", help="sous genre voulu dans la playlist")
parser.add_argument("--pctsousgenre", help="pourcentage du sous genre voulu dans la playlist", type=float)
parser.add_argument("--artiste", help="artiste voulu dans la playlist")
parser.add_argument("--pctartiste", help="pourcentage de l'artiste voulu dans la playlist", type=float)
parser.add_argument("--album", help="album voulu dans la playlist")
parser.add_argument("--titre", help="titre voulu dans la playlist")

args = parser.parse_args()

print (args.temps)
print (args.nomfichier)
print (args.formatfichier)

if args.genre:
    print (args.genre)
    if args.pctgenre:
        print (args.pctgenre)
if args.sousgenre:
    print (args.sousgenre)
    if args.pctsousgenre:
        print (args.pctsousgenre)
if args.artiste:
    print (args.artiste)
    if args.pctartiste:
        print (args.pctartiste)
if args.album:
    print (args.album)
if args.titre:
    print (args.titre)