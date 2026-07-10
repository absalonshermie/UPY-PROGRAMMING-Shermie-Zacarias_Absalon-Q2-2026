
class InvalidVerbError(Exception):
    pass

pronouns = ["Yo", "Tú", "Él", "Nosotros", "Vosotros", "Ellos"]

endings = {
    "ar" : ["o", "as", "a", "amos", "ais", "an"],
    "er" : ["o", "es", "e", "emos", "eis", "en"],
    "ir" : ["o", "es", "e", "imos", "is", "en"],
}

check = True

while check:
    try:
        # INPUT
        verb = input("Write a spanish verb (ar/er/ir): ").strip().lower()
        
        if len(verb) < 2:
            raise ValueError("El verbo es demasiado corto.")
            
        stem = verb[:-2] 
        ending = verb[-2:] 
        
        if ending not in endings:
            raise InvalidVerbError(f"La terminación '{ending}' no es válida. El verbo debe terminar en ar, er o ir.")
            
        conjugations = endings[ending]
        
        check = False 
        
    except ValueError as e:
        print(f"Error: {e}\n")
    except InvalidVerbError as e:
        print(f"Error de dominio: {e}\n")
    except KeyError as e:
        print(f"Error: La llave {e} no existe en el diccionario de terminaciones.\n")

# PROCESS / OUTPUT
print(f"\n--- Conjugación de {verb} ---")
for index, pronoun in enumerate(pronouns):
    termination = conjugations[index]
    print(f"{pronoun} {stem}{termination}")