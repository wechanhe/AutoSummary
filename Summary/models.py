from datetime import datetime

from django.db import models
from django.db.models.signals import post_delete
import os

# class Column(models.Model):
#     name = models.CharField('栏目名称', max_length=256)
#     slug = models.CharField('栏目网址', max_length=256, db_index=True)
#     intro = models.TextField('栏目简介', default='')
#
#     def __str__(self):
#         return self.name
#
#     class Meta:
#         verbose_name = '栏目'
#         verbose_name_plural = '栏目'
#         ordering = ['name']  # 按照哪个栏目排序


class Documents(models.Model):
    id = models.AutoField(primary_key=True,editable=False)
    docname = models.CharField(max_length=50)  #文件名
    keywords = models.TextField(max_length=100,default='')  #关键字
    downloads = models.IntegerField(default=0)  #下载次数
    size = models.FloatField(default=0.0)  #文件大小
    create_time = models.DateTimeField(default=datetime.now)  # 文件上传时间
    update_time = models.DateTimeField(default=datetime.now)  # 文件最后修改时间
    type = models.CharField(max_length=20,default='未知')
    upload_user = models.CharField(max_length=20,default='未知')  # 上传者
    file = models.FileField(upload_to='./Summary/data/')


    def __unicode__(self):
        return self.file.name

    class Meta:
        ordering = ['-pk']


def delete_file(sender, **kwargs):
    patch = kwargs['instance']
    os.remove(patch.file.path)

post_delete.connect(delete_file, sender=Documents)