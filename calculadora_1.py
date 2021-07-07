def calcular():
    print("Que desea hacer?")
    print("1 = Usar la calculadora; 2 = Nada")
    pregunta_hacer = int(input())
    if pregunta_hacer == 1:        
        num_1 = (float(input("Introduzca el primer numero: ")))
        print("Desea sumar(1), restar(2), multiplicar(3) o dividir(4)?")
        operacion = int(input())
        num_2 = (float(input("Introduzca el segundo numero: ")))
        if operacion == 1:
            resultado = num_1 + num_2
            print("El resultado es: ", float(resultado))
        elif operacion == 2:
            resultado = num_1 - num_2
            print("El resultado es: ", float(resultado))
        elif operacion == 3:
            resultado = num_1 * num_2
            print("El resultado es: ", float(resultado))
        elif operacion == 4:
            resultado = num_1 / num_2
            print("El resultado es: ", float(resultado))
        else:
            print("Operacion invalida.")
            return
    else:
        print("Adios.")
        return


calcular()

