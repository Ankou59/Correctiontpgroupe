from flask import Flask, render_template, request, send_file, redirect, url_for, Response, redirect

app = Flask(__name__)

import sys
import os
from personnages  import *
from compteurkill  import *
from gestioncombat  import *
from creationmob  import *

global joueurs
joueurs = []

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.form:
        
        pseudo = request.form["pseudo"] 
        global joueurs
        joueurs.append(pseudo)
        compteurkill = 0
        liste_monstre_vaincus = []

        monpersonnage = personnage(pseudo, 20,6,3)

        while monpersonnage[1] > 0:
            monstreennemi = creationmob()
            gestioncombat(monpersonnage, monstreennemi)

            if monpersonnage[1] > 0:
                compteurkill = compteurennemistues(compteurkill)
                liste_monstre_vaincus.append(monstreennemi[0])
            
        return render_template("home.html", pseudo=pseudo, compteurkill=compteurkill, liste_monstre_vaincus=liste_monstre_vaincus, joueurs=joueurs)
    return render_template("home.html")


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8001)