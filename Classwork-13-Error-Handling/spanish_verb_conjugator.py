# Definimos excepciones de reglas de negocio
class MayusculasError(Exception): pass
class EspaciosError(Exception): pass

pronouns = ["Yo", "Tú", "Él", "Nosotros", "Vosotros", "Ellos"]
endings = {
    "ar": ["o", "as", "a", "amos", "ais", "an"],
    "er": ["o", "es", "e", "emos", "eis", "en"],
    "ir": ["o", "es", "e", "imos", "is", "en"],
}

try:
    verb = input("Write a spanish verb (ar/er/ir): ")

    # Regla de negocio: rechazar mayúsculas
    if verb != verb.lower():
        raise MayusculasError("El verbo debe escribirse en minúsculas")
        
    # Regla de negocio: rechazar espacios
    if verb != verb.strip() or " " in verb:
        raise EspaciosError("El verbo no debe tener espacios extra")

    # Si es muy corto (ej: "a") o no está (ej: "control"), la extracción 
    # de [-2:] dará algo que NO está en el diccionario y Python lanzará KeyError
    stem = verb[:-2]
    ending = verb[-2:]
    
    conjugations = endings[ending]

except MayusculasError as e:
    print(e)
except EspaciosError as e:
    print(e)
except KeyError:
    # Atrapamos errores para "control", un número "123", o inputs vacíos
    print("El verbo debe terminar en ar, er o ir")

# ELSE (Happy Path): Accedemos al diccionario e imprimimos
else:
    for index, pronoun in enumerate(pronouns):
        termination = conjugations[index]
        print(f"{pronoun} {stem}{termination}")