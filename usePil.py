import cv2
import numpy as np
from PIL import Image
from pytesseract import pytesseract


def get_the_dark_pixels_value(gray_image):
    gray_image_array = np.array(gray_image)

    # Find the darkest point value
    darkest_point_value = gray_image_array.min()

    # Print the darkest point value
    return (darkest_point_value)

def get_Image(filename, WINDOW_NORMAL=None):
    # Open the image file
    image = Image.open("./scriptsImages/2.jpeg")

    # Convert the image to grayscale
    gray_image = image.convert("L")

    # Show the grayscale image
    gray_image.show()

    darkest_point_value = get_the_dark_pixels_value(gray_image)
    print(f"the dark value: {darkest_point_value};")
    # Set the threshold value
    threshold = 100 - darkest_point_value

    # Create a new image with the threshold applied
    binary_image = gray_image.point(lambda x: 0 if x < threshold else 255, "1")

    # Save the new image
    binary_image.save("binary_image.jpg")
    # Show the new image
    #binary_image.show()

    img = cv2.imread("binary_image.jpg", 0)
    cv2.namedWindow("Image", cv2.WINDOW_NORMAL)
    cv2.imshow("Image", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # # Use morphological operations to remove noise and fill in gaps
    # kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
    # thresh = cv2.morphologyEx(np.asarray(binary_image, dtype=np.uint8), cv2.MORPH_CLOSE, kernel, iterations=2)    #thresh = cv2.morphologyEx(binary_image, cv2.MORPH_CLOSE, kernel, iterations=2)
    #
    # # Find connected components
    # num_cc, labels, stats, centroids = cv2.connectedComponentsWithStats(thresh)
    #
    # # Iterate through the connected components
    # for i in range(1, num_cc):
    #     x, y, w, h, area = stats[i]
    #     if area < 100:
    #         continue
    #     letter_image = thresh[y:y + h, x:x + w]
    #     cv2.imwrite(f"letter_{i}.jpg", letter_image)
    #
    #     # Use OCR to recognize the text from the letter image
    #     text = pytesseract.image_to_string(letter_image, lang='heb', config='--psm 11')
    #     print(f"Letter {i}: {text}")
