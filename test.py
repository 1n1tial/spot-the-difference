import cv2

img = cv2.imread('./frame.png')

img1 = img[:893, :957, :]
img2 = img[:893, 963:, :]

img1, img2 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY), cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

diff = cv2.absdiff(img1, img2)

t = 8
diff = diff[t:-t, t:-t]

diff = cv2.resize(diff, (diff.shape[1]//2, diff.shape[0]//2))

print(diff > 50)

diff[diff < 50] = 0
diff[diff >= 50] = 255

cv2.imshow('asdf',cv2.cvtColor(diff, cv2.COLOR_GRAY2BGR))
cv2.waitKey()
cv2.destroyAllWindows()
 