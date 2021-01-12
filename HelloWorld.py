# print("Python3 解释器")

# 缩进语法

# """
# {
#   name:
# }
# """

# print()

# a = {
#   "id": 12,
#   "name": "hello",
# }

# print(a.id)

# python 列表

# Python 变量标识符没有类型

# 堆栈

# BIF 内置函数

# movies = ["A", 'b']
# movies.remove('b')
# print(movies)
# movies = ["The Holy Grail", "The Life of Brian", "The Meaning of Life"]
# movies.insert(1, 1975);
# movies.insert(3, 1979);
# movies.insert(5, 1983);
# print(movies)


# # 2 面对少量数据，2更好，append

# # 列表处理代码被 Python 程序员称为组
# for (each_flick) in movies:
#   print(each_flick)

# if isinstance(movies, list):
#   print('true')

#   True;
# movies = ["The Holy Grail", 1975, "The Life of Brian", 1979, "The Meaning of Life", 1983]

# for each_item in movies:
#   if isinstance(each_item, list):
#     for each_item2 in movies:
#       if isinstance(each_item2, list):
#         for each_item3 in movies:
#           print(each_item3)
#       else:
#         print(each_item2)
#   else:
#     print(each_item)

# python3 默认递归深度不能超过100
# def For(movies1):
#   for each_item in movies1:
#     if isinstance(each_item, list):
#       For(each_item)
#     else:
#       print(each_item)

# print(dir(__builtins__))
# Python 社区

# list 函数如何编写，创建一个二维列表

# import random

# def createArr(row, col):
#   arr = []
#   rowCount = 0
#   colCount = 0
#   while rowCount < row:
#     arr.append([])
#     while colCount < col:
#       if random.randint(0, 1) == 0:
#         arr[rowCount].append("*  ")
#       else:
#         arr[rowCount].append("$  ")
#       colCount += 1
#     rowCount += 1
#     colCount = 0
#   rowCount = 0
#   return arr

# def deepFor(listArr):
#   # print(listArr)
#   for item in listArr:
#     if isinstance(item, list):
#       deepFor(item)
#       print()
#     else:
#       print(item, end="")

# deepFor(createArr(10, 10))

# b = 6
# for a in b:
#   print(a)

# arr = []
# arr[0] = 10

# 实现A Star

# arr = [
#   [0, 1, 1, 0, 1, 0, 0, 0],
#   [0, 0, 0, 1, 0, 0, 0, 0],
#   [1, 1, 0, 0, 1, 0, 1, 0],
#   [1, 1, 0, 0, 1, 0, 0, 0],
#   [1, 0, 1, 0, 1, 0, 0, 0],
#   [1, 1, 1, 0, 0, 0, 1, 0],
# ]

# # 二维数据 深度拷贝
# def copy(originArr, targetArr, index):
#   for item in originArr:
#     if isinstance(item, list):
#       targetArr.append([])
#       index += 1
#       copy(originArr[index], targetArr, index)
#     else:
#       targetArr[index].append(item)

# listArr = []
# copy(arr, listArr, -1)

# listArr[0][0] = 10
# print(listArr)
# print(arr)
# # 引用copy
# arr1 = arr.copy()

# arr[0][0] = 10
# print(arr1)
# print(arr)

# 模块无处不在，pypi 就是python 的存储库

# 不同的编辑器是如何得知python import 路径的， 首先python 路径肯定是统一的，那么说明他们都去找了默认的

# from distutils.core import setup

# setup (
#   name = 'nester',
#   version = '1.0.0',
#   py_modules = ['nester'],
#   author = 'hfpython',
#   author_email = '',
#   url = '',
#   description = ''
# )

# 导入模块
# import nester

# nester.add(1, 2)

# 文件可以
# import aaa

# test.multify.multi(5, 5)

# import 就是导入一个文件夹或者文件名

# pyc 是编译后的代码

# import sys

# print(sys.path)

# enumerate()

# BIF 有自己的命名空间，这个命名空间名为 __builtins__

# 基本语法 列表，构建发布，模块
# 处理异常

# python 中的标准 打开 处理 关闭

# import os

# # 当前工作目录
# print(os.getcwd())
# os.chdir('./txt')
# print(os.getcwd())

# the_file = open('seach.txt')


# for txt in the_file:
#   print(txt)
# # 默认GBK 编码
# # print(the_file.readline(), end='') # 1
# # print(the_file.readline(), end='') # 2
# # print(the_file.readline(), end='') # 3
# # print(the_file.readline(), end='') # 4
# # print(the_file.readline(), end='') # 5

# # the_file.seek(0)
# # # 读取完毕
# # print(the_file.readline(), end='') # 1
# # print(the_file.readline(), end='') # 2
# # the_file.seek(1)
# # print(the_file.readline(), end='') # 2

# # 记住一定要关闭
# the_file.close()

# import os

# os.chdir('./txt')
# # 记住两种错误类型， Value Error，IOError
# # if os.path.exists('seach.txt'):
# try:
#   data = open('seach.txt')

#   for reach_line in data:
#     try:
#       (name, value) = reach_line.split(':')
#       print(name, end='')
#       print(" said: ", end='')
#       print(value, end='')
#     except ValueError:
#       pass
# except IOError:
#   print("the data file is missing!")

# 运行时的错误叫做异常， exception
# a

# if 0:
#   print(11)

# print(data.readline(), end='')
# print(data.readline(), end='')
# print(data.readline(), end='')
# print(data.readline(), end='')
# print(data.readline(), end='')

# # 1 臃肿的if else 逻辑判断
# for txt in data:
#   if txt.find(':') >= 0:
#     (name, sta) = txt.split(':', 1)
#   else:
#     name = txt
#     sta = ' 没有东西\n'
#   print(name, sta, end='')

# data.close()

# s = "Jude: hello world"

# (name, sta) = s.split(":")

# print(name, sta)

# help(s.split)

# 保存你的工作

# open 除了read 模式，read and write readOnly

# import os

# os.chdir('./txt')

# # a追加
# data = open('data.out3', 'w+')

# # 写入文件 file
# print("lajdljlafj", file=data)

# # flushing
# data.close()

# try:
#   pass
# except:
#   pass
# finally:
#   print('aksjdflasjdlf')

# python 中的字符串是不可变的哦

# try:
#   a = 10
#   c = a + b
# except:
#   pass
# finally:
#   if 'c' in locals():
#     print(c)

# try:
#   a = 10
#   a + b
# except NameError as err:
#   print("你的代码报错了》", str(err))

# try:
#   data = open('test1.txt', 'w')
#   print("it is", file=data)
# except IOError as err:
#   print("File  error" + str(err))
# finally:
#   if 'data' in locals():
#     data.close()

# # try/except/finally

# try:
#   with open('test.1txt', 'w') as data: 不用操心关闭的问题
#     print('It is', file=data)
# except IOError as err:
#   print("File  error" + str(err))

# with 使用了一种名为上下文管理协议的python 技术

# try:
#   with open('man_data.txt', 'w') as man_file:
#     print('man', file=man_file)
#   with open('other_data.txt', 'w') as other_file:
#     print('other_data', file=other_file)
# except IOError as err:
#   print('File error: ' + str(err))

# with open('ma', 'w') as man_file, open('other', 'w') as other_file:

# print 主要是告诉你 数据在内存中的样子，所以他一般不会做过多处理，模仿python 解释器实际存储列表数据的格式来显示你的数据

# import sys

# sys.stdout('kasjdlfjals')

# import os

# os.chdir('txt')

# try:
#   data = open('data.txt', 'w+')
#   print("hdalskjfdsla", file=data)
# except IOError as err:
#   print('发生错误' + str(err))
# finally:
#   if 'data' in locals():
#     data.close()
# w 模式下本来应该是不能创建文件的，他只能写入文件，w+ 在文件不存在的时候会创建文件，a是追加模式 append
# try:
#   with open('data.txt1321', 'w') as data:
#     print('nihaoya', file=data)
# except IOError as err:
#   print("出错了哦" + str(err))

# import sys

# 标准输出
# sys.stdout

# print("aaa", file=sys.stdout)

# pickle 保存和加载几乎任何python数据对象，包括列表

# import pickle
# import os

# os.chdir('txt')

# # pickle 的唯一要求 就是已二进制访问模式打开这些文件

# # with open('pickle', 'wb') as mysavedata:
# #   pickle.dump([1, 2, 'three'], mysavedata)

# with open('pickle', 'rb') as myresetdata:
#   a_list = pickle.load(myresetdata)

# print(a_list)

# import pickle

# try:
#   pickle.dump(man, man_file)
#   pickle.dump(other, other_file)
# except pickle.PickleError as perr:
#   print('Pickling error: ' + str(perr))

# 数据各式各样，有不同的大小，格式和编码

# import random

# for i in range(0, 10):
#   for row in range(0, 10):
#     for col in range(0, 10):
#       if random.randint(0, 1) == 1:
#         print('*  ', end='')
#       else:
#         print('$  ', end='')
#     print()
#   print()

# 数据有不同格式，大小，编码， 格式 大小，编码
# 格式 后缀
# 最重要的区别就是编码了 utf-8 utf-16
# 格式

# import os
# import pickle
# # 切换执行环境目录
# os.chdir('run')

# with open('1.txt', 'r') as data1:
#   a_list = data1.readline().strip().split(',')

# def sanitize(time_string):
#   if time_string.find('-') >= 0:
#     (mins, secs) = time_string.split('-')
#   elif time_string.find(':') >= 0:
#     (mins, secs) = time_string.split(':')
#   else:
#     return time_string

#   return mins + '.' + secs

# copy_list_a = []

# for item in a_list:
#   copy_list_a.append(sanitize(item))

# copy_list = sorted(copy_list_a)

# print(copy_list)

# with open('1.txt', 'w') as data2:
#   print(copy_list, file=data2)
# pickle.dump(copy_list, data2)

# 串链

# data = [1, 5, 2, 1, 45, 56]

# a = sorted(data)


# print(a, data)

# reverse=True 代表降序排列
# sorted(reverse=True)

# 列表推导 ？？？？？ 这是什么东西 一个列表转换到另一个列表时要编写的代码量

# """
# 4步曲
# 1. 创建列表
# 2. 迭代列表
# 3. 数据处理
# 4. 追加数据
# """

# cl = ['1', 2, 3, 4, 5]
# # 列表推导式
# clear_mikely = [item for item in cl]

# print(clear_mikely)

# 函数式编程， 面向对象，过程式编程

# 去重如何做
# cl = ['1.23', '1.45', '1.45', '1.67', '1.23', '2.45']

# cl2 = []

# for item in cl:
#   if item not in cl2:
#     cl2.append(item)

# print(sorted(cl2))

# 更换数据结构
# 使用集合

# 工厂函数构建集合
# distances = set()

# distances.add(1)

# print(distances)

# distances = {10.5, 11, 7, 'aa'}

# print(distances)

# 工厂函数用来创建某种类型的新的数据项

# 现实中的工厂生产产品 这个概念由此得名

# cl = ['1.23', '1.45', '1.45', '1.67', '1.23', '2.45']

# 这叫切片
# print(sorted(set(cl))[0:3])

# def readFile(file_path) {
#   with open(file_path) as data:
#     return data.readline().strip().split(',')
# }
# readFile('mikey.txt')

# 类， 自己创建自己的数据结构

# 字典，列表，集合

# print(dict({1,2,3,4}))
# 字典
# a = 1
# dis = {a: 1}
# dis[2] = 12
# dis[2] = 'adfsafas'
# print(dis[2])

# 查找是如何查找，a 指代的是一个内存空间，0x1212

# cl = [12, 23]

# print(cl.pop(0))

# print(cl)

# print(type({}))

# dict1 = {
#   'name': sarah.pop(0),
#   'date': sarah.pop(0),
#   'time': sorted(set([sanitize(t) for t in sarah]))[0:3]
# }

# 字典 能够让数据相关联，但是其函数并没有关联

# 如何让函数与定制的数据也能产生关联

# class Athlete:
#   def __init__(self):
#     # The code
#     print('nih')
#     pass

# a = Athlete()

# class Athlete:
#   def __init__(self):
#     pass


# a = Athlete()
# 这句代码会转换为
# Athlete.__init__(a)

# class Circle:
#   def __init__(self, radius = 10, iSpeed = 5):
#     self.radius = radius
#     self.iSpeed = iSpeed

#   def move(self):
#     self.moveTo()

#   def moveTo(self):
#     print('aaaa')

# c =  Circle()
# c.move()

# class Athlete:
#   def __init__(self, a_name, a_dob=None, a_times=[]):
#     self.name = a_name
#     self.dob = a_dob
#     self.times = a_times

#   def tops(self):
#     return (sorted(set([t for t in self.times]))[0:3])

#   def add_time(self, time):
#     self.times.append(time)

#   def add_times(self, times=[]):
#     for item in times:
#       self.times.append(item)

# a = Athlete('Tom', '', ['1.23', '1.67', '2.23', '1.23'])

# print(a.tops())

# l = {'1.2', '121'}
# print(type(l))
# # print(l)

# l = [2.45]
# l.extend([1,2,3,4])
# print(l)

# 扩展定制类, 继承
# 继承内置 的list


# class A extend B{} JavaScript没有访问权限, 都是public, private, protected
# 提供一个类名,新类将派生这个类
# class A(list):
#   def __init__(self, a_name=None):
#     # 初始化派生的类
#     list.__init__([]) # super()
#     self.name = a_name

# a = A('hello')

# a.append('121')

# print(a.name)

# l = list([1])
# l.name = 121;

# print(l.name)

# class Athlete(list):
#   def __init__(self, a_name, a_dob=None, a_times=[]):
#     list.__init__(a_times)
#     self.name = a_name
#     self.dob = a_dob

#   def top3(self):
#     return (sorted(set([t for t in self]))[0:3])

# def add_time(self, time_value):
#   self.append(time_value)

# def add_times(self, list_of_times):
#   self.extend(list_of_times)

# 复杂的概念没必要全部一下了解完毕
# python 支持多重继承

# import nester
# import multify

# 模块组成的集合称为包

# from nester import add

# 相对导入 和 绝对导入 python3 属于绝对导入

# 绝对导入指的是 sys.path 下,和 当前目录同级
#

# from .nester import add

# from test import multify
# import test.multify

# test.multify.multi(1,2)
# 导入不同目录的文件, 需要在其文件目录下新建 __init__ 文件
# 1. from dir import file
# 2. import dir.file 缺点是 你下面的命名空间都需要编写成 dir.file 形式才能调用 dir.file 文件内的代码

# 当使用import 语句导入模块时,解释器会搜索当前模块所在的目录以及sys.path 指定的路径去找需要的import的模块,所以这里直接把上级目录加到了sys.path里
# sys.path.append('..')

# 文件夹作为package需要满足如下两个条件
# 文件夹中必须存在有 __init__.py 文件, 可以为空
# 不能作为顶层模块来执行该文件夹中的py文件。
# 注意：列表第一个元素为空，即代表当前目录，所以你自己定义的模块在当前目录会被优先导入。

# import 复杂1 暂时没有搞懂,大致知道
# """
#   import 导入路径 sys.path 第一个是空,代表当前目录
#   可以通过 sys.path.append('..') 这样的方式添加

#   顶层模块

#   package import不能导入文件夹,只能导入package
#   package 满足两个条件
#     1. 当前文件夹中有__init__.py 文件,即使他是空
#     2. 不能作为顶层模块来执行该文件夹中的py文件
# """


# a = {'a': 1, 'b': 2}

# print(a['a'])

# 类中定义的每一个方法都必须提供self 作为第一个参数

# 生成动态内容的过程已经标准化了, ,称为通用网关接口(Common Gateway Interface, CGI)
# 符合这个标准的程序通常称为CGI脚本

# from string import Template

# 我需要一个服务器
# const http = require('http')
# """
#   http.createServer

#   http.listen(8080)
# """

# python 实现本地服务器

# 导入必备的库 http服务器,CGI模块
# from http.server import HTTPServer, CGIHTTPRequestHandler

# port = 8080
# # 创建一个http服务器
# httpd = HTTPServer(("", port), CGIHTTPRequestHandler)

# # 显示一个友好的信息并启动服务器
# print('starting simple_httpd on port: ' + str(httpd.server_port))
# httpd.serve_forever()

# 如何搭建python 服务器

# import glob
# import cgi
# import cgitb
# from http.server import HTTPServer, CGIHTTPRequestHandler

# # cgitb.enable()
# port = 8080
# httpd = HTTPServer(('', port), CGIHTTPRequestHandler)

# # 查询文件列表
# data_files = glob.glob('./*')

# print(data_files)

# print('servering is running 8080')
# httpd.serve_forever()

# raise TypeError('niakdfjlasjla')

# class A:
#   def __init__(self, name):
#     self.name = name

#   # 这个修饰符允许访问 "top2()" 时 把他当成类属性
#   # @property
#   def top2(self):
#     return self.name


# a = A('aaaa')

# print(a.top2)
# A.__init__(a)

# @property 这个修饰符可以让类的方法表现得跟属性一样

# CGI 通用网关接口
# (Common Gateway interface)

# python 可以在 android 上运行
# SL4A
# Scripting Layer 4 Android 支持python2

# JSON 是Web上使用最广泛的数据交换格式之一

# 那时候支持JSON的唯一语言就是JavaScript

# import json

# names = ['John', ['johnnty', 'jack'], 'Michael', ['Mike', 'mikey', 'mick']]

# print(names)
# print(json.dumps(names))

# import sqlite3
# python 3 预装了SQLite 3 无需配置


# 链接 创建游标 执行sql操作 提交修改 关闭连接

# import sqlite3

# 链接
# connection = sqlite3.connect('test.sqlite')
# # 创建数据游标
# cursor = connection.cursor()
# # 执行sql操作

# connection.commit()
# connection.close()

# import adsfa

# dll 是什么意思, (Dynamic Link Libray) 动态链接库, 二进制文件, 共享DLL
# import sqlite3

# connection = sqlite3.connect('coachdata.sqlite')
# cursor = connection.cursor()

# name = 'Tom'
# dob = 'James'
# cursor.execute("INSERT INTO athletes (name, dob) VALUES (?, ?)", (name, dob))

# # 使修改永久保存
# connection.commit()

# # 关闭数据库
# connection.close()

# """
# li1 = []
# for h in sorted(row_data['10mi'].values(), reverse=True),
# li1.append(h)
# """

# """
# li1 = []
# for t in row_data['20k'].keys()
#   if row_data['20k'][t] == '79.3':
#     li1.append(t)
# """

# """
# li1 = []

# """
# BIF Built In Function
# print(input())

# print(input("What you name \n"))

# import tkinter

# python 中确实存在线程, 但是要尽可能避免
# Python 使用一种称为全局解释器锁的技术来实现

# """
# Web 和 Internet
# 科学计算和统计
# 人工智能
# 桌面界面开发
# 软件开发
# 后端开发
# 网络爬虫
# """

#  with open()

# lambda 表示匿名函数

# python 写爬虫 如何编写 需要导入什么库

# import requests
# import urllib
# import re
# import random


# requests.post('https://www.zhihu.com/question/22591304/followers',timeout=10).text

# 导入turtle包的所有内容:
# from turtle import *

# # 设置笔刷宽度:
# width(4)

# # 前进:
# forward(200)
# # 右转90度:
# right(90)

# # 笔刷颜色:
# pencolor('red')
# forward(100)
# right(90)

# pencolor('green')
# forward(200)
# right(90)

# pencolor('blue')
# forward(100)
# right(90)

# # 调用done()使得窗口等待被关闭，否则将立刻关闭窗口:
# done()

# pdb 调试好不方便

# import turtle
# # import pdb

# # pdb.set_trace()
# turtle.width(4)

# turtle.pencolor('red')
# turtle.forward(200)
# turtle.right(45)

# turtle.pencolor('blue')
# turtle.forward(200)
# turtle.right(45)

# turtle.pencolor('green')
# turtle.forward(200)

# turtle.done()

# from turtle import *

# def drawStar(x, y):
#     pu()
#     goto(x, y)
#     pd()
#     # set heading: 0
#     seth(0)
#     for i in range(5):
#         fd(40)
#         rt(144)

# for x in range(0, 250, 50):
#     drawStar(x, 0)

# done()

# from turtle import *

# # 设置色彩模式是RGB:
# colormode(255)

# lt(90)

# lv = 14
# l = 120
# s = 45

# width(lv)

# # 初始化RGB颜色:
# r = 0
# g = 0
# b = 0
# pencolor(r, g, b)

# penup()
# bk(l)
# pendown()
# fd(l)

# def draw_tree(l, level):
#     global r, g, b
#     # save the current pen width
#     w = width()

#     # narrow the pen width
#     width(w * 3.0 / 4.0)
#     # set color:
#     r = r + 1
#     g = g + 2
#     b = b + 3
#     pencolor(r % 200, g % 200, b % 200)

#     l = 3.0 / 4.0 * l

#     lt(s)
#     fd(l)

#     if level < lv:
#         draw_tree(l, level + 1)
#     bk(l)
#     rt(2 * s)
#     fd(l)

#     if level < lv:
#         draw_tree(l, level + 1)
#     bk(l)
#     lt(s)

#     # restore the previous pen width
#     width(w)

# speed("fastest")

# draw_tree(l, 4)

# done()

# class A:

#   def __init__():
#     pass

#   @overload
#   def printName() -> int: ...

# import turtle

# turtle.width()

# class A:
#   # @overload
#   def pensize(self) -> int: ...

# class B(A):
#   pass
#   # def pensize(self) -> int:
#   #   return 'askdfjla'

# b1 = B()

# b1.pensize()

# import requests

# print(requests.get('https://www.baidu.com'))

# import urllib.request

# response = urllib.request.urlopen('https://blog.csdn.net/weixin_43499626')
# print(response.read().decode('utf-8'))

# import requests
# import ast

# headers = {'Connection': 'close',}
# s = requests.Session()

# tiantian_data = None
# tiantian_url = 'https://api.jikexiu.com/v1//device/category/list'

# with requests.Session() as s:
#   result_data = s.get(tiantian_url, headers=headers)
#   tiantian_data = ast.literal_eval(result_data.text)

# print(tiantian_data)

# get请求
# response = requests.get(url='https://api.jikexiu.com/v1//device/category/list'
# print(response.text)   #打印解码后的返回数据
# 带参数的requests get请求
# response = requests.get(url='https://blog.csdn.net/weixin_43499626', params={'key1':'value1', 'key2':'value2'})

# import requests

# #https://api.jikexiu.com/v1/promotion/coupon/list?key=jj_index_coupon
# sess = requests.session()
# sess.keep_alive = False

# import ssl
# import _ssl

# import requests

# response = requests.get(url='http://api.jikexiu.com/v1//promotion/coupon/list?key=jj_index_coupon')

# import sys

# print(sys.path)

# import ssl

# 中文的unicode 无法输出显示到 txt中
# import requests

# # response = requests.get(url='http://api.jikexiu.com/v1//promotion/coupon/list?key=jj_index_coupon')
# # response = requests.get(url='https://api.jikexiu.com/v1//device/category/list')

# # with open('data.json', 'w') as a:
# #   print('a', file=a)
# # for i in range(0, 100):
#   # response = requests.get(url='https://api.jikexiu.com/v1//device/category/list')
#   # 指定 encodeing就可以了
#   # with open('data.json', 'a', encoding='utf-8') as data_file:
#     # print(response.text, file=data_file)


# response = requests.get(url='https://uland.taobao.com/sem/tbsearch?refpid=mm_26632258_3504122_32538762&keyword=%E5%A5%B3%E8%A3%85&clk1=b5adff411b50a80f980e0b94fbe0cf67&upsId=b5adff411b50a80f980e0b94fbe0cf67')

# print(response.text)

# import os
# import sys

# # 切换工作目录
# os.chdir('D:\\LiJiaJian\\Code\\2-HTML\\phone\\1')
# # 切换目录 D:\LiJiaJian\Code\2-HTML\phone\1

# # 获取当前工作目录
# # print(os.getcwd())
# with open('index.html', 'w+') as data:
#   print("""<!DOCTYPE html>
# <html lang="en">
# <head>
#   <meta charset="UTF-8">
#   <meta name="viewport" content="width=device-width, initial-scale=1.0">
#   <link rel="stylesheet" href="./index.css">
#   <title>Document</title>
# </head>
# <body>

#   <script src="./index.js"></script>
# </body>
# </html>""", file=data)

# with open('index.css', 'w+') as data:
#   print("""html,body,div,span,applet,object,h1,h2,h3,h4,h5,h6,p,blockquote,pre,a,abbr,acronym,address,big,cite,code,del,dfn,em,img,ins,kbd,q,s,samp,small,strike,strong,sub,sup,tt,var,b,u,i,center,dl,dt,dd,ol,ul,li,fieldset,form,label,legend,table,caption,tbody,tfoot,thead,tr,th,td,article,aside,canvas,details,embed,figure,figcaption,footer,header,hgroup,menu,nav,output,ruby,section,summary,time,mark,audio,video {
# 	margin:0;
# 	padding:0;
# 	border:0;
# 	font-size:100%;
# 	font:inherit;
# 	font-weight:normal;
# 	vertical-align:baseline;
# }
# /* HTML5 display-role reset for older browsers */
# article,aside,details,figcaption,figure,footer,header,hgroup,menu,nav,section {
# 	display:block;
# }
# ol,ul,li {
# 	list-style:none;
# }
# blockquote,q {
# 	quotes:none;
# }
# blockquote:before,blockquote:after,q:before,q:after {
# 	content:'';
# 	content:none;
# }
# table {
# 	border-collapse:collapse;
# 	border-spacing:0;
# }
# th,td {
# 	vertical-align:middle;
# }
# /* custom */
# a {
# 	outline:none;
# 	color:#16418a;
# 	text-decoration:none;
# 	-webkit-backface-visibility:hidden;
# }
# a:focus {
# 	outline:none;
# }
# input:focus,select:focus,textarea:focus {
# 	outline:-webkit-focus-ring-color auto 0;
# }""", file=data)

# with open('index.js', 'w+') as data:
#   pass

# import os

# 创建文件夹
# os.makedirs('aaaa')
# os.removedirs('test.txt')
# os.remove('test/*.*/txt')

# import requests

# response = requests.get('blob:https://www.bilibili.com/93c47b03-51e3-4d9e-a436-ab908fe1372c')

# print(response.text)
# import win32api
# import win32con
# import win32gui
# from ctypes import *
# import time

# print(windll.user32.GetCursorPos())

# VK_CODE = {
#     'backspace':0x08,
#     'tab':0x09,
#     'clear':0x0C,
#     'enter':0x0D,
#     'shift':0x10,
#     'ctrl':0x11,
#     'alt':0x12,
#     'pause':0x13,
#     'caps_lock':0x14,
#     'esc':0x1B,
#     'spacebar':0x20,
#     'page_up':0x21,
#     'page_down':0x22,
#     'end':0x23,
#     'home':0x24,
#     'left_arrow':0x25,
#     'up_arrow':0x26,
#     'right_arrow':0x27,
#     'down_arrow':0x28,
#     'select':0x29,
#     'print':0x2A,
#     'execute':0x2B,
#     'print_screen':0x2C,
#     'ins':0x2D,
#     'del':0x2E,
#     'help':0x2F,
#     '0':0x30,
#     '1':0x31,
#     '2':0x32,
#     '3':0x33,
#     '4':0x34,
#     '5':0x35,
#     '6':0x36,
#     '7':0x37,
#     '8':0x38,
#     '9':0x39,
#     'a':0x41,
#     'b':0x42,
#     'c':0x43,
#     'd':0x44,
#     'e':0x45,
#     'f':0x46,
#     'g':0x47,
#     'h':0x48,
#     'i':0x49,
#     'j':0x4A,
#     'k':0x4B,
#     'l':0x4C,
#     'm':0x4D,
#     'n':0x4E,
#     'o':0x4F,
#     'p':0x50,
#     'q':0x51,
#     'r':0x52,
#     's':0x53,
#     't':0x54,
#     'u':0x55,
#     'v':0x56,
#     'w':0x57,
#     'x':0x58,
#     'y':0x59,
#     'z':0x5A,
#     'numpad_0':0x60,
#     'numpad_1':0x61,
#     'numpad_2':0x62,
#     'numpad_3':0x63,
#     'numpad_4':0x64,
#     'numpad_5':0x65,
#     'numpad_6':0x66,
#     'numpad_7':0x67,
#     'numpad_8':0x68,
#     'numpad_9':0x69,
#     'multiply_key':0x6A,
#     'add_key':0x6B,
#     'separator_key':0x6C,
#     'subtract_key':0x6D,
#     'decimal_key':0x6E,
#     'divide_key':0x6F,
#     'F1':0x70,
#     'F2':0x71,
#     'F3':0x72,
#     'F4':0x73,
#     'F5':0x74,
#     'F6':0x75,
#     'F7':0x76,
#     'F8':0x77,
#     'F9':0x78,
#     'F10':0x79,
#     'F11':0x7A,
#     'F12':0x7B,
#     'F13':0x7C,
#     'F14':0x7D,
#     'F15':0x7E,
#     'F16':0x7F,
#     'F17':0x80,
#     'F18':0x81,
#     'F19':0x82,
#     'F20':0x83,
#     'F21':0x84,
#     'F22':0x85,
#     'F23':0x86,
#     'F24':0x87,
#     'num_lock':0x90,
#     'scroll_lock':0x91,
#     'left_shift':0xA0,
#     'right_shift ':0xA1,
#     'left_control':0xA2,
#     'right_control':0xA3,
#     'left_menu':0xA4,
#     'right_menu':0xA5,
#     'browser_back':0xA6,
#     'browser_forward':0xA7,
#     'browser_refresh':0xA8,
#     'browser_stop':0xA9,
#     'browser_search':0xAA,
#     'browser_favorites':0xAB,
#     'browser_start_and_home':0xAC,
#     'volume_mute':0xAD,
#     'volume_Down':0xAE,
#     'volume_up':0xAF,
#     'next_track':0xB0,
#     'previous_track':0xB1,
#     'stop_media':0xB2,
#     'play/pause_media':0xB3,
#     'start_mail':0xB4,
#     'select_media':0xB5,
#     'start_application_1':0xB6,
#     'start_application_2':0xB7,
#     'attn_key':0xF6,
#     'crsel_key':0xF7,
#     'exsel_key':0xF8,
#     'play_key':0xFA,
#     'zoom_key':0xFB,
#     'clear_key':0xFE,
#     '+':0xBB,
#     ',':0xBC,
#     '-':0xBD,
#     '.':0xBE,
#     '/':0xBF,
#     '`':0xC0,
#     ';':0xBA,
#     '[':0xDB,
#     '\\':0xDC,
#     ']':0xDD,
#     "'":0xDE,
#     '`':0xC0}

# class POINT(Structure):
#     _fields_ = [("x", c_ulong),("y", c_ulong)]

# def get_mouse_point():
#     po = POINT()
#     windll.user32.GetCursorPos(byref(po))
#     return int(po.x), int(po.y)

# def mouse_click(x=None,y=None):
#     if not x is None and not y is None:
#         mouse_move(x,y)
#         time.sleep(0.05)
#     win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
#     win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)

# def mouse_dclick(x=None,y=None):
#     if not x is None and not y is None:
#         mouse_move(x,y)
#         time.sleep(0.05)
#     win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
#     win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
#     win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
#     win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)

# def mouse_move(x,y):
#     windll.user32.SetCursorPos(x, y)

# def key_input(str=''):
#     for c in str:
#         win32api.keybd_event(VK_CODE[c],0,0,0)
#         win32api.keybd_event(VK_CODE[c],0,win32con.KEYEVENTF_KEYUP,0)
#         time.sleep(0.01)

# if __name__ == "__main__":
#     mouse_click(2500,780)
#     str1 = 'python'
#     key_input(str1)
#     mouse_click(2500,780)

# import pyautogui
# import pyautogui
# import pynput
# import pythoncom
# import pyHook

# from pynput.mouse import Button, Controller

# mouse = Controller()

# mouse.move(5,-5)
# mouse.position = (10, 20)
# mouse.press(Button.left)
# mouse.release(Button.left)
# mouse.click(Button.left, )
# mouse.scroll(0, 100)

# print('当前指针位置{0}'.format(mouse.position))

# def press(key):
#   print(type(key))

# with 是python2.5引入的新的语法，上下文管理协议

# with 就是简化了流程图 try except finally
# 把资源分配和释放的相关代码统统去掉
# 确保执行过程中是否发生异常都有必要执行的清理操作

# with pynput.keyboard.Listener(press) as listener:
#   listener.join()

# pyautogui.keyDown('command')

# pyautogui.hotkey('win', 'r')
# pyautogui.keyDown('enter')
# # pyautogui.click(400, 400)
# pyautogui.moveTo(400, 400, duration=0.5)
# pyautogui.write('pip install pyHook', interval=0.05)

# pyautogui.keyDown('enter')


# -*- coding: utf-8 -*- #  2 # by oldj http://oldj.net/ #   3import pythoncom  4import pyHook     5def onMouseEvent(event):  6      7    # 监听鼠标事件      8    print "MessageName:",event.MessageName      9    print "Message:", event.Message     10    print "Time:", event.Time     11    print "Window:", event.Window     12    print "WindowName:", event.WindowName     13    print "Position:", event.Position     14    print "Wheel:", event.Wheel     15    print "Injected:", event.Injected           16    print"---"17   18    # 返回 True 以便将事件传给其它处理程序     19    # 注意，这儿如果返回 False ，则鼠标事件将被全部拦截     20    # 也就是说你的鼠标看起来会僵在那儿，似乎失去响应了     21    return True22  23def onKeyboardEvent(event):24   # 监听键盘事件     25    print "MessageName:", event.MessageName     26    print "Message:", event.Message     27    print "Time:", event.Time     28    print "Window:", event.Window     29    print "WindowName:", event.WindowName     30    print "Ascii:", event.Ascii, chr(event.Ascii)     31    print "Key:", event.Key     32    print "KeyID:", event.KeyID     33    print "ScanCode:", event.ScanCode     34    print "Extended:", event.Extended     35    print "Injected:", event.Injected     36    print "Alt", event.Alt     37    print "Transition", event.Transition     38    print "---"      39    # 同鼠标事件监听函数的返回值     40    return True 41 42def main():     43    # 创建一个“钩子”管理对象     44    hm = pyHook.HookManager()      45    # 监听所有键盘事件     46    hm.KeyDown = onKeyboardEvent     47    # 设置键盘“钩子”     48    hm.HookKeyboard()      49    # 监听所有鼠标事件     50    hm.MouseAll = onMouseEvent     51    # 设置鼠标“钩子”     52    hm.HookMouse()      53    # 进入循环，如不手动关闭，程序将一直处于监听状态     54    pythoncom.PumpMessages() 55 56if __name__ == "__main__":     57    main()

# print()

# position = pyautogui.position()

# pyautogui.moveTo(x=1716, y=14, duration=0.5)
# pyautogui.click()
# pyautogui.moveTo(x=1468, y=50, duration=0.5)
# pyautogui.click()
# # pyautogui.write("what? you name", interval=0.05)
# # pyautogui.keyDown('Ctrl')
# # pyautogui.keyDown('V')
# pyautogui.hotkey('ctrl', 'v')
# pyautogui.keyDown('Enter')
# pyautogui.keyDown('Enter')

# # 最后再回来
# pyautogui.moveTo(position, duration=0.5)

# pyautogui.alert('This is the message to display.')

# print(pyautogui.size()) (x=1716, y=14) (x=1468, y=50)
# pyautogui.moveTo(pyautogui.position())
# pyautogui.click()

# while True:
#   print(pyautogui.position())

# distance = 200

# while distance > 0:
#   pyautogui.drag(distance, 0)
#   distance -= 5
#   pyautogui.drag(0, distance)
#   pyautogui.drag(-distance, 0)
#   distance -= 5
#   pyautogui.drag(0, -distance)
#   print('1')

# pyautogui.moveTo(500, 500, duration=2, tween=pyautogui.easeInOutQuad)qunidayede
# pyautogui.write("""# div{width:0.5rem;height: 0.5rem;}""", interval=0.05)# div{width:0.5rem;height: 0.5rem;}

# pyautogui.keyDown('ctrl')
# pyautogui.keyDown('/')
#
# pyautogui.press(['8', '9', '1', '8', '9', '1','8', '9', '1', '8', '9', '1'], interval=5)

# 891891891891891
# 891891891891
# 891891891891
# div{width:0.5rem;height: 0.5rem;}

# div{width:0.5rem;height: 0.5rem;}

# div{width:0.5rem;height: 0.5rem;}
# div{width:0.5rem;height: 0.5rem;}

# div{width:0.5rem;height: 0.5rem;}

# pyautogui.keyDown('shift')

# import pynput

# keyboard = pynput.keyboard.Controller()
# keyboard.press(pynput.keyboard.KeyCode[96])
# keyboard.release(pynput.keyboard.KeyCode[96])

# def press(key):
#   print("key down" + str(key))
#   # try:
#   #   print('alphanumeric key {0} pressed'.format(key.char))
#   # except:
#   #   print('special key {0}'.format(key))

# def release(key):
#   print("key release" + str(key))

# listener = pynput.keyboard.Listener(
#   on_press=press,
#   on_release=release
# )

# listener.start()

# with pynput.keyboard.Listener(on_press=press, on_release=release) as listener:
#   listener.join()

# keyboard = pynput.keyboard.Controller()

# keyboard.type('aaaaaaaaaaaaa aAAAAAAAAAAAA 案件空手道解放了 阿斯兰的剑法')

# keyboard.type('你好')

# with keyboard.pressed(pynput.keyboard.Key.shift):
# keyboard.press('a')
# keyboard.press('a')
# keyboard.press('a')
# keyboard.press('a')
# keyboard.press('a')
# keyboard.press('a')
# keyboard.press('a')
# keyboard.press('a')
# keyboard.press('a')
# keyboard.press('a')
# keyboard.press('a')
# keyboard.press('a')

# keyboard.press('a')
# keyboard.press('a')
# keyboard.press('a')
# keyboard.press('b')
# keyboard.press('b')
# keyboard.press('b')
# pynput.keyboard.press('a')

# def move(x, y):
#   print('鼠标X: {0}'.format(x) + ' 鼠标Y: {0}'.format(y))


# def click(x, y, button, pressed):
#   print(button)
#   print('{0} at {1}'.format(
#         'Pressed' if pressed else 'Released',
#         (x, y)))
#   # if not pressed:
#     # Stop listener
#     # return False

# def scroll(x, y, dx, dy):
#   print('scrolled {0} at {1}'.format('down' if dy < 0 else 'up', (x,y)))
#   print('Scrolled {0}'.format((dx,dy)))

# with pynput.mouse.Listener(on_move=move, on_click=click, on_scroll=scroll) as listener:
#   listener.join()

# pynput 通过这个来监听鼠标和键盘事件，并且保存数据至file文件中
# pyautogui 通过这个实现自动化鼠标和键盘的控制

# from pynput.mouse import Listener
# import pyautogui

# print(pyautogui.prompt('slajfdlsjalfdj'))
# print(pyautogui.confirm('slakfl;sadkf;ak'))
# pyautogui.alert('sjlfasjd')

# pyautogui.typewrite('Hello world!', interval=0.5)


# button7location = pyautogui.locateOnScreen('calc7.png')

# print(button7location)

# pyautogui.moveTo(button7location.left + button7location.width/2, button7location.top + button7location.height/2, duration=0.5)

# img1 = pyautogui.screenshot(region=(1920/2, 0, 1920, 1080))
# print(img1, file=img1)
# pyautogui.scroll(-100, x=100, y=100)

# def click(x, y, button, pressed):
#   with open('auto.asuka', 'a') as data:
#     print('x:{0},y:{1},button:{2},pressed:{3}'.format(
#       x, y, button, pressed), file=data)


# def run():
#   comd_list = []
#   index = 0

#   # 读取指令
#   with open('auto.asuka', 'r') as data:
#     # 拆解指令
#     comd_list = data.read().split('\n')

#   # 预处理指令称为对象
#   for item in comd_list:
#     temp_list = item.split(',')
#     comd_list[index] = {}
#     for attr in temp_list:
#       obj = attr.split(':')
#       try:
#         # 如果这个可以成功 说明值是数字
#         comd_list[index][obj[0]] = int(obj[1])
#       except:
#         if obj[1] == 'True':
#           comd_list[index][obj[0]] = True
#         elif obj[1] == 'False':
#           comd_list[index][obj[0]] = False
#         else:
#           comd_list[index][obj[0]] = obj[1]

#     index += 1

#   # 执行指令
#   for cmd in comd_list:
#     pyautogui.moveTo(cmd['x'], cmd['y'], duration=0.2)
#     if cmd['pressed']:
#       pyautogui.mouseDown(button='left')
#     else:
#       pyautogui.mouseUp(button='left')
#     print(input('请输入指令'))

# run()

# with Listener(on_click=click) as listener:
#   listener.join()

# import pyautogui

# posi = pyautogui.position()

# pyautogui.click(posi)

# print("""#app {0}#{1}alert{{}}""".format(12, 12))

# if pyautogui.confirm('are you sure？ : ') == 'OK':
#   width = pyautogui.prompt('width')
#   height = pyautogui.prompt('height')
#   pyautogui.write("""
#     #app #alert{{
#       position: absolute; 
#       top: 50%;
#       left: 50%;
#       transform: translate(-50%, -50%) scale(0);
#       width: {0}px;
#       height: {1}px;
#       background: url('../images/public/alert.png') no-repeat center center;
#       background-size: contain;
#     }}

#     #app #alert.active{{
#       transition: all .3s;
#       transition-timing-function: cubic-bezier(0, 1.23, 0.84, 1.01);
#       transform: translate(-50%, -50%) scale(1);
#     }}""".format(width, height), interval=0.03)

# import pyautogui

# import pynput
# import pyautogui

# def on_activate():
#   pyautogui.prompt('aaa')
#   print('hello')
  # print('skajfdlajsd')
#   posi = pyautogui.position()
#   pyautogui.click(posi)

#   if pyautogui.confirm('are you sure?') == 'OK':
#     pyautogui.write("""
# #app #alert{
#   position: absolute; 
#   top: 50%;
#   left: 50%;
#   transform: translate(-50%, -50%) scale(0);
#   width: 7.67rem;
#   height: 5.86rem;
#   background: url('../images/public/alert.png') no-repeat center center;
#   background-size: contain;
# }

# #app #alert.active{
#   transition: all .3s;
#   transition-timing-function: cubic-bezier(0, 1.23, 0.84, 1.01);
#   transform: translate(-50%, -50%) scale(1);
# }
#     """, interval=0.03)

# def for_can(f):
#   return lambda k: f(l.canonical(k))

# # 定义热键
# hotkey = pynput.keyboard.HotKey(
#   pynput.keyboard.HotKey.parse('<ctrl>+<alt>+h'),
#   on_activate
# )

# # 监听热键
# with pynput.keyboard.Listener(
#   on_press=for_can(hotkey.press),
#   on_release=for_can(hotkey.release)
# ) as l:
#   l.join()

# 如何监听自定义按键
# def press(key):
#   print(key)

# with pynput.keyboard.Listener(on_press=press) as listener:
#   listener.join()

# git好卡，
# 坚持一个原则，理解为最重要的事

# git 是用C开发的，就够了，Git分布式版本控制系统，集中式版本控制系统

"""
git init 初始化仓库
git config --global user.name  查看当前全局使用的git名
git config --global user.email 查看当前全局使用的email
git status 查看当前状态
git diff 查看版本具体差异
git add 添加文件到暂存区
git commit -m <msg> 提交文件
git log 查看历史记录
git log --pretty=oneline 美化版本查看历史记录

通过版本回退
git reset --hard HEAD^
在window平台，^会被当成换行符
导致在命令行中 
git reset --hard HEAD^ 中的^被忽略掉了，
以下几种解决方式
git reset --hard "HEAD^"
git reset --hard HEAD^^
git reset --hard HEAD~ 或者是 git reset --hard HEAD~1
~后面的数字表示回退几，默认就是1
git reflog : 后悔药(查看命令历史，貌似是版本回退的命令历史)

git log 查看历史
git reflog 查看未来

git 的核心，分布式版本控制系统，
工作区和暂存区
git 还有分支master 默认就是master

git 难点就是分支上，还有HEAD指针
git branch

前面的git 2步曲，
git add 执行的就是把文件添加到暂存区
git commit 执行的就是把暂存区的文件提交到当前分支

git 跟踪并管理的是修改，而不是文件

git checkout -- <file> 丢弃工作区修改

git checkout -- <file> 会让文件回到最近一次add 或 commit的状态

git checkout 分支切换命令
git rm 删除命令

我也修改了文件
git push 上传命令

GitHup 就是提供Git仓库托管服务的

由于本地仓库和git远程仓库之间的数据传输时通过ssh加密的
所以需要设置 ssh-keygen -t rsa -C ‘youremail@exmaple.com’

用户主目录找到这个文件夹 .ssh 
C/user/Adxxx/.ssh

id_rsa 私钥
id_rsa.pub 公钥

创建和合并分支 分支有什么用

记住因为一次历史事件，默认分支已经从master 变为了 main
分支有什么用 ？
分支有什么用 ？
分支有什么用 ？

？ 为什么要创建分支

下班前 提交更改 git push
上班前 拉取最新 git pull

git checkout -b dev 创建并切换分支
git branch dev
git checkout dev

git merge 合并分支 Fast-forward
git branch -d dev

分支命令到此为止
git checkout -b <name> 创建并切换分支
git branch <name> 创建分支
git checkout <name> 切换分支
git merge 合并分支
git branch -d <name> 删除分支
git branch -D <name> 强制删除分支

git checkout -- <file> 这个是撤销修改 容易混淆需要单独记忆

记录密码
git config  credential.helper store

删除密码
git credential-manager uninstall

.git 中的config 文件夹， 多了个 helper

git pull origin main 
git push origin main

查看分支合并情况
git log --graph --pretty=oneline --abbrev-commit

解决冲突 就是git最麻烦的一点，这就是分水岭，一部分人停留在了git的初步使用，一个人能用git上传下拉，回退版本，但是一旦
涉及团队协作，就导致冲突，无法解决
git merge 

git 的commit 和 tag
tag就是指向tag的某个指针
是一个容易记住的有意义的名字

跟某个commit绑定在一起


"""

