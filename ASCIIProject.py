from PIL import Image
import math
import subprocess

brightnessMap = " `^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"
def createMatrix(im,mode):
    ascii_matrix = []
    for x in range(0,im.height):
        ascii_row = []
        for y in range(0,im.width):
            pix = im.getpixel((y,x))
            if(len(pix) < 3):
                avg = pix[0]
            else:
                avg = (pix[0]+pix[1]+pix[2])/3
            if mode == "d":
                num = math.ceil((avg/255)*65)
            else:
                num = 65-math.ceil((avg/255)*65)
            ascii_row.append(brightnessMap[num])
        ascii_matrix.append(ascii_row)
    return ascii_matrix

def printMatrix(ascii_matrix):
    strArt = ""
    for row in ascii_matrix:
        line = [p+p+p for p in row]
        strArt += "".join(line)+"\n"
        print("".join(line))

mode = "nan"
while mode != "d" and mode != "b":
    mode = input("Select mode dark/bright (d/b):")

while True:

    path = input("Enter file path of the image (enter q to quit program):")

    if path == "q":
        print("Quitting program...")
        break
    try:
        image = Image.open(path)
    except:
        print("Invalid file path!")
    else:
        type = image.format
        if(type != "PNG" and type != "JPEG"):
            print("this program only supports PNG and JPEG images!")
        else:
            if image.size > ((150,150)):
                im = image.resize((150,150))
                matrix = createMatrix(im,mode)
            else:
                matrix = createMatrix(image,mode)
            printMatrix(matrix)


