#Una función que calcula la cantidad de carne de aves en kilos si se tienen N gallinas, M gallos y K pollitos cada uno pesando 6 kilos, 7 kilos y 1 kilo respectivamente.

#Declarando e inicializando constantes
PESO_GALLINAS:int
PESO_GALLINAS=6
PESO_GALLOS:int
PESO_GALLOS=7
PESO_POLLITOS:int
PESO_POLLITOS=1
#Función para calcular la cantidad de carne
def cantidadCarne(cantidadGallinas:int,cantidadGallos:int,cantidadPollitos:int)->int:
    totalCarne=cantidadGallinas*PESO_GALLINAS+cantidadGallos*PESO_GALLOS+cantidadPollitos*PESO_POLLITOS #La cantidad total de carne es igual a la suma de la cantidad de los animales por su peso.
    return totalCarne
if __name__=="__main__":
    #Declarando variables con Camelcase y de tipo int dado a que el número de animales es siempre entero.
    cantidadGallinas:int
    cantidadGallos:int
    cantidadPollitos:int
    #Inicializando variables con la función input()
    cantidadGallinas=int(input("Ingrese la cantidad de gallinas: "))
    cantidadGallos=int(input("Ingrese la cantidad de gallos: "))
    cantidadPollitos=int(input("Ingrese la cantidad de pollitos: "))
    
    carneAves=cantidadCarne(cantidadGallinas,cantidadGallos,cantidadPollitos)
    print("La cantidad total de carne de aves en kilos es "+str(carneAves)+" cuando hay "+str(cantidadGallinas)+" gallinas, "+str(cantidadGallos)+" gallos y "+str(cantidadPollitos)+" pollitos.")