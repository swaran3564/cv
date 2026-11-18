
import cv2
import matplotlib.pyplot as plt

img = cv2.imread(r"C:\Users\NISHKA\OneDrive\Desktop\ce\img1.webp", 0)
img = cv2.resize(img, (300,300))
equ = cv2.equalizeHist(img)

plt.figure(figsize=(10,6))

plt.subplot(2,2,1)
plt.imshow(img, cmap='gray')
plt.title("Original")
plt.axis('off')

plt.subplot(2,2,2)
plt.hist(img.ravel(), 256, [0,256], color='black')
plt.title("Original Histogram")

plt.subplot(2,2,3)
plt.imshow(equ, cmap='gray')
plt.title("Equalized")
plt.axis('off')

plt.subplot(2,2,4)
plt.hist(equ.ravel(), 256, [0,256], color='black')
plt.title("Equalized Histogram")

plt.tight_layout()
plt.show()

print("Histogram Equalization Completed")
