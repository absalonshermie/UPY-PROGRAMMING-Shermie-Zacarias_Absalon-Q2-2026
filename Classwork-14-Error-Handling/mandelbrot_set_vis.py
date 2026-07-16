from PIL import Image

config = {}

try:
    # 1. Leer Configuración
    with open("config.txt", "r") as file:
        lines = file.readlines()
        for line in lines:
            line = line.strip()
            if not line:
                continue
            parameter, value = line.split("=")
            config[parameter.strip()] = float(value) if "." in value else int(value)

    max_iter = config["max_iter"]
    ancho = int(config["ancho"])
    alto = int(config["alto"])

    # 2. Configurar la imagen en escala de grises ("L")
    img = Image.new("L", (ancho, alto))

    # 3. Leer CSV y procesar pixeles
    with open("mandelbrot.csv", "r") as archivo:
        lineas = archivo.readlines()
        
    lineas.pop(0) # Quitar encabezados

    for linea in lineas:
        linea = linea.strip()
        if not linea:
            continue
            
        # Si hay datos de más ("extra"), el split(",") lanzará ValueError
        row, column, iterations = linea.split(",")
        iterations = int(iterations)
        row = int(row)
        column = int(column)
        
        # Mapeo de color corregido según los casos de prueba
        if iterations == max_iter:
            brillo = 0
        else:
            brillo = int((iterations / max_iter) * 255)
            
        # Si la columna o fila sobrepasan (ancho, alto), putpixel lanzará IndexError
        img.putpixel((column, row), brillo)
        
    img.save("mandelbrot.png")

except FileNotFoundError as e:
    if "config.txt" in str(e):
        print("No se encontró el archivo config.txt")
    else:
        print("No se encontró el archivo mandelbrot.csv")
except ValueError:
    print("El archivo mandelbrot.csv está mal formado.")
except IndexError:
    print("El archivo mandelbrot.csv no es consistente con el ancho y alto del config.txt.")