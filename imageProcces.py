import cv2

import Utils
from Utils import display


myConfig = r'--psm 3 --oem 3'
# מחלץ באופן פשוט את הטקסט מהתמונה
image_file = "./scriptsImages/1.jpeg"
#display(image_file)
img_reder = cv2.imread(image_file)
#bitwise image
inverted_image = cv2.bitwise_not(img_reder)
cv2.imwrite('scriptsImages/inverted.jpg', inverted_image)
display('scriptsImages/inverted.jpg')

#binarization
def grayScale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imwrite('scriptsImages/gray1.jpg', grayScale(img_reder))
#display('scriptsImages/gray1.jpg')
thresh, binarized_image = cv2.threshold(grayScale(img_reder), 120, 230, cv2.THRESH_BINARY)
cv2.imwrite('scriptsImages/barbarized.jpg', binarized_image)
#options.display('scriptsImages/barbarized.jpg')

# /*********noise removel********************/

no_noise = options.noise_removal(binarized_image)
cv2.imwrite('scriptsImages/no_noise.jpg', no_noise)
options.display('scriptsImages/no_noise.jpg')

# /*********dilation and eroison********************/

eroded_image = options.thin_font(no_noise)
cv2.imwrite('scriptsImages/eroded_image.jpg', eroded_image)
options.display('scriptsImages/eroded_image.jpg')


