import numpy
from PIL import Image


def getimage(image_path):
   
    image = Image.open(image_path, "r")
    width, height = image.size
    pixel_values = list(image.getdata())
    if image.mode == "RGB":
        channels = 3
    elif image.mode == "L":
        channels = 1
    else:
             return None
    pixel_values = numpy.array(pixel_values).reshape((width, height, channels))
    return pixel_values


def getimage1(image1_path):
   
    image1 = Image1.open(image1_path, "r")
    width, height = image1.size
    pixel_values = list(image1.getdata())
    if image1.mode == "RGB":
        channels = 3
    elif image1.mode == "L":
        channels = 1
    else:
       
        return None
    pixel_values = numpy.array(pixel_values).reshape((width, height, channels))
    return pixel_values

def getimage2(image2_path):
   
    image2 = Image2.open(image2_path, "r")
    width, height = image1.size
    pixel_values = list(image2.getdata())
    if image2.mode == "RGB":
        channels = 3
    elif image2.mode == "L":
        channels = 1
    else:
       
        return None
    pixel_values = numpy.array(pixel_values).reshape((width, height, channels))
    return pixel_values

def getimage3(image3_path):
   
    image3 = Image3.open(image_path, "r")
    width, height = image3.size
    pixel_values = list(image3.getdata())
    if image3.mode == "RGB":
        channels = 3
    elif image3.mode == "L":
        channels = 1
    else:
       
        return None
    pixel_values = numpy.array(pixel_values).reshape((width, height, channels))
    return pixel_values

def getimage4(image4_path):
   
    image4 = Image4.open(image4_path, "r")
    width, height = image4.size
    pixel_values = list(image4.getdata())
    if image4.mode == "RGB":
        channels = 3
    elif image4.mode == "L":
        channels = 1
    else:
       
        return None
    pixel_values = numpy.array(pixel_values).reshape((width, height, channels))
    return pixel_values

def getimage5(image5_path):
   
    image5 = Image5.open(image5_path, "r")
    width, height = image5.size
    pixel_values = list(image5.getdata())
    if image5.mode == "RGB":
        channels = 3
    elif image5.mode == "L":
        channels = 1
    else:
       
        return None
    pixel_values = numpy.array(pixel_values).reshape((width, height, channels))
    return pixel_values


image = getimage("cycle.jpg")
image1 = getimage("lion.jpg")
image2 = getimage("dog.jpg")
image3 = getimage("car.jpg")
image4 = getimage("bird.jpg")
image5 = getimage("cow.jpg")

A="bike.jpg"
B= ["lion.jpg","car.jpg","bird.jpg","cow.jpg","bike.jpg"]
for x in B:
  if x == A:
   print("yes")
  else:
    print('no')
