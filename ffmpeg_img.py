#encoding = utf-8
import subprocess
import os


root_dir = r"D:\seagate2\DEEPFAKES\备选\other\test"
pic_out_dir = root_dir + "/" +"frames"
rate = 0.2 #裁剪帧率
frame_format = "jpg" #jpg体积小,png速度快

if not os.path.isdir(pic_out_dir):
    os.makedirs(pic_out_dir)

file_list = []

def getfile(root_dir):
    if os.path.isdir(root_dir):
        for _, _, files in os.walk(root_dir):
            for file in files:
                if str(file).lower().endswith('.mp4') \
                or str(file).lower().endswith('.avi') \
                or str(file).lower().endswith('.mkv') \
                or str(file).lower().endswith('.flv'):
                    #获取文件名,不含后缀
                    shortname, _ = os.path.splitext(file)
                    video_path = os.path.join(root_dir, file)
                    print(file)               
                    subprocess.call(["ffmpeg", '-i', video_path, "-r", "0.2", "-f", "image2", pic_out_dir+'/'+shortname+'-%05d.'+frame_format])
                    print("处理{}完成".format(file))
                    file_list.append(file)

        print("共处理了{}个视频".format(str(len(file_list))))
    else:
        print("路径不对,请确认路径的是不是写错了")


if __name__ == "__main__":
    getfile(root_dir)
