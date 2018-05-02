# AutoSummary 系统功能说明以及实现细节

## 系统用到的技术

* 前端：页面设计使用Bootstrap3，前端用到了Jquery、Ajax等技术
* 后台：使用基于Python的web开发框架Django，版本是2.0.4，Python的版本是3.6
* 开发工具：Pycharm-2017

## 首页

### 实现的功能

* 列表显示文章
  列表主要是显示了存储文件的数据库表信息。
  数据库表设计如下：![avatar]
  [avatar]: https://github.com/wechanhe/AutoSummary/tree/master/Summary/static/pictures/数据库表设计.PNG

* 分页
  考虑到上传的文件数量可能会有点大，为了更好的在首页显示文章列表，结合使用了Django自带的分页模块**django.core.paginator**和Bootstrap的分页样式
  来实现本系统的列表分页显示功能。该模块代码如下：
 ```
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
 ```
* 删除文件
  用户在首页点击删除按钮时，前端获取文件名称并传到服务器，然后服务器通过文件名将文件从服务器删除

### 文件上传页
* 上传文件
  文件上传通过一个表单的形式完成。用户可以输入一些信息，选择本地要上传的文件，点击上传时，服务器会对文章进行分析，提取关键词，然后创建数据库对象将文件描述信息写入数据库。

### 文摘生成页
* 读取文件内容
  页面加载时读取文件，用一个textarea显示文件内容。用户选择句子数量，点击生成文摘，前台通过ajax请求获取文章摘要，在右侧textarea显示文摘内容.

* 关于算法
  算法用的是**TextRank**,这个算法参考PageRank算法的思想，通过对文本进行分词和分句构造图模型，利用投票机制对文本中的重要成分进行排序, 仅利用单篇文档本身的信息即可实现关键词提取、文摘。算法详情请参考[这篇文档](http://www.cnblogs.com/chenbjin/p/4600538.html)

