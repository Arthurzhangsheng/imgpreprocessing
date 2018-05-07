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
#需要改写的部分,需要事先规范化重命名输入图片的名称
read_dir = 'H:\\render\\'  #图片读取路径
save_dir = 'H:\\sketch2render\\render_resized\\' #图片储存路径
total_image_number = 15898 #图片总数
img_name_format = 'render (%d).jpg' #命名格式
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
