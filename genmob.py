import random

def generationmonstre(nom):
    pv = random.randint(5, 20)
    force = random.randint(3, 8)
    armure = random.randint(0, 5)
    monmonstre = [nom, pv, force, armure]
    return monmonstre
