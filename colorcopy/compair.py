import image2lut
import cv2


lut = 'C:/ProgramData/Blackmagic Design/DaVinci Resolve/Support/LUT/WIR Dolce LUT Collection/WIR Dolce 05.cube'
vid = "D:/videos/Family/Grandma's 90th/P1033192.MOV"

LUT = image2lut.lut_instance(lut)


cap = cv2.VideoCapture(vid)

if (cap.isOpened()== False):
  print("Error opening video stream or file")

while(cap.isOpened()):
  ret, frame = cap.read()
  if ret == True:
    h, w, _ = frame.shape
    frame = cv2.resize(frame, (int(w/2), int(h/2)))
    frame = image2lut.apply_lut(frame, LUT)
    cv2.imshow('Frame',frame)
    if cv2.waitKey(25) & 0xFF == ord('q'):
      break
  else:
    break

cap.release()
cv2.destroyAllWindows()