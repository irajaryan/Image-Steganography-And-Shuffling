from PIL import Image
import math

im = Image.open("outEaster.png", "r")
arr = im.load() 

def rot(A, n, x1, y1):
    temple = []
    for i in range(n):
        temple.append([])
        for j in range(n):
            temple[i].append(arr[x1+i, y1+j])
    for i in range(n):
        for j in range(n):
            arr[x1+i,y1+j] = temple[n-1-i][n-1-j]


xres = 480
yres = 480
BLKSZ = 32 #blocksize
for i in range(2, BLKSZ+1):
    for j in range(int(math.floor(float(xres)/float(i)))):
        for k in range(int(math.floor(float(yres)/float(i)))):
            rot(arr, i, j*i, k*i)
for i in range(3, BLKSZ+1):
    for j in range(int(math.floor(float(xres)/float(BLKSZ+2-i)))):
        for k in range(int(math.floor(float(yres)/float(BLKSZ+2-i)))):
            rot(arr, BLKSZ+2-i, j*(BLKSZ+2-i), k*(BLKSZ+2-i))

im.save("out"+str(BLKSZ)+".png")
