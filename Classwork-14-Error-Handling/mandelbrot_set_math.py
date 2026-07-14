class InvalidConfigError(Exception):
    pass

config = {}
file = None

try:
    file = open("config.txt", "r")
    
    for line_num, line in enumerate(file, start=1):
        line = line.strip()
        if not line: 
            continue
            
        try:
            parameter, value = line.split("=")
            config[parameter.strip()] = float(value) if "." in value else int(value)
        except ValueError:
            print(f"Error de formato en línea {line_num}: '{line}'. Ignorando parámetro.")

    required_keys = ["ancho", "alto", "max_iter", "real_min", "real_max", "imag_min", "imag_max"]
    for key in required_keys:
        if key not in config:
            raise KeyError(key)

    width = config["ancho"]
    height = config["alto"]
    max_iter = config["max_iter"]
    
    if width <= 0 or height <= 0:
        raise InvalidConfigError("El 'ancho' y 'alto' deben ser mayores a cero.")

except FileNotFoundError:
    print("Error: El archivo 'config.txt' no se encontró en la carpeta.")
except KeyError as e:
    print(f"Error: Falta el parámetro obligatorio {e} en config.txt.")
except InvalidConfigError as e:
    print(f"Error de configuración: {e}")

finally:
    if file:
        file.close()

else:
    output = None
    try:
        output = open("mandelbrot.csv", "w")
        output.write("row,column,iterations\n")

        for row in range(height):
            for column in range(width):
                real = config["real_min"] + (column / width) * (config["real_max"] - config["real_min"])
                imag = config["imag_min"] + (row / height) * (config["imag_max"] - config["imag_min"])
                c = complex(real, imag)
                
                z = 0 + 0j
                iterations = 0
                
                while (abs(z) <= 2) and (iterations < max_iter):
                    z = z * z + c
                    iterations += 1
                
                output.write(f"{row},{column},{iterations}\n")
                
        print("Fractal de Mandelbrot calculado y guardado exitosamente.")
        
    except Exception as e:
        print(f"Ocurrió un error inesperado al guardar el archivo CSV: {e}")
        
    finally:
        if output:
            output.close()