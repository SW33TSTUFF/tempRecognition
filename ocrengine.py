import pytesseract
import PIL.Image
import cv2

"""
Page segmentation modes: 
O Orientation and script detection (OSD) only
1 Automatic page segmentation with OSD. ‘
2 Automatic page segmentation, but no OSD, or OCR.
3 Fully automatic page segmentation, but no OSD. (Default)
4 Assume a single column of text of variable sizes.
5 Assume a single uniform block of vertically aligned text.
6 Assume a single uniform block of textJ
7 Treat the image as a single text line.
8 Treat the image as a single word.
9 Treat the image as a single word in a circle.
10 Treat the image as a single character.
11 Sparse text. Find as much text as possible in no particular order.
12 Sparse text with OSD.
13 Raw line. Treat the image as a single text line, bypassing hacks that are Tesseract—specific.

"""

"""
OCR Engine Mode 
0   Legacy engine only
1 Neural nets LSTM engine only
2 Lgeacy + LSTM engines
3 Default, based on what is available

"""

myconfig = r"-l eng --psm 11 --oem 1 outputbase digits"

img = cv2.imread("crow.border.png")
height, width, _ = img.shape

boxes = pytesseract.image_to_boxes(img, config=myconfig)
# print(boxes)

for box in boxes.splitlines():
    box = box.split(" ")
    image = cv2.rectangle(img, (int(box[1]), height - int(box[2])), (int(box[3]), height - int(box[4])), (0, 255, 0), 2)
cv2.imshow("img", img)
cv2.waitKey(0)


# text = pytesseract.image_to_string(PIL.Image.open("crow.png"), config=myconfig)
# print(text)