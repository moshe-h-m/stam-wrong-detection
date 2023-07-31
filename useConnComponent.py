import cv2
import pytesseract
import requests
import cv2 as cv
from PIL import Image
import PIL.Image

import getImage

def convertPathImageToGray(path):
    # getImage.show_Image(getImage.get_Image(path))

    image = cv2.imread(path)

    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    #print the gray
    cv2.namedWindow("gray", cv2.WINDOW_NORMAL)
    cv2.imshow("gray", gray)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    # Apply thresholding to create a binary image
    #guess the thresh
    blur1 = cv2.GaussianBlur(gray, (1, 1), 0 )
    ret3, thresh = cv2.threshold(blur1, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    cv2.namedWindow("image", cv2.WINDOW_NORMAL)

    cv2.imshow("image", thresh)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    #drew rectangle around the text

    # Use morphological operations to remove noise and fill in gaps
    # kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
    # thresh = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel, iterations=2)

    # Find connected components
    num_cc, labels, stats, centroids = cv2.connectedComponentsWithStats(thresh)

    # Iterate through the connected components
    for i in range(1, num_cc):
        x, y, w, h, area = stats[i]
        if area < 100:
            continue
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Show the original image with bounding boxes
    cv2.namedWindow("image with bounding boxes", cv2.WINDOW_NORMAL)

    cv2.imshow("image with bounding boxes", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # # Use morphological operations to remove noise and fill in gaps
    # kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
    # thresh = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel, iterations=2)
    #
    # # Find connected components
    #
    # num_cc, labels, stats, centroids = cv2.connectedComponentsWithStats(thresh)
    #
    # # Iterate through the connected components
    # for i in range(1, num_cc):
    #     x, y, w, h, area = stats[i]
    #     if area < 100:
    #         continue
    #     letter_image = thresh[y:y + h, x:x + w]
    #     cv2.imwrite(f"letter_{i}.jpg", letter_image)
    #     leim = cv2.imread(f"letter_{i}.jpg")
    #
    #     # #show the letter image
    #     cv2.namedWindow("letter_im", cv2.WINDOW_NORMAL)
    #     cv2.imshow("letter_im", leim)
    #     cv2.waitKey(0)
    #     cv2.destroyAllWindows()
    #
    #     # Use OCR to recognize the Hebrew text from the letter image
    #
    #
    #
    #     #text = pytesseract.image_to_string(letter_image, lang='heb', config='--psm 11')
    #     #print(f"Letter {i}: {text}")

    # image.show()
    return gray



def show_Image(img):

    # Load the image
    image = cv2.imread(img)


    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply thresholding to create a binary image
    thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

    # Use morphological operations to remove noise and fill in gaps
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
    thresh = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel, iterations=2)

    # Find connected components
    num_cc, labels, stats, centroids = cv2.connectedComponentsWithStats(thresh)

    # Iterate through the connected components
    for i in range(1, num_cc):
        x, y, w, h, area = stats[i]
        if area < 100:
            continue
        letter_image = thresh[y:y + h, x:x + w]
        cv2.imwrite(f"letter_{i}.jpg", letter_image)

        # Use OCR to recognize the text from the letter image
        text = pytesseract.image_to_string(letter_image, lang='heb', config='--psm 11')
        print(f"Letter {i}: {text}")

    image.show()

#a function to perform a RREF ( guos gorden matrix )


# using kraken
def useKrakenToRecognizeHebrewText(img):
    # Load the image
    image = cv2.imread(img)


    # Set Kraken API endpoint and authentication credentials
    url = "https://api.kraken.io/v1/ocr"
    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "Authorization": "API_KEY"
    }

    # Define image file and language
    data = {
        "data": open(img, "rb"),
        "language": "heb"
    }

    # Send image to Kraken API
    response = requests.post(url, headers=headers, data=data)

    # Get recognized text from response
    text = response.json()["data"]["text"]

    # Print recognized text
    print(text)
