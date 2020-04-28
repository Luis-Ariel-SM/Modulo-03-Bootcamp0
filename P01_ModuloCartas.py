import random

palos = ('O','C','E','B')
cartas = ('A','2','3','4','5','6','7','S','C','R')

def crea_baraja ():

    baraja = []

    for palo in palos:
        for carta in cartas:
            naipe = carta + palo
            baraja.append (naipe)

    return (baraja)

def mezclar_baraja (baraja):
    br = []
    i = 0
    while i < 40:
        n = random.randint(0,39)
        while baraja[n] in br:
            n = random.randint(0,39)
        br.append (baraja[n])
        i += 1

    b = br
    return b  

def repartir (b, jugadores, cartas):
    res = []
    for p in range (jugadores):
        res.append([])
    for ic in range (cartas):
        for ij in range (jugadores):
            carta = b.pop(0)
            res[ij].append(carta)
    return res   
    
