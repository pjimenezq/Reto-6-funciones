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
