import numpy as np
import cv2
import glob
import os

#待处理图片文件夹
img_folder = r"F:\zs\DeepFaceLabCUDA-0219-final\workspace\aligned-lj-512"
#处理后保存的文件夹
result_folder =r"F:\zs\DeepFaceLabCUDA-0219-final\workspace\aligned-lj-512\result" 

def hisEqulColor(img):
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    h,s,v = cv2.split(hsv)
    clahe = cv2.createCLAHE(clipLimit=1.0, tileGridSize=(2,2))

    # h = clahe.apply(h)
    s = clahe.apply(s)
    v = clahe.apply(v)
    
    hsv = cv2.merge((h,s,v))
    img = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
    return img


if not os.path.exists(result_folder):
    os.makedirs(result_folder)

for name in glob.glob(f'{img_folder}/*.*[g]'):
    print(f"正在处理{name}")
    
    img = cv2.imread(name)
    eq = hisEqulColor(img)

    basename = os.path.basename(name)
    cv2.imwrite(f'{result_folder}/hist_eq_{basename}',eq)
