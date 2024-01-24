import cv2
import matplotlib.pyplot as plt

img = cv2.imread('pic.jpg')
blurred_img = cv2.GaussianBlur(img, (51,51), 0)

plt.imshow(cv2.cvtColor(blurred_img, cv2.COLOR_BGR2RGB))
plt.show()
