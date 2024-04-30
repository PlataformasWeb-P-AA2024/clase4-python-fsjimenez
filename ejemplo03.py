nombre = input("Ingrese nombre de la persona: ")

edad = int(input("Ingrese la edad de la persona: "))

suledo = float(input("Ingrese el sueldo de la persona: "))

mensajeFinal = "Nombre: %s\nEdad; %d\nSueldo; %2.f\n" % (nombre, edad, suledo)

print(mensajeFinal)