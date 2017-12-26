import cv2
import glob
import numpy as np
import pytesseract
from PIL import Image

count=1

for img1 in glob.glob("C:\\Users\\Vamsi\\Desktop\\ser\\sample\\*.jpg"):
    img = cv2.imread(img1)
# RGB to Gray scale conversion
    img_gray = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)

# Noise removal with iterative bilateral filter(removes noise while preserving edges)
    noise_removal = cv2.bilateralFilter(img_gray,9,75,75)


# Histogram equalisation for better results
    equal_histogram = cv2.equalizeHist(noise_removal)

# Morphological opening with a rectangular structure element
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(5,5))
    morph_image = cv2.morphologyEx(equal_histogram,cv2.MORPH_OPEN,kernel,iterations=300)

# Image subtraction(Subtracting the Morphed image from the histogram equalised Image)
    sub_morp_image = cv2.subtract(equal_histogram,morph_image)

# Thresholding the image
    ret,thresh_image = cv2.threshold(sub_morp_image,0,255,cv2.THRESH_OTSU)

# Applying Canny Edge detection
    canny_image = cv2.Canny(thresh_image,250,255)
    canny_image = cv2.convertScaleAbs(canny_image)

# dilation to strengthen the edges
    kernel = np.ones((3,3), np.uint8)
# Creating the kernel for dilation
    dilated_image = cv2.dilate(thresh_image,kernel,iterations=1)

# Finding Contours in the image based on edges
    new,contours, hierarchy = cv2.findContours(thresh_image, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contours= sorted(contours, key = cv2.contourArea, reverse = True)[:10]
# Sort the contours based on area ,so that the number plate will be in top 10 contours
    screenCnt = None
# loop over our contours
    for c in contours:
 # approximate the contour
     peri = cv2.arcLength(c, True)
     approx = cv2.approxPolyDP(c, 0.06 * peri, True)  # Approximating with 6% error
 # if our approximated contour has four points, then
 # we can assume that we have found our screen
     if len(approx) == 4:  # Select the contour with 4 corners
      screenCnt = approx
      ctr = np.array(screenCnt).reshape((-1,1,2)).astype(np.int32)
      break
    final = cv2.drawContours(img,[ctr], -1, (0, 255, 0), 3)
# Drawing the selected contour on the original image
# Masking the part other than the number plate
    mask = np.zeros(img_gray.shape,np.uint8)
    new_image = cv2.drawContours(mask,[ctr],0,255,-1,)
    new_image = cv2.bitwise_and(img,img,mask=mask)

# Histogram equal for enhancing the number plate for further processing
    y,cr,cb = cv2.split(cv2.cvtColor(new_image,cv2.COLOR_RGB2YCrCb))
# Converting the image to YCrCb model and splitting the 3 channels
    y = cv2.equalizeHist(y)
# Applying histogram equalisation
    final_image = cv2.cvtColor(cv2.merge([y,cr,cb]),cv2.COLOR_YCrCb2RGB)
    img_gray1 = cv2.cvtColor(final_image,cv2.COLOR_RGB2GRAY)
    noise_removal1 = cv2.bilateralFilter(img_gray1,9,75,75)
    equal_histogram1 = cv2.equalizeHist(noise_removal1)
    kernel1 = cv2.getStructuringElement(cv2.MORPH_RECT,(5,5))

    morph_image1 = cv2.morphologyEx(equal_histogram1,cv2.MORPH_OPEN,kernel1,iterations=150)
    sub_morp_image1 = cv2.subtract(equal_histogram1,morph_image1)
    ret1,thresh_image1 = cv2.threshold(sub_morp_image1,0,255,cv2.THRESH_OTSU)
    cv2.imwrite('now'+str(count)+'.JPG', thresh_image1)
    count=count+1
cv2.waitKey() # Wait for a keystroke from the user
