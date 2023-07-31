import pytesseract
from pytesseract import Output
from PIL import Image
from matplotlib import pyplot as plt
import cv2
import numpy as np
from Utils import display, noise_removal, thin_font, save_image



myConfig = r'--psm 3 --oem 3'
# מחלץ באופן פשוט את הטקסט מהתמונה
image_file = "./scriptsImages/1.jpeg"
# /*************************קריאת התמונה*************************/
# # # מציאת הזוויות של כל אות שנמצאה בתמונה
image = cv2.imread("./scriptsImages/1.jpeg")
display("./scriptsImages/1.jpeg")

# מקטין את הגודל של התצוגה
image = cv2.resize(image, None, fx=0.5, fy=0.5)
# יוצר תמונה אפורה כדי לקרוא את הטקסט
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

adaptive_thresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 85, 11)

save_image(adaptive_thresh, "adaptive_thresh")

text = pytesseract.image_to_string(adaptive_thresh, lang='heb', config=myConfig)
#create a new text file

with open('scriptResoult/text/new.txt', 'w', encoding='utf-8') as f:
    print("file created")
    f.write(text)
    print(f"text written to file{f.name}")


#
# cv2.imshow("gray", gray)
# cv2.imshow("adaptive_thresh", adaptive_thresh)
# cv2.imshow("image", image)

cv2.waitKey(0)


# /*************************עוד דרך לקריאת התמונה*************************/
height, width, channels = image.shape
boxes = pytesseract.image_to_boxes(image, lang='heb', config=myConfig)
# הצג את הנקודות של הזוויות
# with open('scriptResoult/text/new.txt', 'w') as f:
#     f.write(boxes)
#     print(f"boxes written to file{f.name}")
# מצייר מלבנים סביב האותיות
for box in boxes.splitlines():
    box = box.split(' ')
    img = cv2.rectangle(image, (int(box[1]), height - int(box[2])), (int(box[3]), height - int(box[4])), (0, 0, 255), 2)
    x, y, w, h = int(box[1]), int(box[2]), int(box[3]), int(box[4])
    cv2.rectangle(image, (x, height - y), (w, height - h), (0, 0, 255), 1)
    cv2.putText(image, box[0], (x, height - y + 25), cv2.FONT_HERSHEY_COMPLEX, 1, (50, 50, 255), 2)

save_image(image, "squers_image")
# cv2.imshow("Image", image)
cv2.waitKey(0)

# כל מיני פעולות על התמונה על ידי שימוש בדאטה
# data = pytesseract.image_to_data(image, lang='heb', config=myConfig, output_type=Output.DICT)
# amount_of_boxes = len(data['text'])
# for i in range(amount_of_boxes):
#     if float(data['conf'][i]) > 30:
#         (x, y, width, height) = (data['left'][i], data['top'][i], data['width'][i], data['height'][i])
#         image = cv2.rectangle(image, (x, y), (x + width, y + height), (0, 255, 0), 2)
#         image = cv2.putText(image, data['text'][i], (x, y + height + 20), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2,
#                             cv2.LINE_AA)
#
# print(data['text'])
# cv2.imshow("Image", image)
# cv2.waitKey(0)

# /*************************דרך שונה שנלמדה בקורס הארוך ביוטיוב קריאת התמונה*************************/

# #capture 5
# no_noise = cv2.imread('./scriptsImages/no_noise.jpg')
# print("1nnnn")
# print("2nnnn")
# ocr_result = pytesseract.image_to_string(no_noise, lang='heb', config=myConfig)
# print(ocr_result)
# #capture 6




