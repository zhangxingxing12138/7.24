class Gun:
    def __init__(self,model):
        self.model = model
        self.bullet_count = 0
    def add_bullet(self,count):
        self.bullet_count+=count
    def shoot(self):
        if self.bullet_count<=0:
            print('没有子弹了。。。')
            return
        self.bullet_count-=1
        print("%s 发射子弹%d..." % (self.model, self.bullet_count))
ak47 = Gun('ak47')
ak47.add_bullet(50)
ak47.shoot()
class Solider:
    def __init__(self,name):
        self.name = name
        self.gun = None
    def fire(self):
        if self.gun is None:
            print("%s 还没有枪..." % self.name)
            return
        print('冲啊。。。%s'%self.name)
        self.gun.add_bullet(100)
        self.gun.shoot()
ak47 = Gun('ak47')
xusanduo = Solider('许三多')
xusanduo.fire()


