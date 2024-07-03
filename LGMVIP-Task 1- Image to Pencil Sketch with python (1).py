#!/usr/bin/env python
# coding: utf-8

# # LGMVIP-Task 1- Image to Pencil Sketch with python

# # Step 1: Read the Image in RGB Format
# 
# In this step, we begin by loading an image from a specified file path using OpenCV. The image is initially read in BGR format, which is the default format used by OpenCV. To properly display the image using Matplotlib, which expects RGB format, we convert the image from BGR to RGB. This conversion ensures the colors are displayed correctly.

# In[29]:


import cv2
import matplotlib.pyplot as plt

#loading image path
image_path = r'C:\Users\SANSHIYA\Downloads\archive (13)\input_image.png'

#Read the image in RGB format
image = cv2.imread(image_path)
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

#Display the original image
plt.imshow(image_rgb)
plt.title('Original Image')
plt.axis('off')
plt.show()


# # Step 2: Convert the Image to Grayscale
# 
# In this step, we proceed to convert the RGB image to a grayscale image. Grayscale images simplify the color information by reducing it to shades of gray, which is essential for various image processing techniques.
# 
# First, we read the image from the specified file path in RGB format, as done in the previous step. Next, we use OpenCV’s cv2.cvtColor function to convert the RGB image to grayscale. The conversion process involves transforming the multi-channel RGB image into a single-channel grayscale image, where each pixel represents a shade of gray.
# 
# To visualize the result, we use Matplotlib to display the grayscale image. We utilize the plt.imshow function with the cmap='gray' parameter to ensure the image is rendered in grayscale. Additionally, we add a title, 'Grayscale Image', to the plot and hide the axis for a cleaner view.

# In[30]:


#Convert to grayscale
gray_image = cv2.cvtColor(image_rgb, cv2.COLOR_RGB2GRAY)

#Display the image
plt.imshow(gray_image, cmap='gray')
plt.title('Grayscale Image')
plt.axis('off')
plt.show()


# # Step 3: Invert the Grayscale Image
# 
# After converting the image to grayscale, the next step involves creating an inverted version of this grayscale image. Inverting the grayscale image means that the light areas become dark and the dark areas become light. This inversion can enhance certain details and is a crucial step in creating a pencil sketch effect.
# 
# We use the cv2.bitwise_not function from OpenCV to invert the grayscale image. This function performs a bitwise NOT operation on each pixel, effectively inverting the image.

# In[31]:


#Invert the grayscale image
inverted_gray_image = cv2.bitwise_not(gray_image)

#Display the inverted grayscale image
plt.imshow(inverted_gray_image, cmap='gray')
plt.title('Inverted Grayscale Image')
plt.axis('off')
plt.show()


# # Step 4: Apply Gaussian Blur to the Inverted Image
# 
# The next step is to apply a Gaussian blur to the inverted grayscale image. Blurring smoothens the image, reducing noise and detail, which helps in the final sketch effect by creating a soft, pencil-like texture.
# 
# We use the cv2.GaussianBlur function to apply the blur. The function requires the image, the size of the kernel, and the standard deviation as parameters. Here, we use a kernel size of (21, 21) and a standard deviation of 0.

# In[32]:


#Apply Gaussian blur to the inverted image
blurred_image = cv2.GaussianBlur(inverted_gray_image, (21, 21), 0)

#Display the blurred image
plt.imshow(blurred_image, cmap='gray')
plt.title('Blurred Image')
plt.axis('off')
plt.show()


# # Step 5: Invert the Blurred Image
# 
# After blurring the inverted grayscale image, we invert it again. This step is essential because it sets up the image for the final sketch creation by making the bright areas darker and vice versa.

# In[33]:


#Invert the blurred image
inverted_blurred_image = cv2.bitwise_not(blurred_image)

#Display the inverted blurred image
plt.imshow(inverted_blurred_image, cmap='gray')
plt.title('Inverted Blurred Image')
plt.axis('off')
plt.show()


# # Step 6: Create the Pencil Sketch
# 
# Finally, we create the pencil sketch by dividing the grayscale image by the inverted blurred image. This division amplifies the edges and details, giving the appearance of a pencil sketch. We use the cv2.divide function for this operation, specifying a scale factor to ensure the pixel values are correctly scaled.

# In[34]:


#Create the pencil sketch by dividing the grayscale image by the inverted blurry image
pencil_sketch = cv2.divide(gray_image, inverted_blurred_image, scale=256.0)

#Display the pencil sketch
plt.imshow(pencil_sketch, cmap='gray')
plt.title('Pencil Sketch')
plt.axis('off')
plt.show()


# In[ ]:




