# Template_Matching

## Goals
<ul>
<li> To find objects in an image using Template Matching</li>
<li> Use this functions: cv2.matchTemplate(), cv2.minMaxLoc()</li>
</ul>

## Theory
Template Matching is a method for searching and finding the location of a template image in a larger image.<br>
OpenCV comes with a function cv2.matchTemplate() for this purpose.<br>
It simply slides the template image over the input image (as in 2D convolution) and compares the template and patch of input image under the template image.<br>
Several comparison methods are implemented in OpenCV. (You can check docs for more details).<br>
It returns a grayscale image, where each pixel denotes how much does the neighbourhood of that pixel match with template.
