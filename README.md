# imgpreprocessing
resize img with padding
# requirement
* cv2
* jupyter notebook
* python 3.5

# usage method
first, rename all the img

then modify the following code in `image preprocessing.ipynb`

```
#需要改写的部分,需要事先规范化重命名输入图片的名称
read_dir = 'H:\\render\\'  #图片读取路径
save_dir = 'H:\\sketch2render\\render_resized\\' #图片储存路径
total_image_number = 15898 #图片总数
img_name_format = 'render (%d).jpg' #命名格式
```
