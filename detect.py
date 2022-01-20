import cv2

# capture = cv2.VideoCapture('S10_Switronic_Short_Cut.mp4')
capture = cv2.VideoCapture('assets/S10_Switronic_Short_Cut_Test.mp4')
ret, frame1 = capture.read()
ret, frame2 = capture.read()

# background image
img = cv2.imread('assets/scr.PNG', 0)
# picture we are looking for
bl = cv2.imread('assets/bl.png', 0)
br = cv2.imread('assets/br2.png', 0)
c = cv2.imread('assets/c.png', 0)
rr = cv2.imread('assets/rr.png', 0)
rl = cv2.imread('assets/rl.png', 0)

img2 = img.copy()


def search(roi, template, inten,x_axis):
    # Using convolution to match template to background
    h, w = template.shape
    result = cv2.matchTemplate(roi, template, cv2.TM_CCOEFF)

    # Getting the minimum and maximum location from the result
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

    location = max_loc

    # Draw a rectangle at where it thinks the template is
    bottom_right = (location[0] + w, location[1] + h)
    if max_val >= inten:
        # print('yes', max_val, location[0])
        if location[0] > x_axis and location[0] < x_axis + 35:
            cv2.rectangle(roi, location, bottom_right, 255, 2)
    # print(min_loc, max_loc)
    return max_val

lis=[]

bl_axis = 20
rl_axis = 70
c_axis = 120
rr_axis = 175
br_axis = 230
while True:
    # _, frame = capture.read()
    ret, frame = capture.read()
    woah = 10700000
    bl_woah = 16700000
    c_woah = 16700000
    rr_woah = 26555260
    br_woah = 20118964

    if ret == True:
        img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # print(img.shape)

        # img2 = img.copy()

        # restrict the convolution to the bottom right of the image
        x = 490
        y = 320
        # roi = img[y:, x:x + 350]
        area = img[y:, x:x + 350]

        # bl works
        # rl doesnt match for combo 43 / rl-c jump
        # c works
        # rr doesnt match for combo 44 / rr-c jump
        # br
        a1 = search(area, br, woah, br_axis)
        # if a1 >= c_woah:
        #     lis.append(a1)

        cv2.imshow('PIU', img)

        if cv2.waitKey(0) == 27:
            break
    else:
        break

capture.release()
cv2.destroyAllWindows()

# lis.sort()
# print(lis)


