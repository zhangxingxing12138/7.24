class Student():
    def __init__(self,name,age,scores):
        self.name=name
        self.age=age
        self.scores=scores
    def get_name(self):
        return self.name
    def get_age(self):
        return self.age
    def get_course(self):
        
        return max(self.scores)
     
xiaomei=Student('小梅',19,('80语文','68数学','90英语'))
print('我叫{}'.format(xiaomei.get_name()))
print('年龄为{}'.format(xiaomei.get_age()))
print('最高分{}'.format(xiaomei.get_course()))
