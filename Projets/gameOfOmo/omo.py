import random

class Player:
    def __init__(self , name = None):
        self.name =name

    def printMySelf(self):
        print(self.name)


class Omo:
    def __init__(self):
        self.omoData1 = [["_", "_", "_"], ["_", "_", "_"], ["_", "_", "_"]]
        self.omoData2 = ["_", "_", "_", "_", "_", "_", "_", "_", "_"]
        self.gameOver =False

    def isFull(self):
        for i in range(0, 3):
            for j in range(0, 3):
                if self.omoData1[i][j] == "_":
                    return False
        return True


    def check(self):
        for i in range(0,3):
            if self.omoData1[i] == ["o", "o", "o"] or self.omoData1[i] == ["x", "x", "x"]:
                return  True

        return False

    def isGameOver(self):
        return self.gameOver

    def play(self, symbol, coordX, coordY , player=None):
        coordX = int(coordX)
        coordY = int(coordY)

        if self.gameOver or self.isFull():
            print('Game Over')
            return

        if self.omoData1[coordY-1][coordX-1] == "_":
            self.omoData1[coordY-1][coordX-1] = symbol
        else:
            print("error")

        if self.check():
            self.gameOver =True
            print('We have winner')

        self.printOmo()



    def printOmo(self):
        print("**************")
        for line in self.omoData1:
            for element in line:
                print(element, end="    ")
            print()
        print("**************")
        print()

def randomX_O():
    rand = random.randint(0,1)
    if rand == 0:
        return "o"
    else:
        return "x"



while True:
    omo = Omo()
    input()
    while not omo.isGameOver() and  not omo.isFull():
        i = random.randint(1,3)#input('Give i: ')
        j= random.randint(1,3) #input('Give j :')
        omo.play(randomX_O(), i , j)

