import cv2
import make_dir

cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'MP4V')
out = cv2.VideoWriter(f"./{make_dir.save_dir}/output.mp4",fourcc,40.0,(640,480))
flag=0
while (cap.isOpened()):
    ret, frame = cap.read()
    frame_g=frame_u=frame_x=frame_d = frame
    if ret== True:
        cv2.imshow("Video",frame)
        out.write(frame)
        
        if cv2.waitKey(1) & 0xFF==27:
            break
        if cv2.waitKey(1) & 0xFF==ord('g'):
            while (True):
                ret_g, frame_g = cap.read()
                if ret_g==True:
                    frame_g = cv2.cvtColor(frame_g,cv2.COLOR_BGR2GRAY)
                    cv2.imshow("Video",frame_g)
                    out.write(frame_g)

                    if cv2.waitKey(1) & 0xFF==27:
                        flag=1
                        break
                    elif cv2.waitKey(1) & 0xFF==ord('r'):
                        break
                else:
                    break
        if flag==1:
            break
    else:
        break

cap.release()
out.release()
cv2.destroyAllWindows()


