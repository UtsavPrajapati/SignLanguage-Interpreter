# -*- coding: utf-8 -*-
"""
Created on Mon Aug 17 13:52:48 2020

@author: user
"""

from PIL import ImageFont, ImageDraw, Image
import numpy as np

nep1 = ["ka","kha","ga","gha","nyae","cha","chha"]
nep2 = ["s","v","u","3","2","r","5"]

def nep(image,ch):
    fontpath = "./sagarmatha.ttf" #
    font = ImageFont.truetype(fontpath, 50)
    img_pil = Image.fromarray(image)
    draw = ImageDraw.Draw(img_pil)
    cr = nep2[nep1.index(ch)]
    #print(ch)
    draw.text((10, 20),cr, font = font, fill = (0, 255, 0, 1))
    img = np.array(img_pil)
    return img