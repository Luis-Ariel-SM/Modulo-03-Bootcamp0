import random

class Baraja ():
    palos = ('O','C','E','B')
    cartas = ('A','2','3','4','5','6','7','S','C','R')

    def __init__(self):

               
        self.naipes = []
        for palo in self.palos:

            for carta in self.cartas:
                
                naipe = carta + palo
                self.naipes.append (naipe)

    
    def mezclar (self):

        br = []
        i = 0
        while len(self.naipes) != len (br):        
            n = random.randint(0,len(self.naipes)-1)
            while self.naipes[n] in br:
                n = random.randint(0,len(self.naipes)-1)
            br.append (self.naipes[n]) 

        self.naipes[:] = br
              
    
    def repartir (self, players, cards):

        res = []
        for p in range (jugadores):
            res.append([])
        for ic in range (cartas):
            for ij in range (jugadores):
                carta = self.naipes.pop(0)
                self.mano[ij].append(carta)
        
        def recoger (self):
            self.naipes
            self.mano

b = Baraja ()
b.mezclar()
print(b.naipes)