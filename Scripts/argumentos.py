# image_rotator.py

from PIL import Image
import argparse # importa el módulo argparse

# inicializa el analizador sintáctico
parser = argparse.ArgumentParser()

# agrega argumentos con sus nombres correspondientes
parser.add_argument('input_file')
parser.add_argument('output_file')
parser.add_argument('angle', type=int)

# analiza los argumentos
args = parser.parse_args()

# carga una imagen del argumento input_file
im = Image.open(args.input_file)

# muestra el tamaño de la imagen
print(im.size)

# gira la imagen en un ángulo proporcionado como argumento
rotated = im.rotate(args.angle)

# guarda la imagen girada usando la ruta de salida de un argumento output_file
rotated.save(args.output_file)

#linea de codigo argumentos.py es mi archivo y rotated.png es mi archivo que tomaremos
# python argumentos.py rotated.png output.png 180