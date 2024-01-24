import cv2
import numpy as np
from matplotlib import pyplot as plt

binary_image = cv2.imread('pic.jpg', cv2.IMREAD_GRAYSCALE)

kernel_size = (5, 5)
kernel = np.ones(kernel_size, np.uint8)

dilated_image = cv2.dilate(binary_image, kernel, iterations=1)

plt.subplot(121), plt.imshow(binary_image, cmap='gray'), plt.title('Original Image')
plt.subplot(122), plt.imshow(dilated_image, cmap='gray'), plt.title('Dilated Image')
plt.show()
