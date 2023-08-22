import ahorcado
import adivinanza


print("=================================================")
print("ESCOJA SU JUEGO")
print("=================================================")


print("(1) ahorcado (2) adivinanza")

juego=int(input("cual es el juego?"))

if(juego == 1):
    print("jugando ahorcado")
elif(juego == 2):
    print("jugando adivinanza")
