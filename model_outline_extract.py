#coding=utf-8
import cv2
import os

#读取/储存目录
read_dir = r'C:\Users\Administrator\Desktop\fashion_deisgn\82_items_(04-28-18)\nobackground\select\0.11_0.16' #原图所在文件夹
save_dir1 = r'C:\Users\Administrator\Desktop\fashion_deisgn\82_items_(04-28-18)\nobackground\select\0.11_0.16/low' #每张图采取低,中,高三个阈值来提取保存3份复杂程度从低到高的线稿
save_dir2 = r'C:\Users\Administrator\Desktop\fashion_deisgn\82_items_(04-28-18)\nobackground\select\0.11_0.16/medium'
save_dir3 = r'C:\Users\Administrator\Desktop\fashion_deisgn\82_items_(04-28-18)\nobackground\select\0.11_0.16/high'
if not os.path.exists(save_dir1):
    os.makedirs(save_dir1)
if not os.path.exists(save_dir2):
    os.makedirs(save_dir2)
if not os.path.exists(save_dir3):
    os.makedirs(save_dir3)
#算法相关参数
lowThreshold_low = 10 #提取线稿的阈值
lowThreshold_medium = 23 
lowThreshold_high = 60 
GBsize = 19 #Gaussian blur size高斯模糊的大小

def edge_produce(img, save_dir, imgname, lowThreshold):#输入图片,生成保存线稿
    #先对三通道分别检验边缘,再合并,以检测出色相差异的边缘
    grayB = img[:,:,0]
    grayG = img[:,:,1]
    grayR = img[:,:,2]
    #用高斯模糊, 过滤掉小细节
    blurB = cv2.GaussianBlur(grayB,(GBsize,GBsize),0)
    blurG = cv2.GaussianBlur(grayG,(GBsize,GBsize),0)
    blurR = cv2.GaussianBlur(grayR,(GBsize,GBsize),0)
    #调用opencv自带的canny算法
    highThreshold = lowThreshold * 2 #canny算子的阈值上限
    detected_edges_B = cv2.Canny(blurB, lowThreshold, highThreshold, apertureSize = 3)
    detected_edges_G = cv2.Canny(blurG, lowThreshold, highThreshold, apertureSize = 3)
    detected_edges_R = cv2.Canny(blurR, lowThreshold, highThreshold, apertureSize = 3)
    #默认生成的是黑底白线的线稿,我先把3张线稿融合到一块
    edge = cv2.bitwise_or(detected_edges_B, detected_edges_G)
    edge = cv2.bitwise_or(edge, detected_edges_R)
    #黑白反转,使背景为白色,线稿为黑色
    edge = 255 - edge
    edge_dir_name = os.path.join(save_dir, imgname)
    cv2.imwrite(edge_dir_name, edge)
    
def main():#批量处理
    all_imgs = os.listdir(read_dir)
    for imgname in all_imgs:
        print(imgname)
        #读取图片
        img_dir_name = os.path.join(read_dir, imgname)
        img = cv2.imread(img_dir_name)
        if img is None:#排除一些异常情况导致未读取到图片
            continue
        edge_produce(img=img, save_dir=save_dir1, imgname=imgname, lowThreshold=lowThreshold_low)
        edge_produce(img=img, save_dir=save_dir2, imgname=imgname, lowThreshold=lowThreshold_medium)
        edge_produce(img=img, save_dir=save_dir3, imgname=imgname, lowThreshold=lowThreshold_high)

if __name__ == '__main__':
    main()
