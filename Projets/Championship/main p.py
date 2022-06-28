from difference import matchJoue
from totalPOIN import calculPoint , Selectchampion
from affichage import afficherScore, afficherTableau

pointHusa = 0
pointReal = 0
pointBarca = 0

print("match 1 : FCB vs HUSA")
result = matchJoue()
pointBarca, pointHusa = calculPoint(pointBarca, pointHusa, result[0], result[1])
afficherScore(pointBarca, pointHusa, result[0], result[1], "FCB", "HUSA")
afficherTableau(pointHusa, pointBarca, pointReal)

print()

print("match 2 : FCB vs REAL")
result = matchJoue()
pointBarca, pointReal = calculPoint(pointBarca, pointReal, result[0], result[1])
afficherScore(pointBarca, pointReal, result[0], result[1], "FCB", "RMA")
afficherTableau(pointHusa, pointBarca, pointReal)

print()

print("match 3 : HUSA vs REAL ")
result = matchJoue()
pointHusa, pointReal = calculPoint(pointHusa, pointReal, result[0], result[1])
afficherScore(pointHusa, pointReal, result[0], result[1], "HUSA", "RMA")
afficherTableau(pointHusa, pointBarca, pointReal)

print(Selectchampion(pointHusa, pointBarca, pointReal))