# 1. Import the necessary packages
from skimage import measure
import argparse
import imutils
import cv2
from skimage import data, img_as_float
from skimage.metrics import structural_similarity as ssim
from skimage.metrics import mean_squared_error

# 2. Construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-f", "--first", required=True, help="Directory of the image that will be compared")
ap.add_argument("-s", "--second", required=True, help="Directory of the image that will be used to compare")
args = vars(ap.parse_args())

# 3. Load the two input images
imageA = cv2.imread(args["first"])
imageB = cv2.imread(args["second"])

# 4. Convert the images to grayscale
grayA = cv2.cvtColor(imageA, cv2.COLOR_BGR2GRAY)
grayB = cv2.cvtColor(imageB, cv2.COLOR_BGR2GRAY)

# 5. Compute the Structural Similarity Index (SSIM) between the two
#    images, ensuring that the difference image is returned
mse = mean_squared_error(grayA, grayB)
ssim_s = ssim(grayA, grayB,
                  data_range=grayB.max() - grayB.min())


# 6. You can print only the score if you want
print("SSIM: {:.5f} {:.5f}".format(mse,ssim_s))