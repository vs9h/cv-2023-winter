import cv2
import matplotlib.pyplot as plt

img = cv2.imread('pic.jpg')
height, width = img.shape[:2]
M = cv2.getRotationMatrix2D((width / 2, height / 2), 45, 1)
rotated_img = cv2.warpAffine(img, M, (width, height))

plt.imshow(cv2.cvtColor(rotated_img, cv2.COLOR_BGR2RGB))
plt.show()
