# imgpreprocessing
resize img with padding into 256*256 jpg
# requirement
* cv2
* jupyter notebook
* python 3.5

# usage method of resize img into 256*256(image preprocessing.ipynb)

first, rename all the img

then modify the following code in `image preprocessing.ipynb`

```
#需要改写的部分
read_dir = 'H:\\render\\'  #图片读取路径
save_dir = 'H:\\sketch2render\\render_resized\\' #图片储存路径
```
# usage method of select model img(filter.py)

First, find the 'haarcascade_frontalface_default.xml' in your opencv folder.
then modify the following code in 'filter.py'

```
read_dir = 'C:/Users/Administrator/Desktop/fashion_deisgn/82_items_(04-28-18)/nobackground' #待挑选图片文件夹路径
save_dir = 'C:/Users/Administrator/Desktop/fashion_deisgn/82_items_(04-28-18)/nobackground/select' #筛选出来的图片保存路径
xmlfile_dir = 'C:/Anaconda3/pkgs/opencv3-3.1.0-py35_0/Library/etc/haarcascades/haarcascade_frontalface_default.xml'
```

# usage method of extra edge from model images(model_outline_extract.py)

# usage method of center_crop_resize.py)
功能:批量把图裁剪成正方形(以宽和高中较小的为准),然后resize到256x256  
方法:修改`read_dir`和`save_dir`的路径,然后运行

# pngread.py
功能：往png图中插入与读取隐藏文本信息
方法：修改`src_png`和`dst_png`的路径，然后运行
