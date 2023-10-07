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