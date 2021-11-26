import cv2
import math
import detection

capture = cv2.VideoCapture('S10_Switronic_Short_Cut_Test.mp4')
ret, frame1 = capture.read()
ret, frame2 = capture.read()

prev_mid_pts = []
track_obj = {}
unique_obj = []
track_id = 0

while True:
    _, frame = capture.read()

    curr_mid_pts = []
    contours, _ = detection.cont(frame1, frame2)

    # Highlights the arrows in a green square on the bottom right of the screen
    for c in contours:
        if cv2.contourArea(c) < 10000 and cv2.contourArea(c) > 4000:
            (x, y, w, h) = cv2.boundingRect(c)

            # Hard coded values for bottom right of the screen
            if y > 325 and (x > 510 and x < 810):
                cv2.rectangle(frame1, (x, y), (x + w, y + h), (0, 255, 0), 2)

                # mid point of the contour
                xMid = int((x + x + w) / 2)
                yMid = int((y + y + h) / 2)
                curr_mid_pts.append((xMid, yMid))

    if len(track_obj) < 1:
        # Compares the current mid point of the contour to the previous mid point.
        # If the distance of the mid point is close (within 36 pxl), the current mid point will be
        # added to the track_obj dictionary. This is used as a way to track a unique moving object
        for i in curr_mid_pts:
            for j in prev_mid_pts:
                dist = math.hypot(j[0] - i[0], j[1] - i[1])
                if dist < 36:
                    track_obj[track_id] = i
                    track_id += 1
    else:
        # Checks a copy of the track_obj dictionary and checks if the current mid point is already in it.
        # If not, it will add it to the unique_obj array.
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
                unique_obj.append(k)

    # A visual of the number of moving objects
    for i, j in track_obj.items():
        cv2.putText(frame1, str(i), (j[0], j[1]-7), 2, 1, (255, 0, 255))

    print(len(unique_obj))

    cv2.imshow('PIU', frame1)

    frame1 = frame2
    prev_mid_pts = curr_mid_pts.copy()
    ret, frame2 = capture.read()

    if cv2.waitKey(120) == 27:
        break

capture.release()
cv2.destroyAllWindows()

