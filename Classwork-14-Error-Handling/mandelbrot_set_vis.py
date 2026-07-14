from PIL import Image

class DimensionesInvalidasError(Exception):
    pass

class CSVVacioError(Exception):
    pass

config = {}

try:
    with open("config.txt", "r") as file:
        for line_num, line in enumerate(file, start=1):
            line = line.strip()
            if not line:
                continue
            try:
                parameter, value = line.split("=")
                config[parameter.strip()] = float(value) if "." in value else int(value)
            except ValueError:
                print(f"Aviso: Formato incorrecto en config.txt (línea {line_num}).")
    
    max_iter = config["max_iter"]
    ancho = config["ancho"]
    alto = config["alto"]
    
    if ancho <= 0 or alto <= 0:
        raise DimensionesInvalidasError("El ancho y alto deben ser mayores a cero.")
        
    with open("mandelbrot.csv", "r") as archivo:
        lineas = archivo.readlines()
        
    if len(lineas) <= 1:
        raise CSVVacioError("El archivo mandelbrot.csv no tiene suficientes datos.")
        
    lineas.pop(0)

except FileNotFoundError as e:
    print(f"Error crítico: No se encontró un archivo necesario. {e}")
except KeyError as e:
    print(f"Error de configuración: Falta el parámetro obligatorio {e} en config.txt.")
except DimensionesInvalidasError as e:
    print(f"Error de dominio: {e}")
except CSVVacioError as e:
    print(f"Error de datos: {e}")

else:
    img = Image.new("HSV", (ancho, alto))
    
    for idx, linea in enumerate(lineas, start=2): 
        linea = linea.strip()
        if not linea:
            continue
            
        try:
            row, column, iterations = linea.split(",")
            iterations = int(iterations)
            row = int(row)
            column = int(column)
            
            if iterations == max_iter:
                brillo = 40
            else:
                brillo = int((iterations / max_iter) * 255)
                
            img.putpixel((column, row), (brillo, 255, 255))
            
        except ValueError:
            print(f"Aviso: Fila {idx} en el CSV corrupta. Saltando píxel.")
        except IndexError:
            print(f"Aviso: Coordenada ({column}, {row}) fuera del límite de la imagen. Saltando.")
            
    try:
        img_rgb = img.convert("RGB")
        img_rgb.save("mandelbrot.png")
        print("DONE: Imagen generada y guardada exitosamente.")
    except Exception as e:
        print(f"Error inesperado al guardar la imagen: {e}")