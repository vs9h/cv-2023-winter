import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('pic.jpg')
brightness_reduction = 50
result = cv2.subtract(img, np.full(img.shape, brightness_reduction, dtype=np.uint8))

plt.imshow(cv2.cvtColor(result, cv2.COLOR_BGR2RGB))
plt.show()
