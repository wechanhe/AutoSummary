#-*- encoding:utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt

from Summary.util import *
from Summary.models import Documents

# 从数据库中读取所有数据
def index(request):
    docs = Documents.objects.all()
    return render(request,'index.html',{'docs':docs})

def upload(request):
    if request.method == 'POST':
        f = request.FILES['file']
        if handle_uploaded_file(f) == True:
            keywords = ''
            for kw in genKeywords(getPath(f.name)):
                keywords += '  ' + kw
            doc = Documents(docname = f.name,keywords = keywords,file = f)
            doc.save()
            return HttpResponseRedirect('/summary/index')
        else:
            return HttpResponse('fail')
    return render(request,'upload.html')

@csrf_exempt
def delete(request):
    if request.method == "POST":
        filename = request.POST.get('name')
        # 删除数据库记录
        Documents.objects.filter(docname = filename).delete()
        # 删除文件
        delete_file(filename)
    return HttpResponseRedirect('/summary/index')
