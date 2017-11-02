from django.shortcuts import render
from blog_test_web.models import ItemInfo

from django.core.paginator import Paginator

# Create your views here.

def index(request):
    limit = 4
    item_info = ItemInfo.objects[:1]
    paginator = Paginator(item_info,limit)
    page = request.GET.get('page',1)
    loaded = paginator.page(page)

    context ={   # 模拟一个假的数据库.models层相当于一个数据库的代理，把数据库内容映射到templates模版层中，
        'ItemInfo':loaded

    }
    return render(request, 'index.html',context)  # 调用
