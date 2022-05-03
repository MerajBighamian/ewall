from django.db import models

# Create your models here.


class Tags(models.Model):
    """
    for specify tags for posts  
    """

    # title for tag
    title = models.CharField('عنوان برچسب', max_length=200,null=False)

    # show title of tag (in django admin instead show object name (machine readable))
    def __str__(self):
        return self.title

class Categories(models.Model):

    """
    specify categories for posts 
    """
    # name of ctegories
    name = models.CharField('نام دسته بندی',max_length=200,null=False)

    # foreign key to this model for specify parent category
    parent_category = models.ForeignKey("Categories", verbose_name="دسته بندی والد", on_delete=models.PROTECT,blank=True)

    # create time of Category
    created_at = models.DateTimeField(auto_now_add=True)

    # update time of Category
    updated_at = models.DateTimeField(auto_now=True)

    # show name of Categories (in django admin instead show object name (machine readable))
    def __str__(self):
        return self.name
