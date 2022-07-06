def afficherScore( scoreEquipe1, scoreEquipe2, nameEquipe1, nameEquipe2):
    print(nameEquipe1["name"], ' ', scoreEquipe1, '  -  ', scoreEquipe2, ' ', nameEquipe2["name"])


def afficherTableau(donneehusa,donneefcb, donneereal):
    print('      ---------- ')
    print("HUSA: ",donneehusa["point"])
    print("FCB: ", donneefcb["point"])
    print("RMA: ", donneereal["point"])
    print('      ---------- ')
