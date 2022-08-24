'''Para varios template: OpenCV Template Machine
(https://opencv24-python-tutorials.readthedocs.io/en/stable/py_tutorials/py_imgproc/py_template_matching/py_template_matching.html) '''
import cv2
import os
import numpy as np
from matplotlib import pyplot as plt

file_path = os.path.dirname(__file__)
relative_path = "/results"
full_path = file_path + relative_path

img_rgb = cv2.imread('medidor_template.jpg')
img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
template = cv2.imread('display_template.jpg',0)
w, h = template.shape[::-1]

res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
threshold = 0.8
loc = np.where( res >= threshold)
for pt in zip(*loc[::-1]):
    cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)

file_name = full_path + '/' + 'display_result' +'.png'
cv2.imwrite(file_name,img_rgb)