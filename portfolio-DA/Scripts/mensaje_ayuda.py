# image_rotator.py

from PIL import Image
import argparse

# inicializa el analizador sintáctico
parser = argparse.ArgumentParser()

# agrega argumentos con sus nombres correspondientes
# considera que ahora utilizamos el parámetro help
parser.add_argument('input_file', help='ruta del archivo de entrada')
parser.add_argument('output_file', help='ruta del archivo de salida')
parser.add_argument('--angle', '-a', type=int, default=90, help='rotación en sentido contrario a las agujas del reloj (grados)')
parser.add_argument('-i', '--info', action='store_true', help='muestra el tamaño de la imagen')

# analiza los argumentos
args = parser.parse_args()

# carga una imagen del argumento input_file
im = Image.open(args.input_file)

# muestra el tamaño de la imagen solo si el indicador info está establecido en True
if args.info:
    print('dimensiones de la imagen de entrada:', im.size)

# gira la imagen en un ángulo proporcionado como argumento
rotated = im.rotate(args.angle)

# guarda la imagen girada usando la ruta de salida de un argumento output_file
rotated.save(args.output_file)

#
# python mensaje_ayuda.py -h