import os

from django.conf import settings

from Summary.models import Documents

from imp import reload
import sys

def handle_uploaded_file(f):
    try:
        fname = '%s/%s' % (settings.DATA_ROOT, f.name)
        with open(fname, 'wb') as file:
            for chunk in f.chunks():
                file.write(chunk)
        return True
    except:
        return False

def delete_file(filename):
    os.remove(getPath(filename))

def getPath(filename):
    return '%s/%s' % (settings.DATA_ROOT,filename)

def genKeywords(path):
    try:
        reload(sys)
        sys.setdefaultencoding('utf-8')
    except:
        pass

    import codecs
    from textrank4zh import TextRank4Keyword, TextRank4Sentence
    text = codecs.open(path, 'r', 'utf-8').read()
    tr4w = TextRank4Keyword()

    tr4w.analyze(text=text, lower=True, window=2)  # py2中text必须是utf8编码的str或者unicode对象，py3中必须是utf8编码的bytes或者str对象

    return tr4w.get_keyphrases(keywords_num=20, min_occur_num= 2)

    # print( '关键词：' )
    # for item in tr4w.get_keywords(20, word_min_len=1):
    #     print(item.word, item.weight)
    #
    # print()
    # print( '关键短语：' )
    # for phrase in tr4w.get_keyphrases(keywords_num=20, min_occur_num= 2):
    #     print(phrase)
    #
    # tr4s = TextRank4Sentence()
    # tr4s.analyze(text=text, lower=True, source = 'all_filters')
    #
    # print()
    # print( '摘要：' )
    # for item in tr4s.get_key_sentences(num=3):
    #     print(item.index, item.weight, item.sentence)  # index是语句在文本中位置，weight是权重
