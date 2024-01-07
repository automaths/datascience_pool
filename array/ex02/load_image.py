from PIL import Image
from numpy import asarray

def ft_load(filename: str) -> list:
    """
    Load an image and display its shape and content in RGB
    """
    image = Image.open("landscape.jpg")
    test = (image.size[0], image.size[1], asarray(image.getdata()).shape[1])
    print("The shape of image is:", (image.size[0], image.size[1], asarray(image.getdata()).shape[1]))
    return asarray(list(image.getdata()))
