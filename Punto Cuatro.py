#Problema planteado: Mi mamá me manda a comprar P panes a 300 cada uno, M bolsas de leche a 3300 cada una y H huevos a 350 cada uno. Hacer un programa que me diga las vueltas (o lo que quedo debiendo) cuando me da un billete de B pesos.

#Declarando constantes
PRECIO_PAN:int
PRECIO_PAN=300
PRECIO_LECHE:int
PRECIO_LECHE=3300
PRECIO_HUEVO:int
PRECIO_HUEVO=350

#Función para calcular las vueltas
def vueltas(cantidadPan:int,cantidadLeche:int,cantidadHuevo:int,billete:int)->int:
    totalVueltas=billete-(PRECIO_PAN*cantidadPan+PRECIO_LECHE*cantidadLeche+PRECIO_HUEVO*cantidadHuevo)
    return totalVueltas

if __name__=="__main__":
    #Declarando e inicializando variables
    cantidadPan=int(input("Ingrese la cantidad de panes comprados: "))
    cantidadLeche=int(input("Ingrese la cantidad de bolsas de lecha compradas: "))
    cantidadHuevo=int(input("Ingrese la cantidad de huevos comprados: "))
    billete=int(input("Ingrese el valor del billete con el que se pagó la compra: "))

    vueltasCompra=vueltas(cantidadPan,cantidadLeche,cantidadHuevo,billete)#Se imprime una respuesta distinta dependiendo si hay vueltas, si se debe o si no hay ninguno de los dos casos.
    if vueltasCompra>0:
        print("Si compró "+  str(cantidadPan)+ " panes, "+str(cantidadLeche)+ " bolsas de leche y " +str(cantidadHuevo)+ " huevos pagando con un billete de " + str(billete) +",las vueltas son " + str(vueltasCompra)+ " pesos.")
    elif vueltasCompra==0:
        print("Si compró "+  str(cantidadPan)+ " panes, "+str(cantidadLeche)+ " bolsas de leche y " +str(cantidadHuevo)+ " huevos pagando con un billete de " + str(billete) +", no hay vueltas, ni queda debiendo.")
    else:
        print("Si compró "+  str(cantidadPan)+ " panes, "+str(cantidadLeche)+ " bolsas de leche y " +str(cantidadHuevo)+ " huevos pagando con un billete de " + str(billete) +", usted queda debiendo " + str(-vueltasCompra)+ " pesos.")