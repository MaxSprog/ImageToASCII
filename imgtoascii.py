from PIL import Image
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
    print("Wrong file name")
    exit()

comp = 7 - int(input("Please state level of vertical compression(0 for none, up to 5): "))
while comp >= img.size[1] or comp > 7:
    print("Level of vertical compression is too high!")
    comp = 7 - int(input("Please state correct level of vertical compression: "))

pix = img.load()
newpix = [['0' for _ in range(img.size[0])] for _ in range(img.size[1])]
num = len(asc) - 1
for i in range(img.size[0]):
    for j in range(img.size[1]):
        col = pix[i,j]
        newpix[j][i] = asc[-1 * round((col[0] * coefs[0] + col[1] * coefs[1] + col[2] * coefs[2]) * num / 255)]

f = open("img.txt", "w")
if comp == 7: 
    for i in newpix:
        for j in i:
            f.write(j)
        f.write("\n")
else:
    for i in range(len(newpix)):
        if i % comp == 0:
            continue
        for j in range(len(newpix[i])):
            f.write(newpix[i][j])
        f.write("\n")
f.close()

# for i in range(len(newpix)):
#     if i % 2 == 0:
#         continue
#     for j in range(len(newpix[i])):
#         print(newpix[i][j], end='')
#     print()

subprocess.check_output('start /wait ' + os.path.abspath("img.txt"), shell=True)