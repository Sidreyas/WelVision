import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the image
image_path = ''
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

# Preprocess the image (e.g., Gaussian blur to reduce noise)
blurred = cv2.GaussianBlur(image, (5, 5), 0)

# Edge detection using Canny
edges = cv2.Canny(blurred, 50, 150)

# Find contours
contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Draw contours on the original image
contour_img = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)
cv2.drawContours(contour_img, contours, -1, (0, 255, 0), 1)

# Display the results
plt.figure(figsize=(20, 15))
plt.subplot(1, 2, 1)
plt.title('Original Image')
plt.imshow(image, cmap='gray')

plt.subplot(1, 2, 2)
plt.title('Defects Detected')
plt.imshow(contour_img)

plt.show()
