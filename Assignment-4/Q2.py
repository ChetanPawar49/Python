import numpy as np
import matplotlib.pyplot as plt

# Sample 3D RGB array representing an image (height, width, 3)
# For simplicity, we'll use a small 3x3 RGB image
rgb_image = np.array([
    [[255, 0, 0], [0, 255, 0], [0, 0, 255]],   # Red, Green, Blue pixels
    [[255, 255, 0], [255, 0, 255], [0, 255, 255]],  # Yellow, Magenta, Cyan pixels
    [[123, 111, 222], [234, 210, 123], [100, 100, 100]]  # Random pixel colors
])

# 1. Convert RGB image to Grayscale
# Grayscale conversion formula: 0.2989 * R + 0.5870 * G + 0.1140 * B
grayscale_image = np.dot(rgb_image[..., :3], [0.2989, 0.5870, 0.1140])

print("Grayscale Image:\n", grayscale_image)

# 2. Apply a threshold to create a binary image (threshold value of 128)
threshold = 128
binary_image = (grayscale_image > threshold) * 255  # Pixels > 128 become white (255), others black (0)

print("\nBinary Image:\n", binary_image)

# Optional: Display the original, grayscale, and binary images using matplotlib
plt.figure(figsize=(10, 3))

# Display original image
plt.subplot(1, 3, 1)
plt.imshow(rgb_image.astype(np.uint8))
plt.title('Original RGB Image')
plt.axis('off')

# Display grayscale image
plt.subplot(1, 3, 2)
plt.imshow(grayscale_image, cmap='gray')
plt.title('Grayscale Image')
plt.axis('off')

# Display binary image
plt.subplot(1, 3, 3)
plt.imshow(binary_image, cmap='gray')
plt.title('Binary Image')
plt.axis('off')

plt.show()