import math

# Definimos nuestras excepciones personalizadas para reglas de negocio
class LimiteInferiorError(Exception): pass
class LimiteSuperiorError(Exception): pass
class IntervaloInvertidoError(Exception): pass
class MetodoInvalidoError(Exception): pass

# TRY principal para validar inputs del usuario
try:
    a_raw = input("Write the left endpoint of the interval: ")
    try:
        if "pi" in a_raw:
            a = eval(a_raw.replace("pi", str(math.pi)))
        else:
            a = float(a_raw)
    except (ValueError, NameError):
        # Python lo detecta, pero nosotros lanzamos nuestro error con el mensaje exacto
        raise LimiteInferiorError("El límite inferior debe ser numérico")

    b_raw = input("Write the right endpoint of the interval: ")
    try:
        if "pi" in b_raw:
            b = eval(b_raw.replace("pi", str(math.pi)))
        else:
            b = float(b_raw)
    except (ValueError, NameError):
        raise LimiteSuperiorError("El límite superior debe ser numérico")
        
    # Regla de negocio
    if a >= b:
        raise IntervaloInvertidoError("El límite inferior debe ser menor que el límite superior")

    f_x = input("Write the function to integrate: ")
    method = input("Select integration method (LRM/RRM/MPM/TM): ")
    
    # Regla de negocio
    if method not in ["LRM", "RRM", "MPM", "TM"]:
        raise MetodoInvalidoError("El método de integración no es válido. Usa LRM, RRM, MPM o TM")

except LimiteInferiorError as e:
    print(e)
except LimiteSuperiorError as e:
    print(e)
except IntervaloInvertidoError as e:
    print(e)
except MetodoInvalidoError as e:
    print(e)

# ELSE (Happy Path): Aquí va lo que procesamos sin errores iniciales
else:
    area = 0.0
    n = 1000
    h = (b - a) / n
    shift = 0
    constant = 0

    if method == "RRM":
        shift = 1
    if method == "MPM":
        constant = h/2
    if method == "TM":
        shift = 1

    # Segundo TRY para evaluar matemáticamente la función sin que el programa colapse
    try:
        for i in range(0 + shift, n + shift):
            xi = a + i * h + constant
            x = xi
            
            height = eval(f_x)
            if method == "TM":
                area += 2 * height * h
            else:
                area += height * h
                
        if method == "TM":
            x = a
            fa = eval(f_x)
            x = b
            fb = eval(f_x)
            area = (area + (fa * h) + (fb * h)) / 2
            
        print(f"The integration of {f_x} is {area:.3f}")
        
    except ZeroDivisionError:
        print("La función no está definida en algún punto del intervalo")
    except NameError:
        print("La función debe estar escrita en términos de x")
    except (SyntaxError, TypeError):
        print("La función ingresada no es válida")