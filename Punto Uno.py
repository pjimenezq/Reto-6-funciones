#1. Crear una función matemática para calcular el volumen y el área superficial de la figura (esfera unida a un cono)

#La fórmula para hallar el volumen de una esfera es V=4/3*π*r1^3
#La fórmula para hallar el volumen de un cono es V=1/3*π*h*r2^2
#Por lo tanto, la función matemática para calcular el volumen de la figura es v=1/3*π*(4*r1^3+h*r2*2)
#La fórmula para hallar el área superficial de la esfera es As=4*π*r1^2
#La fórmula para hallar el área superficial del cono es As=π*r2*(r2+(h^2+r2^2)^1/2)
#Por lo tanto, la función matemática para calcular el área superficial de la figura es As=π*(4*r1^2+r2*(r2+(h^2+r2^2)^1/2))

#2. Crear dos funciones en python para calcular los valores antes establecidos, al ingresar por teclado r1, r2 y h.

import math #importando math para utilizar el valor de pi
pi:float
PI=math.pi #Declarando el valor de pi como una constante

#Función para calcular el volumen de la figura
def volumenFigura (radioUno:float, radioDos:float, altura:float)->float:
    volumen=(1/3)*PI*(4*radioUno**3+radioDos**2*altura)#Utilizando la función matemática para calcular el volumen que se halló en la primera parte
    return volumen

#Función para calcular el área superficial de la figura
def areaSuperficialFigura (radioUno:float, radioDos:float, altura:float)->float:
    areaSuperficial=PI*(4*radioUno**2+radioDos*((radioDos**2+altura**2)**(1/2)+radioDos)) #Utilizando la función matemática para calcular el área superficial que se halló en la primera parte
    return areaSuperficial

if __name__=="__main__":
    #Declaración de variables (nombrándolas con Camelcase y especificando que son de tipo float)
    radioUno:float
    radioDos:float
    radioTres:float

    #Inicializando variables con la función input()
    radioUno=float(input("Ingrese el valor correspondiente a r1: "))
    radioDos=float(input("Ingrese el valor correspondiente a r2: "))
    altura=float(input("Ingrese el valor correspondiente a h: "))

    volumenTotal=volumenFigura(radioUno,radioDos,altura)
    print("Cuando r1 mide "+str(radioUno)+ ", r2 mide "+str(radioDos)+ " y h mide "+str(altura)+ ", el volumen total de la figura es: "+ str(volumenTotal))

    areaSuperficialTotal=areaSuperficialFigura(radioUno,radioDos,altura)
    print("Cuando r1 mide "+str(radioUno)+ ", r2 mide "+str(radioDos)+ " y h mide "+str(altura)+ ", el área superficial total de la figura es: "+ str(areaSuperficialTotal))