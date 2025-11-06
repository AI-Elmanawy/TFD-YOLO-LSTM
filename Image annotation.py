# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 06:58:10 2024
@author: Ahmed
"""

import cv2
import os
K=0
path_img=r"E:\postharvest prj\tomato_prj\Data\images\T3-25" ## your images path
Img_File=[]
for File in os.listdir(path_img):
    if File.endswith('.jpg'):
        Name, ext = os.path.splitext(File)
        Img_File.append(Name)
print(len(Img_File)-1)
#%%
name=Img_File[K]
print(name)
class DrawLineWidget(object):
    def __init__(self):
        self.original_image =cv2.imread(path_img+'/'+name+'.jpg', 1)
        self.clone = self.original_image.copy()
        cv2.namedWindow("image")
        cv2.setMouseCallback("image", self.extract_coordinates)
        # List to store start/end points
        self.image_coordinates = []
        self.N=0
        self.classes=0
        self.color=[(0,255,0), (0,0,255), (0,255,255)]
        self.f=open(path_img+'/'+name+'.txt', 'a')
        file_read=open(path_img+'/'+name+'.txt', 'r').read()
        if file_read[-1]!='\n':
            self.f.write('\n')
    def extract_coordinates(self, event, x, y, flags, parameters):
        # Record starting (x,y) coordinates on left mouse button click
        if event == cv2.EVENT_LBUTTONDOWN:
            self.image_coordinates = [(x,y)]
        # Record ending (x,y) coordintes on left mouse bottom release
        elif event == cv2.EVENT_LBUTTONUP:
            self.image_coordinates.append((x,y))
            # print('Starting: {}, Ending: {}'.format(self.image_coordinates[0], self.image_coordinates[1]))
            H,W, _=self.original_image.shape 
            # print(H,W)
            l, t=self.image_coordinates[0]
            r, b=self.image_coordinates[1]
            h=(b-t)/H
            w=(r-l)/W
            x=(l+(r-l)/2)/W
            y=(t+(b-t)/2)/H
            A=str(self.classes), str(x), str(y), str(w), str(h)
            A=" ".join(A)
            self.f.write(A)
            self.f.write('\n')
            print(A)
            # print(self.classes, x, y, w, h)
            XX=int(x*W)
            YY=int(y*H)
            self.N+=1
            cv2.putText(self.clone,str(self.N), (XX,YY), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255, 0), 2, 2) 
            # Draw line
            # cv2.line(self.clone, self.image_coordinates[0], self.image_coordinates[1], (36,255,12), 2)
            cv2.rectangle(self.clone, (l, t), (r, b),self.color[self.classes], 2)
            cv2.imshow("image", self.clone) 
        # Clear drawing boxes on right mouse button click
        elif event == cv2.EVENT_RBUTTONDOWN:
            # self.clone = self.original_image.copy()
            self.classes+=1
            if self.classes>2:
                self.classes=0
            # self.N=0
        elif event==cv2.EVENT_MOUSEWHEEL:
            H,W, _=self.original_image.shape
            if flags>0:
                H2=H+50
                W2=W+50
            else:
                H2=H-50
                W2=W-50
            self.original_image=cv2.resize(self.original_image, (H2, W2))
            self.clone = self.original_image
            
    def show_image(self):
        return self.clone
    def save_file(self):
        return self.f.close()
if __name__ == '__main__':
    draw_line_widget = DrawLineWidget()
    while True:
        cv2.imshow('image', draw_line_widget.show_image())
        key = cv2.waitKey(1)
        # Close program with keyboard 'q'
        if cv2.waitKey(5) & 0xff == ord("q") or cv2.waitKey(5) & 0xff == ord("Q"):
            # cv2.imwrite(path_img+'/'+name+'_'+str(K)+'_label.jpg', bin_img)
            cv2.destroyAllWindows()
            draw_line_widget.save_file()
            K+=1
            break
        if cv2.waitKey(5) & 0xff == ord("A") or cv2.waitKey(5) & 0xff == ord("a"):
            os.remove(path_img+'/'+name+'.jpg')
            draw_line_widget.save_file()
            cv2.destroyAllWindows()
            K+=1
            break