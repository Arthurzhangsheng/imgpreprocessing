#coding = utf-8
import os
import cv2
'''
本程序用于筛选出适合训练的全身服装模特图片,所用图片已预先去背景处理
但混杂了许多不符合要求的图片,如特写/半身/背面,需要筛选出来
筛选思路如下:
1.检测图片是否有且只有1张人脸,是的话进入第二步
2.计算人脸和全图的比例,用于分离半身照和全身照等
3.将比例数值写到文件名开头,保存文件(这样可按文件名排序来挑选所需图片)

'''

read_dir = 'C:/Users/Administrator/Desktop/fashion_deisgn/82_items_(04-28-18)/nobackground' #待挑选图片文件夹路径
save_dir = 'C:/Users/Administrator/Desktop/fashion_deisgn/82_items_(04-28-18)/nobackground/select' #筛选出来的图片保存路径
xmlfile_dir = 'C:/Anaconda3/pkgs/opencv3-3.1.0-py35_0/Library/etc/haarcascades/haarcascade_frontalface_default.xml'
#这是opencv人脸检测模块的所在位置
if not os.path.exists(save_dir):  #判断保存路径是否存在，不存在则创建一个
    os.makedirs(save_dir)


def detectFaces(read_dir,image_name):#检测图中所有人脸，返回包含所有人脸大小与全图的比例的列表
    image_dir_name = os.path.join(read_dir, image_name)
    img = cv2.imread(image_dir_name)
    face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")#载入人脸检测配置文件
    face_cascade.load(xmlfile_dir)
    if img.ndim == 3:#if语句：如果img维度为3，说明不是灰度图，先转化为灰度图gray，如果不为3，也就是2，原图就是灰度图
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    else:
        gray = img 

    faces = face_cascade.detectMultiScale(gray, 1.2, 5)#1.2是检测窗口每次的放大倍数，3是表示构成检测目标的相邻矩形的最小个数
    detect_result = []
    img_height = img.shape[1]
    for (_,_,_,face_height) in faces:
        ratio = face_height / img_height
        detect_result.append((ratio)) #x,y是左上角坐标，w,h是宽和高
    return detect_result

def judge_save(read_dir, image_name):#判断图片是否有且只有一张人脸，若符合，则计算脸部比例,重命名保存图片到save_dir指定路径中
    image_dir_name = os.path.join(read_dir, image_name)#图片的带路径的名字，类似test/test.jpg
    detect_result = detectFaces(read_dir,image_name)
    if len(detect_result) == 1:
        img = cv2.imread(image_dir_name)
        ratio = '%.2f' % detect_result[0] #把比例数字转成两位小数点的字符串
        img_save_dir_name = os.path.join(save_dir, ratio +'_select_'+ image_name) #生成select/0.36_select_test.jpg
        cv2.imwrite(img_save_dir_name, img) #保存图片到save_dir指定路径中
   
def main():#遍历指定文件夹所有图片，并做判断与保存
    all_imgs = os.listdir(read_dir)
    for imgname in all_imgs:
        print(imgname)
        image_dir_name = os.path.join(read_dir, imgname)#图片的带路径的名字，类似test/test.jpg
        img = cv2.imread(image_dir_name)
        if img is None:#这步排除一些特殊外语字母命名的图片导致未读到图片内容
            continue
        judge_save(read_dir, imgname)

if __name__ == '__main__':
    main()