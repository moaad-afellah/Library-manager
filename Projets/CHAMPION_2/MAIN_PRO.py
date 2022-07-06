from DIFFERENCE import matchJoue
from TOTAL_PIONT import calculPoint, Selectchampion
from AFFICHAGE import afficherScore, afficherTableau

donneehusa = {"name": "HUSA", "point": 0}
donneefcb = {"name": "FCB", "point": 0}
donneereal = {"name": "REAL", "point": 0}

print("match 1 : FCB vs HUSA")
result = matchJoue()
donneefcb["point"],donneehusa["point"] = calculPoint(donneefcb, donneehusa, result[0], result[1])
afficherScore( result[0], result[1], donneefcb, donneehusa)
afficherTableau(donneehusa,donneefcb, donneereal)

print()

print("match 2 : FCB vs REAL")

result = matchJoue()
donneefcb["point"], donneereal["point"]= calculPoint(donneefcb, donneereal, result[0], result[1])
afficherScore( result[0], result[1], donneefcb, donneereal)
afficherTableau(donneehusa,donneefcb, donneereal)

print()

print("match 3 : HUSA vs REAL ")
result = matchJoue()
donneehusa["point"],donneereal["point"] = calculPoint(donneehusa, donneereal, result[0], result[1])
afficherScore( result[0], result[1], donneehusa, donneereal)
afficherTableau(donneehusa,donneefcb, donneereal)

print(Selectchampion(donneehusa, donneefcb,donneereal))
