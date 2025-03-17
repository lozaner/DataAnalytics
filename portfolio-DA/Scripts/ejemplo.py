from PIL import Image

print("¡Pillow está funcionando correctamente!")


try:
    image = Image.open("Image-14.png")
    image.show()  # Esto abrirá la imagen en el visor predeterminado de tu sistema
except FileNotFoundError:
    print("El archivo no se encuentra en la ruta especificada.")