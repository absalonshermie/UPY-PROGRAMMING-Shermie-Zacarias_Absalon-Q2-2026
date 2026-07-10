class DigitoApocrifoError(Exception):
    pass
check = True

while check:
    try:
        rol = input("Escribe el rol: ")
        rol_sin_digito, digito = rol.split("-")
        check = False
    
    except ValueError:
        print("Rol no valido, debe de tener 10 digitos y el ultimo debde de estar separado por -")
    
inverso = rol_sin_digito[::-1]

secuencia = [2,3,4,5,6,7]
suma = 0

for index in range(len(inverso)):
    numero = int(inverso[index: index + 1])
    suma += numero * secuencia[index % 6]
    
resultado = suma % 11
verification = 11 - resultado

try:
    if verification != int(digito):
        raise DigitoApocrifoError
except DigitoApocrifoError as e:
    print("Digito verificador apocrifo")

print(f"{rol_sin_digito}-{verification}") 