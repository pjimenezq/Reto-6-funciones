#1. Crear una función matemática para calcular el área y el perímetro de la figura (un réctangulo y dos círculos)

#La fórmula para hallar el área del rectángulo es A=b*a
#La fórmula para hallar el área de un círculo es A=π*r^2
#Por lo tanto, la función matemática para calcular el área de la figura es A=b*a+2πr^2
#La fórmula para hallar el perímetro del rectángulo es P=2(a+b)
#La fórmula para hallar el perímetro del círculo es P=2*π*r
#Por lo tanto, la función matemática para calcular el perímetro de la figura es P=2(a+b+2*π*r)

#2. Crear dos funciones en python para calcular los valores antes establecidos, al ingresar por teclado r, a y b.

import math #importando math para utilizar el valor de pi
pi:float
PI=math.pi #Declarando el valor de pi como una constante

#Función para calcular el área de la figura
def areaFigura(radio:float, altura:float, base:float)->float:
    area=altura*base+(2*PI*radio**2)#Utilizando la función matemática que se halló en la primera parte para calcular el área 
    return area

#Función para calcular el perímetro de la figura
def perimetroFigura(radio:float, altura:float, base:float)->float:
    perimetro=2*(altura+base+(2*PI*radio))#Utilizando la función matemática que se halló en la primera parte para calcular el perímetro 
    return perimetro

if __name__=="__main__":
    #Declarando las variables de tipo float
    radio:float
    altura:float
    base:float
    #Inicializando variables con la función input()
    radio=float(input("Ingrese el valor correspondiente a r: "))
    altura=float(input("Ingrese el valor correspondiente a a: "))
    base=float(input("Ingrese el valor correspondiente a b: "))
    
    areaTotal=areaFigura(radio,altura,base)
    print("Cuando r mide "+str(radio)+ ", a mide "+str(altura)+ " y b mide "+str(base)+ ", el área total de la figura es: "+ str(areaTotal))

    perimetroTotal=perimetroFigura(radio,altura,base)
    print("Cuando r mide "+str(radio)+ ", a mide "+str(altura)+ " y b mide "+str(base)+ ", el perímetro total de la figura es: "+ str(perimetroTotal))