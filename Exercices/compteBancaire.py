class CompteBancaire:
    def __init__(self, nom = "dupont", solde = 1000):
        self.nom = nom
        self.solde = solde

    def depot(self, somme = 0):
        self.solde = self.solde + somme

    def retrait(self, somme = 0):
        self.solde = self.solde - somme

    def affiche(self):
        print("Le solde du compte bancaire de", self.nom, "est de", self.solde , "euros.")


compte1 = CompteBancaire('Duchmol', 800)
compte1.depot(350)
compte1.retrait(200)
compte1.affiche()
compte2 = CompteBancaire()
compte2.depot(25)
compte2.affiche()