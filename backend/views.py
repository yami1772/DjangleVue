import json
import requests
from django.core import serializers
from django.views.decorators.http import require_http_methods
from django.http import JsonResponse
from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.template import loader

# Create your views here.
from .models import Student
import random


# def index(request(method, url, body=None, headers={})):
def index(request):
    Student_list = Student.objects.order_by('studentNum')[:10]
    StuNum_output = ', '.join([q.studentNum for q in Student_list])
    StuName_output = ', '.join([q.name for q in Student_list])
    # output = stuName_output.join(StuNum_output)
    return HttpResponse(StuName_output)


def renderIndex(request):
    Student_list = Student.objects.order_by('-pub_date')[:5]
    context = {'Student_list': Student_list}
    return render(request, 'backend/renderIndex.html', context)


def detail(request, student_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'polls/detail.html', {'question': question})


"""
插入测试数据
"""


def insert(request):
    # 随机整数 作为学号
    for i in range(0, 5):
        studentNum = int(random.uniform(0, 1) * 10000000000)
        # 从models文件中获取student对象
        student = Student()
        # 给对象赋值
        student.studentNum = studentNum
        student.name = 'tom' + str(i)
        student.age = 15
        student.sex = random.choice([True, False])
        student.mobile = int(random.uniform(0, 1) * 10000000000)
        # 插入数据
        student.save()

    return HttpResponse('数据插入完毕')


"""
查询
"""


def find(request):
    #sql = 'select * from student'
    # django 也可以执行原生的sql语句
    #result = Student.objects.raw(sql)

    # 查询name = tom1的数据
    result = Student.objects.filter(name='tom1')
    """
    result为<class 'django.db.models.query.QuerySet'>的对象
    需要进行数据处理
    """
    arr = []
    for i in result:
        content = {'学号': i.studentNum, '姓名': i.name, '性别': i.sex}
        arr.append(content)
    print(arr)
    print(type(arr))
    return HttpResponse(arr)


"""
修改
"""


def modify(request, studentNum):
    # 通过学号获取student对象
    student = Student.objects.get(studentNum=studentNum)
    # 设置student的name为jack
    student.name = 'jack'
    student.save()
    return HttpResponse('修改成功.')


"""
删除
"""


def delete(request, studentNum):
    try:
        student = Student.objects.get(studentNum=studentNum)
        student.delete()
        return HttpResponse('删除成功.')
    except:
        return HttpResponse('\n\nsth wrong.')


'''
列表
'''


def show_list(request):
    response = {}
    try:
        stu = Student.objects.filter()
        response['list'] = json.loads(serializers.serialize("json", stu))
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1

    return JsonResponse(response)



'''
新增
'''


@require_http_methods(["GET"])
def addStu(request):
    response = {}
    # try:
    #     stu = Student(studentNum=request.GET.get('studentNum'))
    #     stu.save()
    #     response['msg'] = 'success'
    #     response['error_num'] = 0
    # except  Exception as e:
    #     response['msg'] = str(e)
    #     response['error_num'] = 1
    response['msg'] = 'empty class function found'
    return JsonResponse(response)
