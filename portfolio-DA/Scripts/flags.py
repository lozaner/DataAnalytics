# image_rotator.py

from PIL import Image
import argparse

# inicializa el analizador sintáctico
parser = argparse.ArgumentParser()

# agrega argumentos con sus nombres correspondientes
parser.add_argument('input_file')
parser.add_argument('output_file')
parser.add_argument('--angle', '-a', type=int, default=90)
# observa que a continuación agregamos el indicador --info (o simplemente -i)
parser.add_argument('-i', '--info', action='store_true')

# analiza los argumentos
args = parser.parse_args()

# carga una imagen del argumento input_file 
im = Image.open(args.input_file)

# muestra el tamaño de la imagen solo si el indicador --info está establecido en True
if args.info:
    print('dimensiones de la imagen de entrada:', im.size)

# gira la imagen en un ángulo proporcionado como argumento
rotated = im.rotate(args.angle)

# guarda la imagen girada usando la ruta de salida de un argumento output_file
rotated.save(args.output_file)


#se coloca el siguiente codigo 
# python flags.py Image-14.png --angle 180 output.png -i