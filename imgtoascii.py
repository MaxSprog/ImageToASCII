from PIL import Image
from math import floor
import subprocess
import os

coefs = (0.2126, 0.7152, 0.0722,)

asc = []
f = open("symbols.txt", "r")
for x in f:
    asc.append(x[:-1])
f.close()

i = input("Enter picture's file name: ")
try:
    img = Image.open(i)
except:
    print("wrong file name")
pix = img.load()
newpix = [['0' for _ in range(img.size[0])] for _ in range(img.size[1])]
num = len(asc)
for i in range(img.size[0]):
    for j in range(img.size[1]):
        col = pix[i,j]
        newpix[j][i] = asc[-1 * floor((col[0] * coefs[0] + col[1] * coefs[1] + col[2] * coefs[2]) * num / 255)]

f = open("img.txt", "w")

for i in newpix:
    for j in i:
        f.write(j)
    f.write("\n")
f.close()

subprocess.check_output('start /wait ' + os.path.abspath("img.txt"), shell=True)