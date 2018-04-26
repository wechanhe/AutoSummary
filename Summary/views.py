#-*- encoding:utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from Summary.util import *
from Summary.models import Documents


# Create your views here.
def index(request):
    return render(request,'index.html')

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

def delete(request):
    return HttpResponseRedirect(request,'delete.html')
