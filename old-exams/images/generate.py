import random
from PIL import Image

NIMAGES = 100

rnd = random.Random(79021)


for i in range(1, NIMAGES + 1):
    width = rnd.randint(10, 100)
    height = rnd.randint(10, 100)
    r = rnd.randint(0, 255)
    g = rnd.randint(0, 255)
    b = rnd.randint(0, 255)
    extension = rnd.choice(['GIF', 'TIFF', 'JPEG', 'BMP', 'PNG'])
    img = Image.new('RGB', (width, height), color=(r, g, b))
    img.save(f'{i}.unknown', format=extension)
