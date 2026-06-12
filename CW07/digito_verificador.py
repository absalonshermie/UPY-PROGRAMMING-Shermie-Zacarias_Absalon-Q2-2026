#INPUT
def calcular_digito_verificador(rol):
    rol_invertido = str(rol)[::-1]
    secuencia = [2, 3, 4, 5, 6, 7]
    suma = 0
#PROCESS  
    for i, digito in enumerate(rol_invertido):
        multiplicador = secuencia[i % len(secuencia)]
        suma += int(digito) * multiplicador  
    modulo = suma % 11
    resultado = 11 - modulo
    if resultado == 11:
        digito_v = '0'
    elif resultado == 10:
        digito_v = 'K'
    else:
        digito_v = str(resultado)
        
    return digito_v
rol_input = input("Ingresa el rol sin guión ni dígito verificador: ")
dv = calcular_digito_verificador(rol_input)

#OUTPUT
print(f"El dígito verificador calculado es: {dv}")
print(f"Rol completo: {rol_input}-{dv}")
