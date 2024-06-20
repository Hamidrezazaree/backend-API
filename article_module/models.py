from django.db import models

class Article(models.Model):
    title = models.CharField(max_length= 100 , verbose_name='عنوان مقاله')
    author = models.CharField(max_length= 100 , verbose_name= 'نویسنده')
    create_at = models.DateTimeField(auto_now_add=True,verbose_name='ساخته شده در')
    update_at = models.DateTimeField(auto_now=True, verbose_name='آپدیت شده در')

    def __str__(self):
        return f'{self.title[:10]}...'

    class Meta:
        verbose_name = "مقاله"
        verbose_name_plural = "مقالات"

