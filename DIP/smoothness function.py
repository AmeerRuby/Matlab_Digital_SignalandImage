import cv2
import numpy as np

# Load the images
img1 = cv2.imread('image 1.jpeg')
img2 = cv2.imread('image 2.jpeg')
img3 = cv2.imread('image 3.jpeg')

# Convert the images to grayscale
gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
gray3 = cv2.cvtColor(img3, cv2.COLOR_BGR2GRAY)

# Compute the smoothness descriptor R
R1 = np.mean(cv2.Laplacian(gray1, cv2.CV_64F)**2)
R2 = np.mean(cv2.Laplacian(gray2, cv2.CV_64F)**2)
R3 = np.mean(cv2.Laplacian(gray3, cv2.CV_64F)**2)

# Compute the third and fourth moments
moments1 = cv2.moments(gray1)
moments2 = cv2.moments(gray2)
moments3 = cv2.moments(gray3)
third_moments = [moments1['mu20'] + moments1['mu02'],
                 moments2['mu20'] + moments2['mu02'],
                 moments3['mu20'] + moments3['mu02']]
fourth_moments = [moments1['mu30'] + 3*moments1['mu12'],
                  moments2['mu30'] + 3*moments2['mu12'],
                  moments3['mu30'] + 3*moments3['mu12']]

# Print the results
print("Image 1 - R: {:.2f}, Third Moment: {:.2f}, Fourth Moment: {:.2f}".format(R1, third_moments[0], fourth_moments[0]))
print("Image 2 - R: {:.2f}, Third Moment: {:.2f}, Fourth Moment: {:.2f}".format(R2, third_moments[1], fourth_moments[1]))
print("Image 3 - R: {:.2f}, Third Moment: {:.2f}, Fourth Moment: {:.2f}".format(R1, third_moments[2], fourth_moments[2]))
