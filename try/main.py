def division(a, b):
    try:
        resultado = a / b
        if resultado < 0:
            raise ValueError('Ha ocurrido un error, validos solo numero positivos')
    except ZeroDivisionError:
        print("El divisor no puede ser cero") 
    except TypeError:
        print('Solo ingresar caracteres numericos')
    else:
        print('El resultado es:',resultado) 
    finally:
        print('Fin del programa')
division(10, 5)