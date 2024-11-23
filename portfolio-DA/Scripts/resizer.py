# resizer.py

from PIL import Image
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('input_file', help='ruta del archivo de entrada')
parser.add_argument('output_file', help='ruta del archivo de salida')
parser.add_argument('width', help='ancho deseado', type=int)
parser.add_argument('height', help='altura deseada', type=int)
args = parser.parse_args()

im = Image.open(args.input_file)
new_size = (args.width, args.height)
resized = im.resize(new_size)
resized.save(args.output_file)
im.close()

# python resizer.py input_image.png output_image.png 120 80