import numpy as np
import matplotlib.pyplot as plt
import random

#三角形の幾何学画像生成プログラム

class MyGeometry:
    def __init__(self):
        self.color1 = [0,0,0]
        self.color2 = [255,255,255]

    #色設定
    def set_color(self, color):
        self.color1 = color

    def create_geometry(self, size = 10, height = 30, width = 40, file_name = "default"):
        self.out = [[[0] * 3 for _ in range(width*size)] for _ in range (height*size)]
        print(np.shape(self.out))
        for i in range(0, height):
            for j in range(0, width):
                random.seed()
                rand1 = random.randint(0, 510)
                random.seed()
                rand2 = random.randint(0, 510)
                color1 = [min(rand1, 255), max(0, rand1 - 255), max(0, rand1 - 255)]
                color2 = [max(0, rand2 - 255), max(0, rand2 - 255), min(rand2, 255)]
                mid_color = [min(int((rand1+rand2)/2),255), max(0,int(((rand1+rand2)-510)/2)), max(0,int(((rand1+rand2)-510)/2))]
                for x in range(0, size):
                    self.out[x+size*i][x+size*j] = mid_color
                for k in range(0, size-1):
                    for l in range(k+1, size):
                        # self.debug(k+size*i,l+size*j)
                        # self.debug((size)*(i+1)-k-1,(size)*(j+1)-l-1)
                        # print(" ")
                        self.out[k+size*i][l+size*j] = color1
                        self.out[size*(i+1)-(k+1)][size*(j+1)-(l+1)] = color2
        img = np.array(self.out, dtype=np.uint8)
        plt.imsave(file_name+".png", img, dpi=640)

    def debug(self,x,y):
        print("{}, {}".format(y,x))


if(__name__ == "__main__"):
    g = MyGeometry()
    g.create_geometry(25,60,60,"createdImage")
