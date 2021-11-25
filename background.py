# import cv2
# import numpy as np
#
# capture = cv2.VideoCapture('S10_Switronic_Short_Cut.mp4')
# # capture = cv2.VideoCapture('S10_Switronic_Short_Cut_Test.mp4')
# ret, frame1 = capture.read()
# ret, frame2 = capture.read()
#
#
#
#
# while True:
#     ret, frame1 = capture.read()
#
#     cv2.imshow('PIU', frame1)
#
#     if cv2.waitKey(0) == 27:
#         break
#
# capture.release()
# cv2.destroyAllWindows()

import cv2 as cv
import argparse

parser = argparse.ArgumentParser(description='This program shows how to use background subtraction methods provided by \
                                              OpenCV. You can process both videos and images.')
parser.add_argument('--input', type=str, help='Path to a video or a sequence of image.', default='vtest.avi')
parser.add_argument('--algo', type=str, help='Background subtraction method (KNN, MOG2).', default='MOG2')
args = parser.parse_args()
if args.algo == 'MOG2':
    backSub = cv.createBackgroundSubtractorMOG2()
else:
    backSub = cv.createBackgroundSubtractorKNN()
capture = cv.VideoCapture('S10_Switronic_Short_Cut.mp4')
if not capture.isOpened():
    print('Unable to open: ' + args.input)
    exit(0)
while True:
    ret, frame = capture.read()
    if frame is None:
        break

    fgMask = backSub.apply(frame)

    cv.rectangle(frame, (10, 2), (100, 20), (255, 255, 255), -1)
    cv.putText(frame, str(capture.get(cv.CAP_PROP_POS_FRAMES)), (15, 15),
               cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0))

    cv.imshow('Frame', frame)
    cv.imshow('FG Mask', fgMask)

    keyboard = cv.waitKey(30)
    if keyboard == 'q' or keyboard == 27:
        break




