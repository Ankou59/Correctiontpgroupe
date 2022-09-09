from genmob import *


def creationmob():
    liste_monstres = ["Ponyo", "Xavier", "Nadia", "Romero", "Titi", "Emeric", "Laetissia", "Helene"]
    nommonstre = random.choice(liste_monstres)
    return generationmonstre(nommonstre)