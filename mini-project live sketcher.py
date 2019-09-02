#!/usr/bin/env python
# coding: utf-8

# In[2]:


import cv2

import numpy as np 

def sketch(image):
    img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    #applying gaussian blur
    img_gray_blur = cv2.GaussianBlur(img_gray,(5,5), 0)
    #apply the canny edge detection algorithm
    canny_edges = cv2.Canny(img_gray_blur, 10, 70)
    #thresholding to optimize
    ret,mask = cv2.threshold(canny_edges, 70, 255, cv2.THRESH_BINARY_INV)
    return mask

#get hand over camera
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    cv2.imshow("our live sketcher", sketch(frame))
    if cv2.waitKey(2) == 13:
        break
cap.release()
cv2.destroyAllWindows()


# In[ ]:





# In[ ]:





# In[ ]:




