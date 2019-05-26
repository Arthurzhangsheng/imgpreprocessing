import numpy as np
import cv2
import os
'''
本程序将图片转化到HSV色彩空间进行直方图匹配，
因任务需求，只对色相H和饱和度S做了直方图匹配，明度V未变化，
若需要都做变化，或直接对BGR色彩空间做直方图匹配，需要修改部分代码
'''


def channel_hist_match(source, template, hist_match_threshold=255, mask=None):
    # Code borrowed from:
    # https://stackoverflow.com/questions/32655686/histogram-matching-of-two-images-in-python-2-x
    masked_source = source
    masked_template = template

    if mask is not None:
        masked_source = source * mask
        masked_template = template * mask

    oldshape = source.shape
    source = source.ravel()
    template = template.ravel()
    masked_source = masked_source.ravel()
    masked_template = masked_template.ravel()
    s_values, bin_idx, s_counts = np.unique(source, return_inverse=True,
                                            return_counts=True)
    t_values, t_counts = np.unique(template, return_counts=True)
    ms_values, mbin_idx, ms_counts = np.unique(source, return_inverse=True,
                                            return_counts=True)
    mt_values, mt_counts = np.unique(template, return_counts=True)

    s_quantiles = np.cumsum(s_counts).astype(np.float64)
    s_quantiles = hist_match_threshold * s_quantiles / s_quantiles[-1]
    t_quantiles = np.cumsum(t_counts).astype(np.float64)
    t_quantiles = 255 * t_quantiles / t_quantiles[-1]
    interp_t_values = np.interp(s_quantiles, t_quantiles, t_values)

    return interp_t_values[bin_idx].reshape(oldshape)    

def color_hist_match(src_im, tar_im, hist_match_threshold=255, mask=None):
    h,w,c = src_im.shape
    src_im = cv2.cvtColor(src_im,cv2.COLOR_RGB2HSV)
    tar_im = cv2.cvtColor(tar_im,cv2.COLOR_RGB2HSV)
    
    #只对色相H和饱和度S做了匹配，亮度保持不变
    matched_H = channel_hist_match(src_im[:,:,0], tar_im[:,:,0], hist_match_threshold, mask)
    matched_S = channel_hist_match(src_im[:,:,1], tar_im[:,:,1], hist_match_threshold, mask)
    # matched_V = channel_hist_match(src_im[:,:,2], tar_im[:,:,2], hist_match_threshold, mask)
    
    to_stack = (matched_H, matched_S, src_im[:,:,2])
    for i in range(3, c):
        to_stack += ( src_im[:,:,i],)
    
    
    matched_hsv = np.stack(to_stack, axis=-1).astype(src_im.dtype)
    matched_img_rgb = cv2.cvtColor(matched_hsv,cv2.COLOR_HSV2RGB)
    return matched_img_rgb



if __name__ == "__main__":
    #待处理图片
    img1_path = r"img/lj.jpg"
    img2_path = r"img/gyx.png"

    #处理后保存的文件夹
    result_folder =r"result" 

    if not os.path.exists(result_folder):
        os.makedirs(result_folder)
        
    img1_bgr = cv2.imread(img1_path)
    img2_bgr = cv2.imread(img2_path)


    img1_rgb = cv2.cvtColor(img1_bgr,cv2.COLOR_BGR2RGB)
    img2_rgb = cv2.cvtColor(img2_bgr,cv2.COLOR_BGR2RGB)

    matched_rgb = color_hist_match(img1_rgb, img2_rgb, hist_match_threshold=255)
    matched_bgr = cv2.cvtColor(matched_rgb,cv2.COLOR_RGB2BGR)
    

    cv2.imwrite(f'{result_folder}/result.jpg', matched_bgr)
