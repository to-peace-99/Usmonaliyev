# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1hYJbSfit5ZAWRUuW2O_TYb4ezbV19gjQ
"""

pip install opencv-python

from google.colab.patches import cv2_imshow
import cv2
rasm=cv2.imread("rasm.jpg")
rasm1=cv2.imread("rasm1.jpg")
rasm2=cv2.imread("rasm2.jpg")
rasm3=cv2.imread("rasm3.jpg")
rasm4=cv2.imread("rasm4.jpg")
cv2_imshow(rasm)
cv2_imshow(rasm1)
cv2_imshow(rasm2)
cv2_imshow(rasm3)
cv2_imshow(rasm4)

oqqora=cv2.cvtColor(rasm,cv2.COLOR_BGR2GRAY)
cv2_imshow(oqqora)
oqqora1=cv2.cvtColor(rasm1,cv2.COLOR_BGR2GRAY)
cv2_imshow(oqqora1)
oqqora2=cv2.cvtColor(rasm2,cv2.COLOR_BGR2GRAY)
cv2_imshow(oqqora2)
oqqora3=cv2.cvtColor(rasm3,cv2.COLOR_BGR2GRAY)
cv2_imshow(oqqora3)
oqqora4=cv2.cvtColor(rasm4,cv2.COLOR_BGR2GRAY)
cv2_imshow(oqqora4)