class Circle():
    def __init__(self,centre,radii,color):
        self.centre=centre
        self.radii=radii
        self.color=color
    def zhouchang(self):
        a=2*3.14*self.radii
        print('圆的周长为：%f'%a)
    def mianji(self):
        b=float(3.14*self.radii*self.radii)
        print('圆的面积为：%f'%b)
yuan=Circle((3,4),3,'红色')
yuan.zhouchang()
yuan.mianji()
