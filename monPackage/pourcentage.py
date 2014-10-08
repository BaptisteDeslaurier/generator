'''
Created on 8 oct. 2014

@author: etudiant
'''
import logging

'''Fonction de vérification des poucentages'''
def verifPourcentage(arg):
    try:
        pct = int(arg)
        if pct<0:
            pct = abs(pct)
            logging.warning('La quantité saisie doit etre positive')
            logging.info('Nombre négatif transformé en positif: ' + str(pct))
        elif pct>100:
            pct = None
            logging.warning('La quantité saisie est supérieur à 100')
            logging.info('Nombre supérieur à 100 transformé en : ' + str(pct))
    except ValueError:
        logging.error('Impossible de convertir ' + arg + ' en nombre entier !')
        logging.info("***** Fin du programme *****")
        exit(1)


'''Fonction de gestion des arguments'''
def gestionPctage(typeArg):
    i = 0
    ligneList = 1
    j = 0
    ligneList2 = 1
    somme = 0

    '''Tant que la liste du type d'argument passé à encore une ligne'''
    while ligneList <= len(typeArg):
        logging.info("Utilisation de la fonction pour vérifier que le pourcentage est entre 0 et 100")
        '''Vérification du %'''
        verifPourcentage(typeArg[i][1])
        somme = somme + int(typeArg[i][1])
        ligneList = ligneList + 1
        i = i + 1
    logging.info('Total des sommes des %: ' + str(somme))
    if somme > 100:
        '''Tant que la liste du type d'argument passé à encore une ligne'''
        logging.info('Remise du total des % à 100 grace à la proportionalité')
        while ligneList2 <= len(typeArg):
            '''Round() permet d'arrondir à l'entier le plus proche'''
            typeArg[j][1] = round(int(typeArg[j][1])*100/somme)
            j = j + 1
            ligneList2 = ligneList2 + 1