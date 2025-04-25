import pandas as pd
from PIL import Image
from matplotlib.image import imread
import matplotlib.pyplot as plt

img_path = r"C:\Users\bharg\Documents\Sunny\Images\car-photo.png"


car = imread(r"C:\Users\bharg\Documents\Sunny\Images\car-photo.png")
print(car)
#print(car.shape)
plt.hist(car.ravel(), bins=256, color='gray')
plt.title("Pixel Intensity Histogram")
plt.xlabel("Pixel Value")
plt.ylabel("Frequency")
plt.show()