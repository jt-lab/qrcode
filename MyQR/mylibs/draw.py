# -*- coding: utf-8 -*-

from PIL import Image, ImageColor
import os

def draw_qrcode(abspath, qrmatrix,background, foreground):
    unit_len = 3
    x = y = 4*unit_len
    pic = Image.new('1', [(len(qrmatrix)+8)*unit_len]*2, background)
    
    for line in qrmatrix:
        for module in line:
            if module:
                draw_a_black_unit(pic, x, y, unit_len, ImageColor.getcolor(foreground, "RGB"))
            x += unit_len
        x, y = 4*unit_len, y+unit_len

    saving = os.path.join(abspath, 'qrcode.png')
    pic.save(saving)
    return saving
    
def draw_a_black_unit(p, x, y, ul, color):
    for i in range(ul):
        for j in range(ul):
            p.putpixel((x+i, y+j), color)
