# Reto 6
Para este reto, se hizo un programa individual para cada uno de los puntos.

## Primer punto

1. Dado la figura de la imagen, desarrolle:

![image](https://github.com/pjimenezq/Reto-6-funciones/assets/141860508/2919d6e2-8839-435b-9553-410359e772e7)

* Una función matemática para calcular el volumen y el área superficial.
* Cree dos funciones en python para calcular los valores antes establecidos, al ingresar por teclado r1, r2 y h.
* Revise como utilizar el valor de pi usando import math y math.pi

**Código**

```
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

```

## Segundo punto

2. Dado la figura de la imagen, desarrolle:

![image](https://github.com/pjimenezq/Reto-6-funciones/assets/141860508/6f32a23d-3854-4b45-9913-ad409b2daa0d)

* Una función matemática para calcular el área y el perimetro.
* Cree dos funciones en python para calcular los valores antes establecidos, al ingresar por teclado r, a y b.
* Revise como utilizar el valor de pi usando import math y math.pi

**Código**

```
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
```

## Tercer punto

3. Diseñe una función que calcule la cantidad de carne de aves en kilos si se tienen N gallinas, M gallos y K pollitos cada uno pesando 6 kilos, 7 kilos y 1 kilo respectivamente.

**Código**

```
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
```
## Cuarto punto

4. Mi mamá me manda a comprar P panes a 300 cada uno, M bolsas de leche a 3300 cada una y H huevos a 350 cada uno. Hacer un programa que me diga las vueltas (o lo que quedo debiendo) cuando me da un billete de B pesos.

**Código**

```
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
```
## Quinto punto

5. Haga un programa que utilice una función para calcular el valor de un préstamo C usando interés compuesto del i por n meses.

**Código**

```
#Hacer un programa que utilice una función para calcular el valor de un préstamo c usando interés compuesto del i por n meses.

#La fórmula del interés compuesto es CapitalFinal=CapitalInicial(1+(interés mensual/100))**tiempo(en meses)

#Función para calcular el Capital Final en una fórmula de interés compuesto
def valor(capitalInicial:float,interes:float,meses:int)->float:
    valorFinal=capitalInicial*(1+(interes/100))**(meses)
    return valorFinal

if __name__=="__main__":
    #Declarando e inicializando variables con la función input
    capitalInicial=float(input("Ingrese el valor del capital inicial: "))
    interes=float(input("Ingrese la tasa de interés mensual: "))
    meses=int(input("Ingrese la cantidad de meses del préstamo: "))
    
    total=valor(capitalInicial,interes,meses)
    print("El valor del préstamo cuando el capital inicial es " +str(capitalInicial)+ ", los intereses mensuales son de " +str(interes)+ " y los meses son "+str(meses)+ ", es de "+str(total))
```
## Sexto punto

6. El número de contagiados de Covid-19 en el país de NuncaLandia se duplica cada día. Hacer un programa que diga el número total de personas que se han contagiado cuando pasen D días a partir de hoy, si el número de contagiados actuales es C.
   
**Código**

```
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

```
## Séptimo punto

7. Escriba un programa que pida 5 números reales y calcule las siguientes operaciones usando una función para cada una:

* El promedio
* La mediana
* El promedio multiplicativo (multilplica todos y luego calcula la raíz de la cantidad de operandos)
* Ordenar los números de forma ascendente
* Ordenar los números de forma descendente
* La potencia del mayor número elevado al menor número
* La raíz cúbica del menor número

**Código**
```
# Problema planteado:Escribir un programa que pida 5 números reales y calcule el promedio, la mediana, el promedio multiplicativo, ordenar los números de forma ascendente, ordenar los números de forma descendente, la potencia del mayor número elevado al menor número, la raíz cúbica del menor número

def promedio(a:float, b:float, c:float, d:float, e:float)->float:
    elPromedio=(a+b+c+d+e)/5
    return elPromedio

def promedioMultiplicativo(a:float, b:float, c:float, d:float, e:float)->float:
    elPromedioMultiplicativo=(a*b*c*d*e)**(1/5)
    return elPromedioMultiplicativo

def ordenAscendente(a:float, b:float, c:float, d:float, e:float)->float:
    primero=a
    segundo=b
    tercero=c
    cuarto=d
    quinto=e

    if primero>segundo:
        segundo=primero
        primero=b

    if primero>tercero:
        tercero=primero
        primero=c

    if primero>cuarto:
        cuarto=primero
        primero=d

    if primero>quinto:
        quinto=primero
        primero=e
    
    if segundo>tercero:
        auxiliar=tercero
        tercero=segundo
        segundo=auxiliar
    
    if segundo>cuarto:
        auxiliar=cuarto
        cuarto=segundo
        segundo=auxiliar
    
    if segundo>quinto:
        auxiliar=quinto
        quinto=segundo
        segundo=auxiliar
    
    if tercero>cuarto:
        auxiliar=cuarto
        cuarto=tercero
        tercero=auxiliar
    
    if tercero>quinto:
        auxiliar=quinto
        quinto=tercero
        tercero=auxiliar

    if cuarto>quinto:
        auxiliar=quinto
        quinto=cuarto
        cuarto=auxiliar

    ascendente=primero, segundo, tercero, cuarto, quinto
    return ascendente

def ordenDescendente(a:float, b:float, c:float, d:float, e:float)->float:
    primero=a
    segundo=b
    tercero=c
    cuarto=d
    quinto=e

    if primero>segundo:
        segundo=primero
        primero=b

    if primero>tercero:
        tercero=primero
        primero=c

    if primero>cuarto:
        cuarto=primero
        primero=d

    if primero>quinto:
        quinto=primero
        primero=e
    
    if segundo>tercero:
        auxiliar=tercero
        tercero=segundo
        segundo=auxiliar
    
    if segundo>cuarto:
        auxiliar=cuarto
        cuarto=segundo
        segundo=auxiliar
    
    if segundo>quinto:
        auxiliar=quinto
        quinto=segundo
        segundo=auxiliar
    
    if tercero>cuarto:
        auxiliar=cuarto
        cuarto=tercero
        tercero=auxiliar
    
    if tercero>quinto:
        auxiliar=quinto
        quinto=tercero
        tercero=auxiliar

    if cuarto>quinto:
        auxiliar=quinto
        quinto=cuarto
        cuarto=auxiliar

    descendente=quinto, cuarto, tercero, segundo, primero
    return descendente

def mediana(a:float, b:float, c:float, d:float, e:float)->float:
    primero=a
    segundo=b
    tercero=c
    cuarto=d
    quinto=e

    if primero>segundo:
        segundo=primero
        primero=b

    if primero>tercero:
        tercero=primero
        primero=c

    if primero>cuarto:
        cuarto=primero
        primero=d

    if primero>quinto:
        quinto=primero
        primero=e
    
    if segundo>tercero:
        auxiliar=tercero
        tercero=segundo
        segundo=auxiliar
    
    if segundo>cuarto:
        auxiliar=cuarto
        cuarto=segundo
        segundo=auxiliar
    
    if segundo>quinto:
        auxiliar=quinto
        quinto=segundo
        segundo=auxiliar
    
    if tercero>cuarto:
        auxiliar=cuarto
        cuarto=tercero
        tercero=auxiliar
    
    if tercero>quinto:
        auxiliar=quinto
        quinto=tercero
        tercero=auxiliar

    if cuarto>quinto:
        auxiliar=quinto
        quinto=cuarto
        cuarto=auxiliar

    laMediana=tercero
    return laMediana

def raizCubicaMenorNumero(a:float, b:float, c:float, d:float, e:float)->float:
    primero=a
    segundo=b
    tercero=c
    cuarto=d
    quinto=e

    if primero>segundo:
        segundo=primero
        primero=b

    if primero>tercero:
        tercero=primero
        primero=c

    if primero>cuarto:
        cuarto=primero
        primero=d

    if primero>quinto:
        quinto=primero
        primero=e
   
    raizCubica=primero**(1/2)
    return raizCubica

def potenciaMayorElevadoMenor(a:float, b:float, c:float, d:float, e:float)->float:
    primero=a
    segundo=b
    tercero=c
    cuarto=d
    quinto=e

    if primero>segundo:
        segundo=primero
        primero=b

    if primero>tercero:
        tercero=primero
        primero=c

    if primero>cuarto:
        cuarto=primero
        primero=d

    if primero>quinto:
        quinto=primero
        primero=e
   
    if segundo>quinto:
        auxiliar=quinto
        quinto=segundo
        segundo=auxiliar
    
    if tercero>quinto:
        auxiliar=quinto
        quinto=tercero
        tercero=auxiliar

    if cuarto>quinto:
        auxiliar=quinto
        quinto=cuarto
        cuarto=auxiliar
    mayorElevadoMenor=quinto**primero
    return mayorElevadoMenor
```
## Octavo punto

8. Para el punto anterior incluir las funciones en un archivo independiente e importarlas para su uso.

**Código**

```
import PuntoSieteFunciones #Importando las funciones realizadas en el punto 7
if __name__=="__main__":
    #Declarando e inicializando las variables correspondientes a los 5 números reales del problema planteado
    a=float(input("Ingrese el primer número real "))
    b=float(input("Ingrese el segundo número real "))
    c=float(input("Ingrese el tercer número real "))
    d=float(input("Ingrese el cuarto número real "))
    e=float(input("Ingrese el quinto número real "))

    #Aplicando las funciones
    promedio=PuntoSieteFunciones.promedio(a,b,c,d,e)
    print("El promedio de los cinco números reales es "+str(promedio))

    mediana=PuntoSieteFunciones.mediana(a,b,c,d,e)
    print("La mediana es " +str(mediana))

    promedioMultiplicativo=PuntoSieteFunciones.promedioMultiplicativo(a,b,c,d,e)
    print("El promedio multiplicativo es "+ str(promedioMultiplicativo))

    ordenFormaAscendente=PuntoSieteFunciones.ordenAscendente(a,b,c,d,e)
    print("Los números ordenados de forma ascendente son "+ str(ordenFormaAscendente))

    ordenFormaDescendente=PuntoSieteFunciones.ordenDescendente(a,b,c,d,e)
    print("Los númros ordenados de forma descendente son: " + str(ordenFormaDescendente))

    potenciaMayorElevadoAlMenor=PuntoSieteFunciones.potenciaMayorElevadoMenor(a,b,c,d,e)
    print("La potencia del mayor número elevado al menor número es " + str(potenciaMayorElevadoAlMenor))

    raizCubicaMenor=PuntoSieteFunciones.raizCubicaMenorNumero(a,b,c,d,e)
    print("La raíz cúbica del menor número es " + str(raizCubicaMenor))

```
## Noveno punto
9. Consultar qué es y cómo funciona pip en python.

Pip es un gestor de paquetes para Python, es decir que este cumple con la función de instalar y administrar paquetes en Python de forma eficiente. 
Este regularmente se instala a la vez que uno instala Python. Pip facilita y hace eficaz el uso de librerías ya que hace que la persona que necesite utilizar la librería de un tercero no tenga que acceder directamente a la página del fabricante, descargar la librería, colocarla en el proyecto manualmente y volverla a descargar cada vez que tenga una nueva actualización.
Para instalar los paquetes, se ejecuta la consola de windows (win + r y luego se escribe cmd + enter) y allí se escribe “pip install” +”nombre del paquete”. Asimismo, para mostrar los paquetes instalados se escribe “pip list”.

## Décimo punto
10. Hacer un listado de módulos populares para python que se puedan instalar com pip y consultar cómo instalarlos.
Como se estableció anteriormente, para instalar los módulos se debe escribir en la consola de windows  _pip install nombre_. Donde _nombre_, es el nombre del paquete que se busca instalar. Por ejemplo: _pip install numpy_.
Las librerías más reconocidas son:
* Matplotlib: Genera una gran variedad de gráficos de calidad.
* TensorFlow: Fue desarrollada por Google y es utilizada para el cálculo numérico y en el Deep Learning.
* PyTorch: Desarrollado por Facebook y empleado en el cálculo numérico.
* Keras: Para el desarrollo de modelos de aprendizaje profundo.
* Scikit-learn: Para la construcción de modelos de aprendizaje automático o machine learning y para el análisis de datos.
* Pandas: Utilizada en Data Science, para el análisis y la manipulación de datos.
* Seaborn: Permite la visualización de datos estadísticos.
* NumPy: Especializada en cálculo numérico y análisis de datos.

## Referencias
https://www.programaenpython.com/avanzado/gestion-de-dependencias-en-python-con-pip/#Instalar_dependencias_con_pip
https://immune.institute/sin-categorizar/librerias-python-que-son/
