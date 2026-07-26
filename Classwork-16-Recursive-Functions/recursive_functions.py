

def recursiva(n):
    #CASO BASE
    if n == 0:
        return "Done"
    else:
        print(n-1)
        return recursiva (n-1)

def fibonnaci (n):
    if (n==0) or (n==1):
        print (n)
        return n
    else:
        print((n-1, n-2))
        return fibonnaci (n-1) + fibonnaci (n-2)
    
def factorial (n):
    if (n==0) or (n==1):
        return 1
    else:
        return factorial (n-1)*n

def multiplicacion_recursiva (n,m):
    total = 0
    if m==0:
        return 0
    else:
        total += n
        return multiplicacion_recursiva (n,m-1) + n

def division_entera_recursiva (dividendo, divisor):
    if dividendo - divisor < 0:
        return 0
    else:
        return division_entera_recursiva (dividendo - divisor, divisor) + 1

def potencia_recursiva (base, exponente):
    if exponente ==0:
        return 1
    else:
        return potencia_recursiva(base, exponente -1)* base

def serie_collatz(n):
    if n == 1:
        #print("END")
        return 0
    else:
        if n % 2 ==0:
            #print(n // 2)
            return serie_collatz(n//2)
        else:
            #print(3*n + 1)
            return serie_collatz(3*n + 1)
import json

def aplanar_json(diccionario, clave_padre = '', separador = '.'):
    if isinstance(diccionario, list):
        diccionario = dict(enumerate(diccionario))
        
    elementos = []
    for key, value in diccionario.items():
        nueva_llave = f"{clave_padre}{separador}{key}" if clave_padre else str(key)
        
        if isinstance(value, (dict, list)):
            elementos.extend(aplanar_json(value, nueva_llave, separador).items())
        else:
            elementos.append((nueva_llave, value))
            
    return dict(elementos)

with open('json_prueba.json', 'r', encoding='utf-8') as archivo:
    json_crudo = json.load(archivo)

print(aplanar_json(json_crudo))






























