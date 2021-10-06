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
        if cv2.waitKey(1) & 0xFF==ord('g') or flag==5:
            while (True):
                ret_g, frame_g = cap.read()
                if ret_g==True:
                    frame_g = cv2.cvtColor(frame_g,cv2.COLOR_BGR2GRAY)
                    cv2.imshow("Video",frame_g)
                    out.write(frame_g)

                    if cv2.waitKey(1) & 0xFF==27:## exit
                        flag=1
                        break
                    elif cv2.waitKey(1) & 0xFF==ord('r'): ## reset
                        flag=2
                        break
                    elif cv2.waitKey(1) & 0xFF==ord('u'): ## uv
                        flag=3
                        break
                    elif cv2.waitKey(1) & 0xFF==ord('x'):## xyz
                        flag=4
                        break
                else:
                    break
        if flag==1:
            break
        elif cv2.waitKey(1) & 0xFF or flag==2:
            continue
        elif cv2.waitKey(1) & 0xFF==ord('u') or flag==3:
            ## UV color
            while (True):
                ret_u, frame_u = cap.read()
                if ret_u==True:
                    frame_u = cv2.cvtColor(frame_u,cv2.COLOR_BGR2YUV)
                    cv2.imshow("Video",frame_u)
                    out.write(frame_u)

                    if cv2.waitKey(1) & 0xFF==27:## exit
                        flag=1
                        break
                    elif cv2.waitKey(1) & 0xFF==ord('r'): ## reset
                        flag=2
                        break
                    elif cv2.waitKey(1) & 0xFF==ord('g'): ## gray
                        flag=5
                        break
                    elif cv2.waitKey(1) & 0xFF==ord('x'):## xyz
                        flag=4
                        break
                else:
                    break
        elif cv2.waitKey(1) & 0xFF==ord('x') or flag==4:
            ##XYZ
            while (True):
                ret_u, frame_u = cap.read()
                if ret_u==True:
                    frame_u = cv2.cvtColor(frame_u,cv2.COLOR_BGR2YUV)
                    cv2.imshow("Video",frame_u)
                    out.write(frame_u)

                    if cv2.waitKey(1) & 0xFF==27:## exit
                        flag=1
                        break
                    elif cv2.waitKey(1) & 0xFF==ord('r'): ## reset
                        flag=2
                        break
                    elif cv2.waitKey(1) & 0xFF==ord('g'): ## gray
                        flag=5
                        break
                    elif cv2.waitKey(1) & 0xFF==ord('u'):## xyz
                        flag=3
                        break
                else:
                    break
            
    else:
        break

cap.release()
out.release()
cv2.destroyAllWindows()


