from PIL import Image
from io import BytesIO
import requests


def test():
    return 'hello world'


def max_colors(thumbnail_URL):
    response = requests.get(thumbnail_URL)
    img = Image.open(BytesIO(response.content))
    return img.getcolors()


print(max_colors('https://i.ytimg.com/vi/troEfX2xU7g/hq720.jpg?sqp=-oaymwEcCNAFEJQDSFXyq4qpAw4IARUAAIhCGAFwAcABBg==&rs=AOn4CLAriuyAF6KnU30xGkqYCCWybgAMzA'))
