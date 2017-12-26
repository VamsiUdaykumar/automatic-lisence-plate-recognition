Step-by-step guide to LPR

Prerequisites:

Tesseract version 3.04: https://github.com/tesseract-ocr/tesseract

Python 3.5 :https://www.python.org/downloads/release/python-350/

Anaconda :https://anaconda.org/anaconda/python

Pytesseract package : pip install pytesseract

OpenCV 2 : conda install -c conda-forge opencv 

Pillow : pip install PILLOW

Instructions:

1) Install the above prerequisites

2) Make Sure the environment variables are updated in Windows and the bash_profile is updated in mac/linux systems

3) Open the FinalAlpr/localise.py directory on any text editor

4) Change the path in the for loop where the images are stored but leave the "/*.JPG" part alone, unless your images are not in JPG format you can change the extension accordingly. 

5) Change the output directories in the lower part where we store the intermediate images.

6) Make the same changes accordindly in ocr.py if you make changes in the Step-5

7) Now open terminal/command prompt

8) Go to the place where you have stored FinalAlpr

9) Execute-:
    First go to the folder where the code for the localisation of the image is stored and execute the code using
		python3 localise.py
	After execution is over you can see the images after localisation stored in the given directory
	Go to the folder where the ocr part of the code is stored
	Execute the ocr.py using
		python3 ocr.py
		
10) You will see the output i.e the license plate number on the terminal