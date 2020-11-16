import baraja

ordenada = baraja.creaBaraja()
print("Esta es la primera baraja: ", ordenada) 

otraBaraja = baraja.creaBaraja()
print("Esta es la segunda baraja nada mas crearla:", otraBaraja)

baraja.barajar(otraBaraja)
print("Y ahora la he barajado: ", otraBaraja)
print("Para que fernando se lo crea, la baraja primera: ", ordenada)



