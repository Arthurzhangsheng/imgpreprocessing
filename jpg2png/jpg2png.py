import numpy as np
import cv2
import glob
import os
from tqdm import tqdm
'''
批量把JPG图转化格式为PNG，同时可以进行裁剪工作
'''

#待处理图片文件夹
jpg_folder = r"F:\zs\DeepFaceLabCUDA-0219-final\workspace\AV\guchuanyizhi\1024aligned"
#处理后保存的文件夹
png_folder =r"F:\zs\DeepFaceLabCUDA-0219-final\workspace\AV\guchuanyizhi\512png" 
#是否裁剪
RESIZE = True
#缩小后的尺寸
target_size = (512,512)
#缩放的插值方式
interpolation = cv2.INTER_AREA #如果要缩小图像，通常推荐使用#INTER_AREA插值效果最好，而要放大图像，通常使用INTER_CUBIC(速度较慢，但效果最好)，或者使用INTER_LINEAR(速度较快，效果还可以)。

#自动创建保存文件夹
if not os.path.exists(png_folder):
    os.makedirs(png_folder)

for name in tqdm(glob.glob(f'{jpg_folder}/*.jpg'), ncols=10):  
    img = cv2.imread(name)
    if RESIZE:
        img = cv2.resize(img, target_size, interpolation= interpolation)
    basename = os.path.basename(name).split(".")[0]#获取带后缀的基本文件名后，分割字符串，得到无后缀名字
    
    cv2.imwrite(f'{png_folder}/{basename}.png',img)

