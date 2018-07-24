class Animal():
    def __init__(self,color):
        self.color = color
        
    def call(self):
        print('叫')
class Fish(Animal):
    def __init__(self,color):
        super().__init__(color)
        self.tail = True
        
    def call(self):
        
        print('%s的鱼再叫'%self.color)
xiaoyu=Fish('黄色')


xiaoyu.call()
