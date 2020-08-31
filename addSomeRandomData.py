from backend.models import Student
import random
"""
插入测试数据
"""
def insert(request):
    # 随机整数 作为学号
    for i in range(0, 5):
        studentNum = int(random.uniform(0, 1) * 1000000)
        # 从models文件中获取student对象
        student = Student()
        # 给对象赋值
        student.studentNum = studentNum
        student.name = 'tom' + str(i)
        student.age = 10 + int(random.uniform(0, 10))
        student.sex = random.choice([True, False])
        student.mobile = int(random.uniform(0, 1) * 10000000000)
        # 插入数据
        student.save()

    return HttpResponse('数据插入完毕')
