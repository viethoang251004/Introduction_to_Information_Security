from PIL import Image, ImageDraw
import os
import sys
from random import SystemRandom
random = SystemRandom()
xrange = range


infile = "C:/Tap/BaoMatThongTin/file_to_encrypt.png"
#if not os.path.isfile(infile):
    #print("That file does not exist.")
    #exit()

img = Image.open(infile)

f, e = os.path.splitext(infile)
out_filename_A = f+"_A.png"
out_filename_B = f+"_B.png"

img = img.convert('1') 

print("Image size: {}".format(img.size))
width = img.size[0]*2
height = img.size[1]*2
print("{} x {}".format(width, height))
out_image_A = Image.new('1', (width, height))
out_image_B = Image.new('1', (width, height))
draw_A = ImageDraw.Draw(out_image_A)
draw_B = ImageDraw.Draw(out_image_B)

patterns = ((1, 1, 0, 0), (1, 0, 1, 0), (1, 0, 0, 1),
            (0, 1, 1, 0), (0, 1, 0, 1), (0, 0, 1, 1))

for x in xrange(0, int(width/2)):
    for y in xrange(0, int(height/2)):
        pixel = img.getpixel((x, y))
        pat = random.choice(patterns)
        draw_A.point((x*2, y*2), pat[0])
        draw_A.point((x*2+1, y*2), pat[1])
        draw_A.point((x*2, y*2+1), pat[2])
        draw_A.point((x*2+1, y*2+1), pat[3])
        if pixel == 0:  
            draw_B.point((x*2, y*2), 1-pat[0])
            draw_B.point((x*2+1, y*2), 1-pat[1])
            draw_B.point((x*2, y*2+1), 1-pat[2])
            draw_B.point((x*2+1, y*2+1), 1-pat[3])
        else:
            draw_B.point((x*2, y*2), pat[0])
            draw_B.point((x*2+1, y*2), pat[1])
            draw_B.point((x*2, y*2+1), pat[2])
            draw_B.point((x*2+1, y*2+1), pat[3])

out_image_A.save(out_filename_A, 'PNG')
out_image_B.save(out_filename_B, 'PNG')
print("Done.")