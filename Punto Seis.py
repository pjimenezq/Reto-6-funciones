#Problema planteado: El número de contagiados de Covid-19 en el país de NuncaLandia se duplica cada día. Hacer un programa que diga el número total de personas que se han contagiado cuando pase D días a partir de hoy, si el número de contagiados actuales es C.

#Función para calcular la cantidad de contagiados
def contagiados(dias:int, actuales:int)->int:
    totalcontagiados=(2**dias)*actuales
    return totalcontagiados

if __name__=="__main__":
    #Declarando e inicializando variables
    dias:int
    dias=int(input("Ingrese la cantidad de días que han pasado a partir de hoy: "))
    actuales:int
    actuales=int(input("Ingrese la cantidad de contagiados actuales: "))
    
    personasContagiadas=contagiados(dias,actuales)
    print("Si el número de contagiados actuales es "+str(actuales)+ " cuando pasen " +str(dias)+ " días a partir de hoy, el número total de personas contagiadas será " +str(personasContagiadas))
