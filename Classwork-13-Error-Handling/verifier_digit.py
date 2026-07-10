class RolInvalidoError(Exception):
    pass

# INPUT
rol = input("Escribe el rol: ")

# PROCESS
try:
    rol_sin_digito, digito = rol.split('-')
except ValueError:
    print("Rol inválido, no tiene el formato XXXXXXXXX-X")
else:
    try:
        digito = int(digito)
    except ValueError:
        print("El digito verificador debe ser numerico")
    else:
        try:
            rol_invertido = [int(i) for i in rol_sin_digito]
        except ValueError:
            print("Los digitos del rol deben ser numericos")
        else:
            rol_invertido.reverse()
            
            secuencia = [2, 3, 4, 5, 6, 7]
            
            suma = 0
            
            for index in range(len(rol_invertido)):
                suma += rol_invertido[index] * secuencia[index % 6]
                
            resultado = suma % 11
            
            verificador = 11 - resultado
            
            try:
                if (verificador != digito):
                    raise RolInvalidoError(f"El dígito verificador no conicide, se esperaba {verificador}")
            except RolInvalidoError as e:
                print(f"Error: {e}")
            else:
                # OUTPUT
                print(f"Rol verificado, {rol_sin_digito}-{verificador}")