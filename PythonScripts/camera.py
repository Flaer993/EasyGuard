import datetime

import cv2
 
current_date_time = datetime.datetime.now().replace(second = 0,microsecond = 0)
v_current_date_time = current_date_time.strftime("%Y_%d_%m_%H_%M")
print(v_current_date_time)
v_name =str(v_current_date_time)
print(v_name)
v_file = open (f'/Users/borisprudnikov/Desktop/ШП/{v_name}.avi','w')
v_file.close()
key_start_control='m'
cap = cv2.VideoCapture(0)
 
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))
frame_size = (frame_width,frame_height)
fps = 30
output = cv2.VideoWriter(f'/Users/borisprudnikov/Desktop/ШП/{v_name}.avi', cv2.VideoWriter_fourcc('M','J','P','G'), 30, frame_size)
ret, frame1 = cap.read()
ret, frame2 = cap.read()
while(cap.isOpened()):
    # vid_capture.read() methods returns a tuple, first element is a bool
    # and the second is frame
    ret, frame = cap.read()
    cv2.imshow('camera1', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    if ret == True:
           # Write the frame to the output files
           output.write(frame1)
           
           difference = cv2.absdiff(frame1, frame2)
           gray = cv2.cvtColor(difference, cv2.COLOR_BGR2GRAY)
           blur = cv2.GaussianBlur(gray, (5,5), 0)
           _, threshold = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
           dilate = cv2.dilate(threshold, None, iterations=3)
           contour, _ = cv2.findContours(dilate, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
           cv2.drawContours(frame1, contour, -2, (0, 255, 0), 2)
           cv2.imshow("image", frame1)
           frame1 = frame2
           ret, frame2 = cap.read()
    
    else:
         print("Stream disconnected")
         break
    
    
 
 
 
output.release()
cap.release()
cv2.destroyAllWindows()
