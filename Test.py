import cv2
import numpy as np
import math

# capture = cv2.VideoCapture('S10_Switronic_Short_Cut.mp4')
capture = cv2.VideoCapture('S10_Switronic_Short_Cut_Test.mp4')
ret, frame1 = capture.read()
ret, frame2 = capture.read()

prev_mid_pts = []
track_obj = {}
track_id = 0
count = 0
counter = 0
fRame = 0
flag = False


while True:
    _, frame = capture.read()

    count += 1
    fRame += 1

    curr_mid_pts = []

    diff = cv2.absdiff(frame1, frame2)
    gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
    contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for c in contours:
        if cv2.contourArea(c) < 10000 and cv2.contourArea(c) > 4000:
            (x, y, w, h) = cv2.boundingRect(c)
            if y > 325 and (x > 510 and x < 810):

                cv2.rectangle(frame1, (x, y), (x + w, y + h), (0, 255, 0), 2)

                #mid point
                xMid = int((x + x + w) / 2)
                yMid = int((y + y + h) / 2)

                curr_mid_pts.append((xMid, yMid))

                cv2.circle(frame1, (xMid, yMid), 5, (0, 0, 255), 5)

                # flag = True
                # if flag == True:
                #     counter+=1

    if len(track_obj) < 1:
    # if flag == True:
        for i in curr_mid_pts:
            for j in prev_mid_pts:
                # print(j[0],i[0],j[1],i[1])
                dist = math.hypot(j[0] - i[0], j[1] - i[1])
                # print(dist)
                if dist < 36:
                    track_obj[track_id] = i
                    track_id += 1
                    print("1st",track_obj)
    else:
        for j, k in track_obj.copy().items():
            obj_exist = False
            for i in curr_mid_pts:
                dist = math.hypot(k[0] - i[0], k[1] - i[1])
                if dist < 36:
                    track_obj[j] = i
                    obj_exist = True
                    continue
            if not obj_exist:
                track_obj.pop(j)

    for i, j in track_obj.items():
        cv2.circle(frame1, j, 5, (0, 0, 255), 5)
        cv2.putText(frame1, str(i), (j[0], j[1]-7), 2, 1, (255, 0, 255))

    cv2.imshow('PIU', frame1)

    frame1 = frame2
    prev_mid_pts = curr_mid_pts.copy()

    ## p1 threshold line
    # cv2.line(frame1, (150, 335), (450, 335), (255, 0, 0), 2)
    # cv2.line(frame1, (150, 370), (450, 370), (0, 0, 255), 2)
    # cv2.line(frame1, (150, 405), (450, 405), (255, 0, 0), 2)

    # # p2 threshold line
    # cv2.line(frame1, (510, 335), (810, 335), (255, 0, 0), 2)
    # cv2.line(frame1, (510, 370), (810, 370), (0, 0, 255), 2)
    # cv2.line(frame1, (510, 405), (810, 405), (255, 0, 0), 2)


    ret, frame2 = capture.read()

    if cv2.waitKey(0) == 27:
        break

capture.release()
cv2.destroyAllWindows()

