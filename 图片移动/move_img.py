import glob
import shutil,os
from tqdm import tqdm
'''
批量把JPG图转化格式为PNG，同时可以进行裁剪工作
'''

#待处理图片文件夹
jpg_folder = r"H:\零零发素材\MN\001-050\017"
#处理后保存的文件夹
gather_folder =r"H:\零零发素材\MN\001-050\017图片集合" 

#自动创建保存文件夹
if not os.path.exists(gather_folder):
    os.makedirs(gather_folder)

i = 0
for name in tqdm(glob.glob(f'{jpg_folder}/**/*.??[gG]', recursive=True), ncols=10):  

    shutil.move(name,f"{gather_folder}/{i:05d}.jpg")
    i += 1

