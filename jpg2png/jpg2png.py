import numpy as np
import cv2
import glob
import os

#待处理图片文件夹
img_folder = r"./jpg"
#处理后保存的文件夹
result_folder =r"./png" 


if not os.path.exists(result_folder):
    os.makedirs(result_folder)

for name in glob.glob(f'{img_folder}/*.jpg'):
    print(f"正在处理{name}")
    
    img = cv2.imread(name)
    target_size=(512,512)
    img = cv2.resize(img, target_size, interpolation=cv2.INTER_AREA)#缩小推荐用cv2.INTER_AREA
    basename = os.path.basename(name).split(".")[0]#获取带后缀的基本文件名后，分割字符串，得到无后缀名字
    
    cv2.imwrite(f'{result_folder}/{basename}.png',img)
