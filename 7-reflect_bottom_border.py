import cv2
import matplotlib.pyplot as plt

img = cv2.imread('pic.jpg')
height = img.shape[0]
reflected_img = cv2.copyMakeBorder(img, 0, height, 0, 0, cv2.BORDER_REFLECT)

plt.imshow(cv2.cvtColor(reflected_img, cv2.COLOR_BGR2RGB))
plt.show()
