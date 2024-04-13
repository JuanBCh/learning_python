import os
from PIL import Image

def abrir_imagen(ruta_img):
    imagen = Image.open(ruta_img)
    imagen.show()

ruta_relativa = 'sandia.jpeg'
ruta_absoluta = os.path.join(os.getcwd(), ruta_relativa)

abrir_imagen(ruta_absoluta)