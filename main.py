import cv2
import detection

v='assets/staircase.mp4'
capture = cv2.VideoCapture(v)
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

prev_co = []
track_obj = {}
unique_obj = []
track_id = 0
x = 490
y = 320

while True:
    ret, frame = capture.read()

    if ret == True:

        current_co = []
        img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # detection for arrows
        left_blue = detection.search(img, bl, bl_axis)
        left_red = detection.search(img, rl, rl_axis)
        centre = detection.search(img, c, c_axis)
        right_red = detection.search(img, rr, rr_axis)
        right_blue = detection.search(img, br, br_axis)

        # adds the co-ordinates of the arrow to current array
        if left_blue is not None:
            current_co.append(left_blue)
        if left_red is not None:
            current_co.append(left_red)
        if centre is not None:
            current_co.append(centre)
        if right_red is not None:
            current_co.append(right_red)
        if right_blue is not None:
            current_co.append(right_blue)

        # Compares the current co-ordinate of the arrow to the previous co-ordinate.
        # If the distance of the mid point is close (within 25 pxl), the current co-ordinate will be
        # added to the track_obj dictionary. This is used as a way to track a unique moving object
        if len(track_obj) < 1:
            for i in range(len(prev_co)):
                if len(current_co) == len(prev_co):
                    dist = prev_co[i][1]-current_co[i][1]
                    if dist < 25 and dist > 0:
                        track_obj[track_id] = current_co
                        track_id += 1

        # Checks a copy of the track_obj dictionary and checks if the current co-ordinate is already in it.
        else:
            for j, k in track_obj.copy().items():
                obj_exist = False
                for i in current_co:
                    dist = k[0][1] - i[1]
                    if dist < 25 and dist > 0:
                        track_obj[j] = [i]
                        obj_exist = True
                        continue
                # If not, it will add it to the unique_obj array.
                if not obj_exist:
                    track_obj.pop(j)
                    unique_obj.append(k)

        prev_co = current_co.copy()
        cv2.imshow('PIU', img)
        if cv2.waitKey(1) == 27:
            break
    else:
        break

capture.release()
cv2.destroyAllWindows()

# print(unique_obj)


# Show the arrow sequence in an array
new_arr = []
for i in unique_obj:
    if i[0][0] > 20 < 60:
        new_arr.append("LB")
    if i[0][0] > 70 < 110:
        new_arr.append("LR")
    if i[0][0] > 120 < 170:
        new_arr.append("C")
    if i[0][0] > 175 < 220:
        new_arr.append("RR")
    if i[0][0] > 230 < 270:
        new_arr.append("RB")

print(new_arr)



