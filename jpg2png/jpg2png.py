import numpy as np
import cv2
import glob
import os
from tqdm import tqdm
'''
批量把JPG图转化格式为PNG，同时可以进行裁剪工作
'''

#待处理图片文件夹
img_folder = r"F:\zs\DeepFaceLabCUDA-0219-final\workspace\AV\benzhuangling\1024aligned"
#处理后保存的文件夹
result_folder =r"F:\zs\DeepFaceLabCUDA-0219-final\workspace\AV\benzhuangling\512png" 
#是否裁剪
RESIZE = True
#缩小后的尺寸
target_size = (512,512)
interpolation = cv2.INTER_AREA #缩小推荐用cv2.INTER_AREA

if not os.path.exists(result_folder):
    os.makedirs(result_folder)

for name in tqdm(glob.glob(f'{img_folder}/*.jpg'), ncols=10):  
    img = cv2.imread(name)
    if RESIZE:
        img = cv2.resize(img, target_size, interpolation= interpolation)
    basename = os.path.basename(name).split(".")[0]#获取带后缀的基本文件名后，分割字符串，得到无后缀名字
    
    cv2.imwrite(f'{result_folder}/{basename}.png',img)

