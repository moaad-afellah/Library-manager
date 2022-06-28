def calculPoint(pointEquipe1, pointEquipe2, scoreEquipe1, scoreEquipe2):
    if scoreEquipe1 == scoreEquipe2:
        return pointEquipe1 + 1, pointEquipe2 + 1

    if scoreEquipe1 > scoreEquipe2:
        return pointEquipe1 + 3, pointEquipe2

    return pointEquipe1, pointEquipe2 + 3


def Selectchampion(pointEquipe1, pointEquipe2, pointEquipe3):

    if pointEquipe1> pointEquipe2 and pointEquipe1> pointEquipe3:
        return "Bravo HUSA"
    if pointEquipe2 > pointEquipe1 and pointEquipe2 > pointEquipe3:
        return "Bravo FCB"
    if pointEquipe3 > pointEquipe1 and pointEquipe3 > pointEquipe2:
        return "Bravo RMA"

    return "No Champion"

