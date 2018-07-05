
#coding:utf8
import os

def rename():
        i=0
        path=r"E:\GAN\maya\day5\WGAN-WGAN-GP_with_own_image\samples\buildingskin"
        for i in range(487):
            d = i+1
            olddir = path + '/' + "buildingskin ({})".format(d) + ".png"
            newdir = path + '/' + "buildingskin({})".format(d) + ".png"
            print(olddir)
            print(newdir)
            os.rename(olddir,newdir)#重命名
rename()