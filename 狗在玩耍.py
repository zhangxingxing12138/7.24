class Dog():
    def __init__(self,name):
        self.name=name
    def game(self):
       print("%s 蹦蹦跳跳的玩耍..." %self.name)
class XiaoTiandog(Dog):
    def game(self):
        print("%s 飞到天上去玩耍..." % self.name)
class Person():
    def __init__(self,name):
        self.name = name
    def game_with_dog(self, dog):

        print("%s 和 %s 快乐的玩耍..." % (self.name, dog.name))
                
wangcai = XiaoTiandog('飞天旺财')
xiaoming=Person('小明')
xiaoming.game_with_dog(wangcai)
wangcai.game()
