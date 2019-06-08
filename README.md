# imgpreprocessing
各种用过的图片处理python程序
# requirement
* opencv-python
* .ipynb结尾的需要用jupyter notebook打开
* python 3.6

### image preprocessing.ipynb
已废弃，原本是resize img into 256 x 256 ，现在批量裁剪用img_resize.ipynb

### usage method of select model img(filter.py)
功能：根据人脸数量来筛选图片
用法：
First, find the 'haarcascade_frontalface_default.xml' in your opencv folder.
then modify the following code in 'filter.py'

```
read_dir = 'C:/Users/Administrator/Desktop/fashion_deisgn/82_items_(04-28-18)/nobackground' #待挑选图片文件夹路径
save_dir = 'C:/Users/Administrator/Desktop/fashion_deisgn/82_items_(04-28-18)/nobackground/select' #筛选出来的图片保存路径
xmlfile_dir = 'C:/Anaconda3/pkgs/opencv3-3.1.0-py35_0/Library/etc/haarcascades/haarcascade_frontalface_default.xml'
```

### (model_outline_extract.py)
功能：提取图像边缘

### usage method of center_crop_resize.py)
功能:批量把图裁剪成正方形(以宽和高中较小的为准),然后resize到256x256  
方法:修改`read_dir`和`save_dir`的路径,然后运行

### pngread.py
功能：往png图中插入与读取隐藏文本信息  
方法：修改`src_png`和`dst_png`的路径，然后运行

### img_resize.ipynb
功能：批量缩放图片
方法：修改`read_path`和`save_path`，以及cv2.resize函数中的尺寸

### jpg2png.py
功能：批量把jpg转png，同时可以进行裁剪
方法：修改`jpg_folder`为jpg文件夹目录，修改`png_folder`为png保存目录。如还需要裁剪，设置`RESIZE`为`True`，并设置裁剪大小`target_size`和插值方法`interpolation`
