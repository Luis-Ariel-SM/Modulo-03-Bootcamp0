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

    while len(baraja) != len (br):        
        n = random.randint(0,len(baraja)-1)
        while baraja[n] in br:
            n = random.randint(0,len(baraja)-1)
        br.append (baraja[n])       

    baraja[:] = br
    return baraja 

def repartir (b, jugadores, cartas): # Funcion para repartir una cantidad de baraja segun cantidad de jugadores
    res = []
    for p in range (jugadores):
        res.append([])
    for ic in range (cartas):
        for ij in range (jugadores):
            carta = b.pop(0)
            res[ij].append(carta)
    return res   
    
def invertir (b): # Funcion para invertir las listas
    for i in range (len(b)//2):
        aux = b [i]
        b [i] = b [-1-i]
        b [-1-i] = aux