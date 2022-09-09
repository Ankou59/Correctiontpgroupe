def gestiondegats(pvdef, forceatk, armuredef):
    if (forceatk > armuredef):
        return pvdef - (forceatk-armuredef)
    else:
        return pvdef - 1
