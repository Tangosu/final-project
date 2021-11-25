import cv2
import numpy as np

# capture = cv2.VideoCapture('S10_Switronic_Short_Cut.mp4')
capture = cv2.VideoCapture('S10_Switronic_Short_Cut_Test.mp4')
# x = 520
# y = 460
# start = (x, y)
# end = (x+50, y+50)
# rgb = (0, 255, 0)
ret, frame1 = capture.read()
ret, frame2 = capture.read()
# line1 = cv2.line(frame1, (200, 350), (450, 350), (255, 0, 0), 2)
# line2 = cv2.line(frame1, (500, 350), (800, 350), (255, 0, 0), 2)


while True:
    _, frame = capture.read()

    diff = cv2.absdiff(frame1, frame2)
    gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
    # dilated = cv2.dilate(thresh, None, iterations=3)
    contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # cv2.rectangle(frame, start, end, rgb, 2)
    # line1 = cv2.line(frame1, (150, 350), (450, 350), (255, 0, 0), 2)
    # line2 = cv2.line(frame1, (510, 350), (810, 350), (255, 0, 0), 2)
    count = 0
    for c in contours:
        # if cv2.contourArea(c) < 6000 and cv2.contourArea(c) > 2000:
        #     continue
        # print(y)
        # x, y, w, h = cv2.boundingRect(c)
        if cv2.contourArea(c) < 10000 and cv2.contourArea(c) > 4000:
            count+=1
            print(count,cv2.contourArea(c))
            (x, y, w, h) = cv2.boundingRect(c)
            if y > 325 and (x > 510 and x < 810):
                cv2.rectangle(frame1, (x, y), (x + w, y + h), (0, 255, 0), 2)
                xMid = int((x + (x+w)) / 2)
                yMid = int((x + (y+h)) / 2)
                cv2.circle(frame, (xMid, yMid), 5, (0, 0, 255), 5)

    cv2.imshow('PIU', frame1)

    frame1 = frame2
    ## p1 threshold line
    # cv2.line(frame1, (150, 335), (450, 335), (255, 0, 0), 2)
    # cv2.line(frame1, (150, 370), (450, 370), (0, 0, 255), 2)
    # cv2.line(frame1, (150, 405), (450, 405), (255, 0, 0), 2)

    #
    # # p2 threshold line
    # cv2.line(frame1, (510, 335), (810, 335), (255, 0, 0), 2)
    # cv2.line(frame1, (510, 370), (810, 370), (0, 0, 255), 2)
    # cv2.line(frame1, (510, 405), (810, 405), (255, 0, 0), 2)
    cv2.line(frame1, (510, 325), (510, 500), (0, 0, 255), 2)
    cv2.line(frame1, (810, 325), (810, 500), (255, 0, 0), 2)


    ret, frame2 = capture.read()

    if cv2.waitKey(0) == 27:
        break

capture.release()
cv2.destroyAllWindows()

