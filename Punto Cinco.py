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
