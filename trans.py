# -*- coding: utf-8 -*-
"""
Created on Mon Aug 17 13:52:48 2020

@author: user
"""

from PIL import ImageFont, ImageDraw, Image
import numpy as np

nep1 = ["ka","kha","ga","gha","nyae","cha","chha","jaa","jha","nya","tah","tha"
        ,"da","dha","ana","ta","dah","dhaa","na","pa","pha","ba","bha","ma","ya",
        "ra","la","wo","sha","ssha","saa","ha","ksa","tra","gya",
        "shunna","eak","dui","teen","chaar","paach","chaa","saat","aath","naau"]
nep2 = ["s","v","u","3","8=","r","5","h","em","`","6","7"
        ,"8","9","0f","t","b","B","g","k","km","a","e","d","o",
        "/","n","j","z","if",";","x","If","q","1",
        ")","!","@","#","$","%","^","&","*","("]

print(len(nep1))
print(len(nep2))
def nep(image,ch):
    fontpath = "./sagarmatha.ttf" 
    font = ImageFont.truetype(fontpath, 50)
    img_pil = Image.fromarray(image)
    draw = ImageDraw.Draw(img_pil)
    cr = nep2[nep1.index(ch)]
    #print(ch)
    draw.text((10, 20),cr, font = font, fill = (0, 255, 0, 1))
    img = np.array(img_pil)
    return img

def nepSet(image,lst):
    fontpath = "./sagarmatha.ttf" 
    font = ImageFont.truetype(fontpath, 50)
    img_pil = Image.fromarray(image)
    draw = ImageDraw.Draw(img_pil)
    cr = ""
    for ch in lst:
        cr += nep2[nep1.index(ch)]
    #print(ch)
    draw.text((10, 400),cr, font = font, fill = (0, 255, 0, 1))
       
    img = np.array(img_pil)
    return img
