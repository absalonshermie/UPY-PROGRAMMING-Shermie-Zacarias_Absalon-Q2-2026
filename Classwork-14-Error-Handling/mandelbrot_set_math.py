config = {}

try:
    with open("config.txt", "r") as file:
        for line in file:
            line = line.strip()
            if not line:
                continue
            # Separamos parámetros. Si falta el "=", Python lanza ValueError
            parameter, value = line.split("=")
            parameter = parameter.strip()
            value = value.strip()
            config[parameter] = float(value) if "." in value else int(value)
            
    # Forzamos KeyError si falta algún parámetro obligatorio
    required_keys = ["ancho", "alto", "max_iter", "real_min", "real_max", "imag_min", "imag_max"]
    for key in required_keys:
        if key not in config:
            raise KeyError(key)

    width = config["ancho"]
    height = config["alto"]
    max_iter = config["max_iter"]
    
    # La validación de TypeError si "ancho" o "alto" tienen decimales y se leyeron como float
    if not isinstance(width, int) or not isinstance(height, int):
        raise TypeError("El ancho y alto deben ser números enteros")

    with open("mandelbrot.csv", "w") as output:
        output.write("row,column,iterations\n")
        
        # Si todo está correcto, procesa el CSV
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

except FileNotFoundError:
    print("No se encontró el archivo config.txt")
except ValueError:
    print("El archivo de configuración está mal formado.")
except KeyError as e:
    print(f"Falta el parámetro {e} en config.txt.")
except TypeError:
    print("Los parámetros 'ancho' y 'alto' deben ser números enteros.")