import cv2
import os
from tkinter import *
from tkinter import filedialog

root = Tk()
root.filename = filedialog.askopenfilename(initialdir = os.getcwd()+'/.before_img', title = "Select file")
root.withdraw()

print(root.filename)

font = cv2.FONT_HERSHEY_SIMPLEX
color_white = (255,255,255)

i = 1

def numbering(event, x, y, flags, param):
    global i
    if event == cv2.EVENT_LBUTTONDOWN:
        if i < 10:
            cv2.circle(img,(x,y),22,color_white,-1)
            cv2.circle(img,(x,y),20,(0,0,0),-1)
            cv2.putText(img,str(i),(x-10,y+10),font,1,color_white,2)
            print('%d, %d' %(x,y))
        elif i >= 10 and i < 100:
            cv2.circle(img,(x,y),22,color_white,-1)
            cv2.circle(img,(x,y),20,(0,0,0),-1)
            cv2.putText(img,str(i),(x-18,y+11),font,0.9,color_white,2)
            print('%d, %d' %(x,y))
        cv2.imshow('image', img)
        i += 1

img = cv2.imread(root.filename)

cv2.namedWindow('image')
cv2.setMouseCallback('image', numbering)
cv2.imshow('image', img)

n = 1
name = []

while(n):
    if cv2.getWindowImageRect('image') == (-1,-1,-1,-1):
        break
    if cv2.waitKey(0) & 0xFF == 27:
        break

for num in range(i-1):
    name.append(int(num)+1)

cv2.imwrite(os.getcwd() + '/.after_img/' + '@'+str(name).replace('[','').replace(']','').replace(' ','')+'.png', img)
cv2.destroyAllWindows()
