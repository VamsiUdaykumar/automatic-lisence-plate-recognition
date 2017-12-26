import cv2
from PIL import Image
import glob
import numpy as np
count = 1
while count < 26 :
    
    im = Image.open("pic"+str(count)+".JPG")
    size = 7016, 4961
    im_resized = im.resize(size, Image.ANTIALIAS)
    im_resized.save("dp"+str(count)+".JPG",dpi=(300,300))
    cv2.waitKey() # Wait for a keystroke from the user
    count = count+1
