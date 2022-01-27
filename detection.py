# Find arrows using template matching
import cv2


def search(img, template, x_axis):
    # restrict the convolution to the bottom right of the image
    x = 490
    y = 320
    roi = img[y:, x:x + 350]

    # Using convolution to match template to background
    h, w = template.shape
    result = cv2.matchTemplate(roi, template, cv2.TM_CCOEFF)

    # Getting the minimum and maximum location from the result
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

    location = max_loc

    # Draw a rectangle at where it thinks the template is
    bottom_right = (location[0] + w, location[1] + h)
    if max_val >= 10000000:
        if location[0] > x_axis and location[0] < x_axis + 35:
            cv2.rectangle(roi, location, bottom_right, 255, 2)
    return max_val
