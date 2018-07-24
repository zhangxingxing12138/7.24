class Course():
    def __init__(self,number,title,teacher,place):
        self.number=number
        self.title=title
        self.teather=teacher
        self.__place=place
    def showcourse(self):
        print('我的课程编号是{}\n课程名称为{}\n任课老师是{}老师\n上课地点在{}'.format(self.number,self.title,self.teather,self.__place))
shuxueke=Course('003','数学','程胜华','主教三楼')
shuxueke.showcourse()

