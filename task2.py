"""
Denoise Problem
(Due date: Nov. 25, 11:59 P.M., 2019)
The goal of this task is to denoise image using median filter.

Do NOT modify the code provided to you.
Do NOT import ANY library or API besides what has been listed.
Hint: 
Please complete all the functions that are labeled with '#to do'. 
You are suggested to use utils.zero_pad.
"""


import utils
import numpy as np
import json

def median_filter(img):
    """
    Implement median filter on the given image.
    Steps:
    (1) Pad the image with zero to ensure that the output is of the same size as the input image.
    (2) Calculate the filtered image.
    Arg: Input image. 
    Return: Filtered image.
    """
    # TODO: implement this function.
    
    rows=(len(img))
    cols=(len(img[0]))
    
    
    """padding the image"""
    img=utils.zero_pad(img,1,1)
    
    """convolution"""
    
    
    img_conv=[]
    
    for i in range(rows):
        each_row=[]
        for j in range(cols):
            
            each_list=[]
            for m in range(i,i+3):
                for n in range(j,j+3):
                    
                    each_list.append(img[m][n])
                    
            each_list=sorted(each_list)
            
            median=each_list[4]
            each_row.append(median)
        img_conv.append(each_row)
        
    return (np.array(img_conv)).astype(np.uint8)

def mse(img1, img2):
    """
    Calculate mean square error of two images.
    Arg: Two images to be compared.
    Return: Mean square error.
    """    
    # TODO: implement this function.
    
    mse=0
    
    for i in range(len(img1)):
        for j in range(len(img1[0])):
            mse+=(img1[i][j]-img2[i][j])**2
    
    return (mse/(len(img1)*len(img1[0])))
    

if __name__ == "__main__":
    img = utils.read_image('lenna-noise.png')
    gt = utils.read_image('lenna-denoise.png')

    result = median_filter(img)
    error = mse(gt, result)

    with open('results/task2.json', "w") as file:
        json.dump(error, file)
    utils.write_image(result,'results/task2_result.jpg')


