import cv2

cap = cv2.VideoCapture(0) # 0 showing avaibale device we can give video file name 
fourcc = cv2.VideoWriter_fourcc('X','V','I','D')
out = cv2.VideoWriter("video.mp4",fourcc,20.0,(640,480))
while(True):
    ret, frame = cap.read()
    if ret== True:
        cv2.imshow('frame',frame)
        out.write(frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
cap.release()
cv2.destroyAllWindows()