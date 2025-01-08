import cv2
img =cv2.imread("ab.jpg",1)
print(img)
cv2.imshow('image',img)  # show the image 
k= cv2.waitKey(0)

if k==27:
    cv2.destroyAllWindows()
elif k== ord('s'):
    cv2.imwrite('image.png',img)  # make new image 
    cv2.destroyAllWindows()


