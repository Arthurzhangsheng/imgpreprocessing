import os
import cv2

read_dir = 'E:/GAN/facedetect/test'
save_dir = 'select' #筛选出来的图片保存路径

if not os.path.exists(save_dir):  #判断保存路径是否存在，不存在则创建一个
    os.makedirs(save_dir)


def detectFaces(read_dir,image_name):#检测图中所有人脸，返回包含所有人脸大小与全图的比例的列表
    image_dir_name = os.path.join(read_dir, image_name)
    img = cv2.imread(image_dir_name)
    face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")#载入人脸检测配置文件
    face_cascade.load('E:/Anaconda3/pkgs/opencv-3.3.1-py36h20b85fd_1/Library/etc/haarcascades/haarcascade_frontalface_default.xml')
    if img.ndim == 3:#if语句：如果img维度为3，说明不是灰度图，先转化为灰度图gray，如果不为3，也就是2，原图就是灰度图
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    else:
        gray = img 

    faces = face_cascade.detectMultiScale(gray, 1.2, 3)#1.2是检测窗口每次的放大倍数，3是表示构成检测目标的相邻矩形的最小个数
    detect_result = []
    img_height = img.shape[1]
    for (_,_,_,face_height) in faces:
        ratio = face_height / img_height
        detect_result.append((ratio)) #x,y是左上角坐标，w,h是宽和高
    return detect_result

def judge_save(read_dir, image_name):#判断图片是否是合格图片，若合格，则重命名保存图片到save_dir指定路径中
    image_dir_name = os.path.join(read_dir, image_name)#图片的带路径的名字，类似test/test.jpg
    detect_result = detectFaces(read_dir,image_name)
    if len(detect_result) == 1:
        img = cv2.imread(image_dir_name)
        ratio = '%.2f' % detect_result[0] #把比例数字转成两位小数点的字符串
        img_save_dir_name = os.path.join(save_dir, ratio +'_select_'+ image_name) #生成select/0.36_select_test.jpg
        cv2.imwrite(img_save_dir_name, img) #保存图片到save_dir指定路径中
   
def main():#遍历指定文件夹所有图片，并做判断与分类保存
    all_imgs = os.listdir(read_dir)
    print(all_imgs)
    for img in all_imgs:
        judge_save(read_dir, img)

if __name__ == '__main__':
    main()
