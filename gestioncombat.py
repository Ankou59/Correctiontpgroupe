from gestiondegats import *

def gestioncombat(joueur, monstre):
    while(joueur[1] > 0 and monstre[1] > 0):
        #combat ?
        monstre[1] = gestiondegats(monstre[1], joueur[2], monstre[3])   
        if (monstre[1] > 0):
            joueur[1] = gestiondegats(joueur[1], monstre[2], joueur[3])


    return joueur