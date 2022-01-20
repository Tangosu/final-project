import cv2


capture = cv2.VideoCapture('S10_Switronic_Short_Cut_Test.mp4')
ret, frame1 = capture.read()
ret, frame2 = capture.read()

# background image
img = cv2.imread('scr.PNG', 0)
# picture we are looking for
template = cv2.imread('br.png', 0)
h, w = template.shape

# methods for comparison
# methods = [cv2.TM_CCOEFF, cv2.TM_CCOEFF_NORMED, cv2.TM_CCORR,
#            cv2.TM_CCORR_NORMED, cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]
methods = [cv2.TM_CCOEFF]

# test
# for i in methods:
#     img2 = img.copy()
#     # roi = img2[y:y]
#     x = 620
#     y = 150
#     h2, w2 = img2.shape
#     roi = img2[0:400 , x:]
#     print(img2.shape)
#     print(roi.shape)
#
#     # Using convolution to match template to background
#     result = cv2.matchTemplate(roi, template, i)
#
#     # Getting the minimum and maximum location from the result
#     min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
#
#     # TM_SQDIFF gives best match based on minimum location
#     # All other methods use maximum location
#     if i in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
#         location = min_loc
#     else:
#         location = max_loc
#
#     # cv2.rectangle(img2, (150, 150), (100, 200), 255, 2)
#     # Draw a rectangle at where it thinks the template is
#     bottom_right = (location[0] + w, location[1] + h)
#     cv2.rectangle(roi, location, bottom_right, 255, 2)
#     print(min_loc, max_loc)
#
#     cv2.imshow('test', img2)
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()

img2 = img.copy()

# restrict the convolution to the bottom right of the image
# x = 620
# y = 150
# roi = img2[y:, x:x+420]
#
# # Using convolution to match template to background
# result = cv2.matchTemplate(roi, template, cv2.TM_CCOEFF)
# # result = cv2.matchTemplate(img2, template, cv2.TM_CCOEFF)
#
# # Getting the minimum and maximum location from the result
# min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
#
# location = max_loc
#
# # Draw a rectangle at where it thinks the template is
# bottom_right = (location[0] + w, location[1] + h)
# cv2.rectangle(roi, location, bottom_right, 255, 2)
# print(min_loc, max_loc)

# cv2.imshow('test', img2)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


while True:
    # _, frame = capture.read()
    ret, frame = capture.read()
    if ret == True:
        img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # print(img.shape)

        img2 = img.copy()

        # restrict the convolution to the bottom right of the image
        x = 490
        y = 130
        roi = img2[y:, x:x + 350]

        # Using convolution to match template to background
        result = cv2.matchTemplate(roi, template, cv2.TM_CCOEFF)
        # result = cv2.matchTemplate(img2, template, cv2.TM_CCOEFF)

        # Getting the minimum and maximum location from the result
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

        location = max_loc

        # Draw a rectangle at where it thinks the template is
        bottom_right = (location[0] + w, location[1] + h)
        cv2.rectangle(roi, location, bottom_right, 255, 2)
        print(min_loc, max_loc)



        cv2.imshow('PIU', img2)

        if cv2.waitKey(0) == 27:
            break
    else:
        break

capture.release()
cv2.destroyAllWindows()


