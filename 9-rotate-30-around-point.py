import cv2

rotation_angle = 30
pivot_point = (100, 100)

original_image = cv2.imread('pic.jpg')
height, width = original_image.shape[:2]
rotation_matrix = cv2.getRotationMatrix2D(pivot_point, rotation_angle, 1.0)
rotated_image = cv2.warpAffine(original_image, rotation_matrix, (width, height))
cv2.imwrite('pic-transformed.jpg', rotated_image)
