from django.db import models

# Create your models here.

class Topic(models.Model):
    """用户学习的主题"""
    text = models.CharField(max_length=20)              # 文本字符串
    date_added = models.DateTimeField(auto_now_add=True) # 时间字符串

    def __str__(self):
        """返回模型的字符串表示"""
        return  self.text

'''
要记录学到的国际象棋和攀岩知识，需要为用户可在学习笔记中添加的条目定义模型。
每个条目都与特定主题相关联，这种关系被称为多对一关系，即多个条目可关联到同一个 主题。
'''
class Entry(models.Model):
    """学到的有关某个主题的具体知识"""
    topic = models.ForeignKey(Topic,on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        """返回模型字符串表示"""
        return self.text[:50]+"..."