import cv2 
import os

read_dir = r"C:\Users\Administrator\Desktop\buildingskin\Pinterest_amrahmedalii\Building Skin(680E)"
save_dir = r"C:\Users\Administrator\Desktop\buildingskin\Pinterest_amrahmedalii\test"

all_imgs = os.listdir(read_dir)
i = 1
for imgname in all_imgs:
    
    print(imgname)
    image_dir_name = os.path.join(read_dir, imgname)#图片的带路径的名字，类似test/test.jpg
    img = cv2.imread(image_dir_name)
    
    if img is None:#这步排除一些特殊外语字母命名的图片导致未读到图片内容
        continue
    
    h , w, c = img.shape
    if h >= w:#高大于宽
        roi = img[(h-w)//2:(h-w)//2+w , :]
        scaling_ratio = 256. / w
        img_resize = cv2.resize(roi,None,fx=scaling_ratio,fy=scaling_ratio, 
                                interpolation = cv2.INTER_AREA)#缩小图片用cv2.INTER_AREA,放大图片用 cv2.INTER_CUBIC (slow) & cv2.INTER_LINEAR
        cv2.imwrite(save_dir+'/%05d.jpg'%i,img_resize)
        
    else:
        roi = img[ : , (w-h)//2:(w-h)//2+h]
        scaling_ratio = 256. / h
        img_resize = cv2.resize(roi,None,fx=scaling_ratio,fy=scaling_ratio, 
                                interpolation = cv2.INTER_AREA)
        cv2.imwrite(save_dir+'/%05d.jpg'%i,img_resize)                        
        

    i += 1