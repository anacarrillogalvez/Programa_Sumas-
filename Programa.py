n1 = input("¿Dime el primer número?")
n2 = input("¿Dime el segundo número?")

print (n1+n2)




while True:
    try:
        n1 = int(input("¿Dime el primer número?"))
        break
    except ValueError:
        print("El valor introducido no es un número. Intenta de nuevo")


suma = n1+n2

print ("La suma de los dos números es: " + str(n1+n2))


// Comentarios en el lenguaje de programacion 
// Pruebas 
