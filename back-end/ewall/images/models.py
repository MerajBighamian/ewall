from django.db import models
from post.models import Post
from categories_and_tags.models import Categories
# Create your models here.
class Covers(models.Model):
    image = models.ImageField('تصویر مورد نظر', upload_to='media/images',max_length=None)
    models.ForeignKey(Post, verbose_name='تصویر آگهی', on_delete=models.CASCADE)

