import datetime
import cv2
import os
 

current_date_time = datetime.datetime.now().replace(second = 0,microsecond = 0)
v_current_date_time = current_date_time.strftime("%Y_%d_%m_%H_%M")
v_name =str(v_current_date_time)

v_file = open (f'/Users/borisprudnikov/Desktop/ШП/{v_name}.avi','w')
v_file.close()

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
    if cv2.waitKey(1)== ord('2'):
        os.system('bash scr.sh')
    if cv2.waitKey(1)==ord('q'):
        break
    
    if ret == True:
           # Write the frame to the output files
           output.write(frame1)
           
    
    else:
         print("Stream disconnected")
         break
    

output.release()
cap.release()
cv2.destroyAllWindows()
