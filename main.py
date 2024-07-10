import cv2

img1, img2 = cv2.imread('./farm1.png'), cv2.imread('./farm2.png')

img1, img2 = img1[:691, :, :], img2[:, :930, :]

img1, img2 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY), cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

diff = cv2.absdiff(img1, img2)

cv2.imshow('asdf',cv2.cvtColor(diff, cv2.COLOR_GRAY2BGR))

cv2.waitKey()
cv2.destroyAllWindows()