#-*- encoding:utf-8 -*-
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from Summary.util import *
from Summary.models import Documents
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger

# 从数据库中读取所有数据
def index(request):
    docs = Documents.objects.all()
    paginator = Paginator(docs,10)  #一页显示10条数据
    page = request.GET.get('page') #获取页码
    if page:
        article_list = paginator.page(page)
    else:
        article_list = paginator.page(1)
    try:
        customer = paginator.page(page)
    except PageNotAnInteger:
        customer = paginator.page(1)
    except EmptyPage:
        customer = paginator.page(paginator.num_pages)
    return render(request, 'index.html', {'cus_list': customer, 'articles': article_list})

@csrf_exempt
def upload(request):
    if request.method == 'POST':
        upload_user = request.POST.get("upload_user")  # 上传者
        keywords = ""  # 关键词
        type = request.POST.get("category")  # 类别
        f = request.FILES.get('file')  # 文件
        size = int(request.POST.get("size")) #文件大小，单位为字节
        docname = f.name  # 文件名
        if len(Documents.objects.filter(docname = docname))>=1:
            return HttpResponse("fileExist")
        else:
            try:
                # doc = Documents(docname = docname,file=f)
                # doc.save()
                # doc = Documents.objects.get(docname = docname)
                # handle_uploaded_file(f)
                doc = Documents(docname=docname,type=type, size = get_FileSize(size),upload_user =upload_user, file=f)
                doc.save()
                return HttpResponse("uploadsuccess")
            except:
                return HttpResponse("fail")
    return render(request,'upload.html')

@csrf_exempt
def download(request):
    if request.method == "POST":
        try:
            filename = request.POST.get('name')
            # 获取文件路径
            source = getPath(filename)
            import tkinter as tk
            from tkinter import filedialog

            root = tk.Tk()
            root.withdraw()

            target = filedialog.askopenfilename()

            return HttpResponse("success")
        except:
            return HttpResponse("fail")
    return HttpResponseRedirect("/summary/index")

@csrf_exempt
def delete(request):
    if request.method == "POST":
        try:
            filename = request.POST.get('name')
            # 删除数据库记录
            Documents.objects.filter(docname = filename).delete()
            # 删除文件
            # delete_file(filename)
            return HttpResponse("success")
        except:
            return HttpResponse("fail")
    return HttpResponseRedirect("/summary/index")

@csrf_exempt
def generate(request,docname):
    path = getPath(docname)
    raw = ''
    summarization = ''
    idx = 1 # 句子编号
    num = 3 # 生成文摘句子数量
    with open(path, 'r',encoding='utf-8') as file:
        for line in file:
            raw += line
    for item in getSummarization(path,num):
        summarization += str('第'+str(idx)+'句：'+item['sentence']+'\n\n')
        idx += 1
    return render(request,"generate.html",{'raw':raw,'summarization':summarization})

def result(request):
    return render(request,"result.html")