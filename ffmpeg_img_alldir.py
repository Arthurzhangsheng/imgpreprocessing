#encoding = utf-8
import subprocess
import os


root_dir = r"D:\seagate2\DEEPFAKES\test"
pic_out_dir = root_dir + "/" +"frames"
rate = 0.2 #裁剪帧率
frame_format = "jpg" #jpg体积小,png速度快

if not os.path.isdir(pic_out_dir):
    os.makedirs(pic_out_dir)

format_list = [".mp4", ".avi", ".mkv", ".flv"]
file_list = []

def getfile(root_dir):
    if os.path.isdir(root_dir):
        for fpathe, dirs, files in os.walk(root_dir):
            for _file in files:
                #判断是否为视频格式文件
                if os.path.splitext(_file)[-1].lower() in format_list:
                    #获取文件名,不含后缀
                    shortname = os.path.splitext(_file)[0]
                    #创建当前视频的带路径文件名
                    video_path = os.path.join(fpathe, _file)
                    print(_file)               
                    subprocess.call(["ffmpeg", '-i', video_path, "-r", str(rate), "-f", "image2", pic_out_dir+'/'+shortname+'-%05d.'+frame_format])
                    print("处理{}完成".format(_file))
                    file_list.append(_file)

        print("共处理了{}个视频".format(str(len(file_list))))

    else:
        print("路径不对,请确认路径的是不是写错了")


if __name__ == "__main__":
    getfile(root_dir)
