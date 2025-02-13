#!/usr/bin/env python
# coding: utf-8

# In[7]:


import cv2

# Load an image (Change the path if needed)
image = cv2.imread("sample.jpg")

# Display the image
cv2.imshow("Sample Image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

