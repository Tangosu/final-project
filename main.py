import cv2
import detection

capture = cv2.VideoCapture('assets/S10_Switronic_Short_Cut.mp4')
# capture = cv2.VideoCapture('assets/S10_Switronic_Short_Cut_Test.mp4')
ret, frame1 = capture.read()

# picture we are looking for
bl = cv2.imread('assets/bl.png', 0)
br = cv2.imread('assets/br2.png', 0)
c = cv2.imread('assets/c.png', 0)
rr = cv2.imread('assets/rr.png', 0)
rl = cv2.imread('assets/rl.png', 0)

# arrow axis on roi
bl_axis = 20
rl_axis = 70
c_axis = 120
rr_axis = 175
br_axis = 230
while True:
    ret, frame = capture.read()

    if ret == True:
        img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # bl works
        # rl doesnt match for combo 43 / rl-c jump
        # c works
        # rr doesnt match for combo 44 / rr-c jump
        # br
        # detection for arrows
        left_blue = detection.search(img, bl, bl_axis)
        left_red = detection.search(img, rl, rl_axis)
        centre = detection.search(img, c, c_axis)
        right_red = detection.search(img, rr, rr_axis)
        right_blue = detection.search(img, br, br_axis)

        cv2.imshow('PIU', img)

        if cv2.waitKey(0) == 27:
            break
    else:
        break

capture.release()
cv2.destroyAllWindows()

