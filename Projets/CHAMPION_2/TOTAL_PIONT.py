def calculPoint(pointEquipe1, pointEquipe2, scoreEquipe1, scoreEquipe2):
    if scoreEquipe1 == scoreEquipe2:
        return pointEquipe1["point"] + 1, pointEquipe2["point"] + 1

    if scoreEquipe1 > scoreEquipe2:
        return pointEquipe1["point"] + 3, pointEquipe2["point"]

    if scoreEquipe1 < scoreEquipe2:
        return pointEquipe1["point"], pointEquipe2["point"] + 3


def Selectchampion(pointEquipe1, pointEquipe2, pointEquipe3):
    if pointEquipe1["point"] > pointEquipe2["point"] and pointEquipe1["point"] > pointEquipe3["point"]:
        return "Bravo HUSA"
    if pointEquipe2["point"] > pointEquipe1["point"] and pointEquipe2["point"] > pointEquipe3["point"]:
        return "Bravo FCB"
    if pointEquipe3 ["point"]> pointEquipe1["point"] and pointEquipe3["point"] > pointEquipe2["point"]:
        return "Bravo RMA"

    return "No Champion"
