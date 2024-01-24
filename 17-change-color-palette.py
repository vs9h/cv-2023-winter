import cv2
import numpy as np

image = cv2.imread('pic.jpg')

template_colors = {
    (0, 0, 255): (0, 255, 0),
    (0, 255, 0): (255, 0, 0)
}

image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

mapped_image = np.zeros_like(image_rgb)

for old_color, new_color in template_colors.items():
    mask = np.all(image_rgb == np.array(old_color), axis=-1)
    mapped_image[mask] = new_color

mapped_image_bgr = cv2.cvtColor(mapped_image, cv2.COLOR_RGB2BGR)

cv2.imshow('Mapped Image', mapped_image_bgr)
cv2.waitKey(0)
cv2.destroyAllWindows()
