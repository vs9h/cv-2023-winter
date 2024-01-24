import cv2
import numpy as np
from matplotlib import pyplot as plt

image = cv2.imread('pic.jpg', cv2.IMREAD_GRAYSCALE)

f_transform = np.fft.fft2(image)
f_transform_shifted = np.fft.fftshift(f_transform)

rows, cols = image.shape
crow, ccol = rows // 2, cols // 2
mask_radius = 30

mask = np.ones((rows, cols), np.uint8)
center = (crow, ccol)
x, y = np.ogrid[:rows, :cols]
mask_area = (x - center[0])**2 + (y - center[1])**2 <= mask_radius**2
mask[mask_area] = 0

f_transform_shifted_filtered = f_transform_shifted * mask
filtered_image = np.abs(np.fft.ifft2(np.fft.ifftshift(f_transform_shifted_filtered)))

plt.subplot(131), plt.imshow(image, cmap='gray'), plt.title('Original Image')
plt.subplot(132), plt.imshow(filtered_image, cmap='gray'), plt.title('Filtered Image')
plt.subplot(133), plt.imshow(mask, cmap='gray'), plt.title('Mask')
plt.show()
