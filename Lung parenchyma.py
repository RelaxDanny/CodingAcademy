import os
import cv2 
import numpy as np
import pandas as pd
import skimage
from skimage import measure
from collections import Counter


def split_target_dir(target_dir,output_dir):
    target_list=[target_dir+os.sep+file for file in os.listdir(target_dir)]
    print(target_list)
    for target in target_list:
        img_split=split_lung_parenchyma(target,15599,-96)
        dst=target.replace(target_dir,output_dir)
        dst_dir=os.path.split(dst)[0]
        if not os.path.exists(dst_dir):
            os.makedirs(dst_dir)
        cv2.imencode('.jpg', img_split)[1].tofile(dst)
    print(f'Target list done with {len(target_list)} items')


def split_lung_parenchyma(target,size,thr):
    img=cv2.imdecode(np.fromfile(target,dtype=np.uint8),cv2.IMREAD_GRAYSCALE)
    try:
        img_thr= cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV,size,thr).astype(np.uint8)
    except:
        img_thr= cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV,999,thr).astype(np.uint8)
    img_thr=255-img_thr
    img_test=measure.label(img_thr, connectivity = 1)
    props = measure.regionprops(img_test)
    img_test.max()
    areas=[prop.area for prop in props]
    ind_max_area=np.argmax(areas)+1
    del_array = np.zeros(img_test.max()+1)
    del_array[ind_max_area]=1
    del_mask=del_array[img_test]
    img_new = img_thr*del_mask
    mask_fill=fill_water(img_new)
    img_new[mask_fill==1]=255
    img_new = 255-img_new
    _, labels, stats, centroids = cv2.connectedComponentsWithStats(img_new.astype( np.uint8 ))
    labels = np.array(labels, dtype=np.float)
    maxnum = Counter(labels.flatten()).most_common(3)
    maxnum = sorted([x[0] for x in maxnum])
    background = np.zeros_like(labels)
    if len(maxnum) == 1:
        pass
    elif len(maxnum) == 2:
        background[labels == maxnum[1]] = 1
    else:
        background[labels == maxnum[1]] = 1
        background[labels == maxnum[2]] = 1
    img_new[background == 0] = 0
    img_new=cv2.dilate(img_new, np.ones((5,5),np.uint8) , iterations=3)
    img_new = cv2.erode(img_new, np.ones((5, 5), np.uint8), iterations=2)
    img_new = cv2.morphologyEx(img_new, cv2.MORPH_CLOSE, cv2.getStructuringElement(cv2.MORPH_RECT, (10, 10)),iterations=2)
    img_new = cv2.medianBlur(img_new.astype(np.uint8), 21)
    img_out=img*img_new.astype(bool)
    return img_out


def fill_water(img):
    copyimg = img.copy()
    copyimg.astype(np.float32)
    height, width = img.shape
    img_exp=np.zeros((height+20,width+20))
    height_exp, width_exp = img_exp.shape
    img_exp[10:-10, 10:-10]=copyimg
    mask1 = np.zeros([height+22, width+22],np.uint8)   
    mask2 = mask1.copy()
    mask3 = mask1.copy()
    mask4 = mask1.copy()
    print(height_exp, width_exp)
    print(mask1.shape)
    cv2.floodFill(np.float32(img_exp), mask1, (0, 0), 1) 
    cv2.floodFill(np.float32(img_exp), mask2, (35, 58), 1) 
    cv2.floodFill(np.float32(img_exp), mask3, (height_exp-1, 0), 1) 
    cv2.floodFill(np.float32(img_exp), mask4, (0, 58), 1)
    mask = mask1 | mask2 | mask3 | mask4
    output = mask[1:-1, 1:-1][10:-10, 10:-10]
    return output

target_dir = "test"
output_dir = "test"
split_target_dir(target_dir,output_dir)








