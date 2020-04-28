import P01_ModuloCartas

b1 = (P01_ModuloCartas.crea_baraja())
b2 = (P01_ModuloCartas.crea_baraja())

print (b1)
print (b2)

print (P01_ModuloCartas.mezclar_baraja(b1))

b = P01_ModuloCartas.crea_baraja()
manos = P01_ModuloCartas.repartir(b,3,5)

print(manos)
