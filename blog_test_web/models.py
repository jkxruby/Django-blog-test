from django.db import models
# Create your models here.
from mongoengine import connect

connect('ganji1_db', host='127.0.0.1', port= 27017 )

from mongoengine import *  # 和之前的pymongo相比，mongoengine采用的是面向 对象语言方式交互,* 表示引用所有插件

class ItemInfo(Document):  # 类的命名方式，括号内是它继承的类，面向对象
    title = StringField()
    url = StringField()
    price = IntField()     # 这里的命名必须对应数据库里的命名
    look = StringField()   # 而且，这里必须列出所有数据库的key,否则报错提示某key 不存在
    area = StringField()
    cates = StringField()
    pub_date = StringField()


    meta = {'collection':'new_ganji1'}  # 仅用于调用已存在的数据库，这行就是告诉django，你的数据是从哪里来的，对应哪个collection


for i in ItemInfo.objects[:1]:
    print(i.title,i.url,i.price)
