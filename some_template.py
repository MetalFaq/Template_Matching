''' Para un solo template: OpenCV Template Maching
(https://opencv24-python-tutorials.readthedocs.io/en/stable/py_tutorials/py_imgproc/py_template_matching/py_template_matching.html) '''
import os
import cv2
import numpy as np
from matplotlib import pyplot as plt

file_path = os.path.dirname(__file__)
relative_path = "/results"
full_path = file_path + relative_path

img = cv2.imread('medidor_template.jpg',0)
template = cv2.imread('res_template.jpg',0)
w, h = template.shape[::-1]

# All the 6 methods for comparison in a list
methods = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR',
            'cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']
count = 0
for meth in methods:
    img_copy = img.copy()
    method = eval(meth)

    # Apply template Matching
    res = cv2.matchTemplate(img_copy,template,method)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

    # If the method is TM_SQDIFF or TM_SQDIFF_NORMED, take minimum
    if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        top_left = min_loc
    else:
        top_left = max_loc
    bottom_right = (top_left[0] + w, top_left[1] + h)

    cv2.rectangle(img,top_left, bottom_right, 255, 2)

    plt.subplot(121),plt.imshow(res,cmap = 'gray')
    plt.title('Matching Result'), plt.xticks([]), plt.yticks([])
    plt.subplot(122),plt.imshow(img,cmap = 'gray')
    plt.title('Detected Point'), plt.xticks([]), plt.yticks([])
    plt.suptitle(meth)

    plt.show()
    
    file_name = full_path + '/' + f'res_{meth}' +'.png'    
    cv2.imwrite(file_name,img_copy)
    