# This is a sample Python script.
import sys

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import cv2
import pytesseract
from PIL import Image
import getImage
import useConnComponent
import usePil




# Press the green button in the gutter to run the script.
if __name__ == '__main__':




    img = getImage.get_Image("./scriptsImages/1.jpeg")
    getImage.show_Image(img)
    #print me all images in the folder scriptsImages
    for image in getImage.get_all_images("./scriptsImages"):
        getImage.show_Image(image)

    useConnComponent.convertPathImageToGray("./scriptsImages/1.jpeg")

    usePil.get_Image("./scriptsImages/2.jpeg")
    print(cv2.imshow.__doc__)

    text = pytesseract.image_to_string("./scriptsImages/1.jpeg", lang='heb')

    # Write the text to a file
    with open("output.txt", "w", encoding="utf-8") as f:
        f.write(text)








