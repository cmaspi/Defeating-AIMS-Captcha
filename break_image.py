import numpy as np
import os
import cv2 as cv


def sep_image(img : np.ndarray, name : str):
    """
    Takes in input as image in form of a numpy array which represents the images.
    It breaks down the image into separate characters and returns the images of size 30 x 30 along with labels
    """
    # Return variable
    ret = []

    # Converting to Gray scale
    img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    
    # Removing all the noisy information from the captcha images
    # 220 is the threshold that we use, any pixel with lower intensity
    # is set to 0 (black)
    # anything higher is set to 255 (white)
    img[img < 220] = 0
    img[img >= 220] = 255


    # Finding Contours
    # contours are basically the separate blobs of pixels
    contours, _ = cv.findContours(img, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    # sorting the contours in left to right order
    contours = sorted(contours, key = lambda x: x[0][0][0])

    # count of how many characters we have accounted for
    j = 0

    # the number of countours can be more than 5 or even less than 5
    # If we have the letter j, the dot on top counts as a separate blob.
    # Sometimes we can have 2 letters joined and that would be a single blob
    for i in range(contours.__len__()):
        if j >= 5:
            break
        
        # the left top point is x,y. w,h are the dimensions of 
        # rectangle surrounding this contour
        x, y, w, h = cv.boundingRect(contours[i])

        if h < 10 and w < 10:
            # Case when the dot over j is a separate contour
            continue
        
        # When two characters are joint and are considered as same contour
        if w/h > 1.5:
            char1 = img[y-2 : y+h+2, x-2 : x+ w//2 +2]
            char2 = img[y-2 : y+h+2, x+w//2-2 : x+ w +2]

            #resizing the image to standardise the dimension
            char1 = cv.resize(char1, (30,30), cv.INTER_AREA)
            char2 = cv.resize(char2, (30,30), cv.INTER_AREA)
            

            ret.append([char1.reshape((30,30,1)), name[j]])
            ret.append([char2.reshape((30,30,1)), name[j+1]])
            j += 2
            continue
        # We need to include the dot over j, there's no i in captcha images
        # I just made the assumption that j will never appear in a joint character case
        if name[j] == 'j':
            char = img[y-10:y+h+2, x-4:x+w+4]
            char = cv.resize(char, (30,30), cv.INTER_AREA)
            
        else:
            char = img[y-2:y+h+2, x-2:x+w+2]
            char = cv.resize(char, (30,30), cv.INTER_AREA)

        ret.append([char.reshape((30,30,1)), name[j]])
        j+=1
    return ret

if __name__ == '__main__':
    dataset = []

    for filename in os.listdir("images/"):
        img = cv.imread("images/"+filename)
        dataset.extend(sep_image(img, filename))

    dataset = np.array(dataset, dtype = object)
    np.save('character.npy', dataset)

