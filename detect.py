import cv2


# background image
img = cv2.imread('scr.PNG', 0)
# picture we are looking for
template = cv2.imread('bl.png', 0)
h, w = template.shape
print(template.shape)

# methods for comparison
methods = [cv2.TM_CCOEFF, cv2.TM_CCOEFF_NORMED, cv2.TM_CCORR,
           cv2.TM_CCORR_NORMED, cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]

for i in methods:
    img2 = img.copy()
    # roi = img2[y:y]

    # Using convolution to match template to background
    result = cv2.matchTemplate(img2, template, i)

    # Getting the minimum and maximum location from the result
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

    # TM_SQDIFF gives best match based on minimum location
    # All other methods use maximum location
    if i in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        location = min_loc
    else:
        location = max_loc

    # cv2.rectangle(img2, 50, 50, 255, 2)
    # Draw a rectangle at where it thinks the template is
    bottom_right = (location[0] + w, location[1] + h)
    cv2.rectangle(img2, location, bottom_right, 255, 2)
    print(min_loc, max_loc)

    cv2.imshow('test', img2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


