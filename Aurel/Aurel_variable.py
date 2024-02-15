import re
import pandas as pd

# Population pour chaque arrondissement parisien
population_paris = {
    "PARIS 1ER ARRDT": 28365,
    "PARIS 2E ARRDT": 20654,
    "PARIS 3E ARRDT": 17315,
    "PARIS 4E ARRDT": 28184,
    "PARIS 5E ARRDT": 60404,
    "PARIS 6E ARRDT": 44517,
    "PARIS 7E ARRDT": 57100,
    "PARIS 8E ARRDT": 38582,
    "PARIS 9E ARRDT": 24603,
    "PARIS 10E ARRDT": 111116,
    "PARIS 11E ARRDT": 153307,
    "PARIS 12E ARRDT": 208518,
    "PARIS 13E ARRDT": 181454,
    "PARIS 14E ARRDT": 138550,
    "PARIS 15E ARRDT": 225362,
    "PARIS 16E ARRDT": 170358,
    "PARIS 17E ARRDT": 173686,
    "PARIS 18E ARRDT": 195022,
    "PARIS 19E ARRDT": 187276,
    "PARIS 20E ARRDT": 202950,
}

# Superficie pour chaque arrondissement parisien
superficie_paris = {
    "PARIS 1ER ARRDT": 2.891,
    "PARIS 2E ARRDT": 9.92,
    "PARIS 3E ARRDT": 11.71,
    "PARIS 4E ARRDT": 16.02,
    "PARIS 5E ARRDT": 2.541,
    "PARIS 6E ARRDT": 2.153,
    "PARIS 7E ARRDT": 4.088,
    "PARIS 8E ARRDT": 7.801,
    "PARIS 9E ARRDT": 2.182,
    "PARIS 10E ARRDT": 2.893,
    "PARIS 11E ARRDT": 19.22,
    "PARIS 12E ARRDT": 20.09,
    "PARIS 13E ARRDT": 7.15,
    "PARIS 14E ARRDT": 13.71,
    "PARIS 15E ARRDT": 15.85,
    "PARIS 16E ARRDT": 16.37,
    "PARIS 17E ARRDT": 14.22,
    "PARIS 18E ARRDT": 10.59,
    "PARIS 19E ARRDT": 4.773,
    "PARIS 20E ARRDT": 5.984,
}


# Fonction qui va garder seulement le numéro de l'arrondissement
def extraire_chiffres(texte):
    chiffres = re.findall(r'\d+', texte)
    return chiffres[0]