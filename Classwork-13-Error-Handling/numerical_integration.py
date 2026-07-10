import math

class InvalidMethodError(Exception):
    pass

check = True

while check:
    try:
        a_input = input("Write the left endpoint of the interval: ")
        if "pi" in a_input:
            a = eval(a_input.replace("pi", str(math.pi)))
        else:
            a = float(a_input)

        b_input = input("Write the right endpoint of the interval: ")
        if "pi" in b_input:
            b = eval(b_input.replace("pi", str(math.pi)))
        else:
            b = float(b_input)
            
        method = input("Select integration method (LRM/RRM/MPM/TRP): ")
        
        if method not in ["LRM", "RRM", "MPM", "TRP"]:
            raise InvalidMethodError(f"Método '{method}' no reconocido. Usa LRM, RRM, MPM o TRP.")
            
        check = False 
        
    except ValueError:
        print("Error: Los extremos del intervalo deben ser números válidos o la constante 'pi'.\n")
    except InvalidMethodError as e:
        print(f"Error de dominio: {e}\n")
    except (NameError, SyntaxError):
        print("Error: Expresión inválida al escribir 'pi'.\n")

f_x = input("Write the function to integrate (e.g., x**2, math.sin(x)): ")

# PROCESS
area = 0.0
n = 1000
h = (b - a) / n
shift = 0
constant = 0

if method == "RRM":
    shift = 1
if method == "MPM":
    constant = h/2
if method == "TRP":
    shift = 1

try:
    for i in range(0 + shift, n + shift):
        xi = a + i * h + constant
        x = xi
        
        height = eval(f_x) 
        
        if method == "TRP":
            area += 2 * height * h
        else:
            area += height * h
            
    if method == "TRP":
        x = a
        fa = eval(f_x)
        x = b
        fb = eval(f_x)
        area = (area + (fa * h) + (fb * h)) / 2
        
    # OUTPUT 
    print(f"The integration of {f_x} is {area:.4f}")

except ZeroDivisionError:
    print("Error: ZeroDivisionError. Hubo una división entre cero al evaluar la función en este intervalo.")
except TypeError as e:
    print(f"Error de tipo al evaluar la función. Detalles: {e}")
except (NameError, SyntaxError) as e:
    print(f"Error de sintaxis en la función '{f_x}'. Asegúrate de escribirla correctamente (ej. usar 'math.sin(x)' o 'x**2'). Detalles: {e}")