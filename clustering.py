import cv2

# img = cv2.imread('./frame.png')

# img1 = img[:893, :957, :]
# img2 = img[:893, 963:, :]

# img1, img2 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY), cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

# diff = cv2.absdiff(img1, img2)

# t = 8
# diff = diff[t:-t, t:-t]

# diff = cv2.resize(diff, (diff.shape[1]//2, diff.shape[0]//2))

# print(diff > 50)

# diff[diff < 50] = 0
# diff[diff >= 50] = 255



# cv2.imshow('asdf',cv2.cvtColor(diff, cv2.COLOR_GRAY2BGR))
# cv2.waitKey()
# cv2.destroyAllWindows()

import cv2
import numpy as np
# img = cv2.imread('./frame.png')

# img1 = img[:893, :957, :]
# img2 = img[:893, 963:, :]

# img1, img2 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY), cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

# diff = cv2.absdiff(img1, img2)

# t = 8
# diff = diff[t:-t, t:-t]

# diff = cv2.resize(diff, (diff.shape[1]//2, diff.shape[0]//2))

# print(diff > 50)

# diff[diff < 50] = 0
# diff[diff >= 50] = 255



# cv2.imshow('asdf',cv2.cvtColor(diff, cv2.COLOR_GRAY2BGR))
# cv2.waitKey()
# cv2.destroyAllWindows()

# import cv2
# import numpy as np

# gray = diff
# im = cv2.cvtColor(diff, cv2.COLOR_GRAY2BGR)
# # distance-transform
# dist = cv2.distanceTransform(~gray, cv2.DIST_L1, 3)
# # max distance
# k = 10
# bw = np.uint8(dist < k)
# # remove extra padding created by distance-transform
# kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (k, k))
# bw2 = cv2.morphologyEx(bw, cv2.MORPH_ERODE, kernel)
# # clusters
# contours, _ = cv2.findContours(bw2, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
# # draw clusters and bounding-boxes
# i = 0
# print(len(contours))
# for cnt in contours:
#     x, y, w, h = cv2.boundingRect(cnt)
#     cv2.rectangle(im, (x, y), (x+w, y+h), (0, 255, 0), 2)
#     cv2.drawContours(im, contours, i, (255, 0, 0), 2)
#     i += 1

# cv2.imshow('asdf',im)
# cv2.waitKey()
# cv2.destroyAllWindows()

def get_cluster_centers(img):
    
    img1 = img[:893, :957, :]
    img2 = img[:893, 963:, :]

    img1, img2 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY), cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

    diff = cv2.absdiff(img1, img2)

    t = 8
    diff = diff[t:-t, t:-t]

    diff = cv2.resize(diff, (diff.shape[1]//2, diff.shape[0]//2))

    diff[diff < 50] = 0
    diff[diff >= 50] = 255

    gray = diff
    im = cv2.cvtColor(diff, cv2.COLOR_GRAY2BGR)
    # distance-transform
    dist = cv2.distanceTransform(~gray, cv2.DIST_L1, 3)
    # max distance
    k = 10
    bw = np.uint8(dist < k)
    # remove extra padding created by distance-transform
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (k, k))
    bw2 = cv2.morphologyEx(bw, cv2.MORPH_ERODE, kernel)
    # clusters
    contours, _ = cv2.findContours(bw2, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    # draw clusters and bounding-boxes
    i = 0
    print(len(contours))
    
    for cnt in contours:
        x, y, w, h = cv2.boundingRect(cnt)
        cv2.rectangle(im, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cv2.drawContours(im, contours, i, (255, 0, 0), 2)
        i += 1

        yield (x + w // 2 + t, y + h // 2 + t)