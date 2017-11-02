from django.shortcuts import render
from blog_test_web.models import ItemInfo

# Create your views here.

def index(request):
    item_info = ItemInfo.objects[:1]
    context ={   # 模拟一个假的数据库.models层相当于一个数据库的代理，把数据库内容映射到templates模版层中，
        'title': item_info[0].title,
        'url': item_info[0].url,
        'price': item_info[0].price

    }
    return render(request, 'index.html',context)  # 调用
