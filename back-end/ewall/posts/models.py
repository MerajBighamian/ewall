from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from categories_and_tag.models import Tags,Categories

# Create your models here.
class Post(models.Model):
    """
    this is model for Posts in website
    """
    # title of Post
    title = models.CharField('عنوان',max_length=200)

    # detail of Post
    detail = models.TextField('توضیحات',default='توضیحاتی وجود ندارد!')

    # foreign key to User model for specify author of post
    author = models.ForeignKey(User,on_delete=models.CASCADE)

    # contact_details for author of post
    contact_details  = author.name

    #  valid cities for city field
    cities = (
        (1,'بوشهر'),
        (2,'اصفهان'),
        (3,'تهران'),
    )

    # city of Post
    city = models.IntegerField('شهر شما : ', choices=cities)

    # description of Post for show to search engine and etc .
    description = models.CharField(max_length=200,default='توضیحات') #not show to user 

    # slug of Post for show in url bar
    slug = models.SlugField()

    # create time of Post
    created_at = models.DateTimeField(auto_now_add=True)

    # update time of Post
    updated_at = models.DateTimeField(auto_now=True)

    # publishe time of Post (default value is present time (object create in database))
    published_at = models.DateTimeField(default=timezone.now,null=True)

    # status of Post (default False)
    status = models.BooleanField('نمایش داده شود؟',default=False)

    # ManyToManyField for specifies tags of post
    tags = models.ManyToManyField(Tags) # for show Tags

    # ManyToManyField for specifies categories of post
    categories = models.ManyToManyField(Categories, blank = True)

    # ManyToManyField for specifies related_post of post
    related_post = models.ManyToManyField('Post',blank=True)

    # show title of post (in django admin instead show object name (machine readable))
    def __str__(self):
        return self.title
    


class Comments(models.Model):
    """
        specify table for all comments of posts
    """

    # title of Post
    title = models.CharField('عنوان نظر',max_length=200,null=True)

    # body of Post
    body = models.TextField("متن نظر")

    #  foreign key to User model for specify author of comment
    author = models.ForeignKey(User, verbose_name="نویسنده", on_delete=models.CASCADE)

    #  foreign key to Post model for specify post of comment
    post_id = models.ForeignKey(Post, verbose_name="پست مورد نظر", on_delete=models.CASCADE)

    parent_id = models.ForeignKey('Comments',on_delete=models.CASCADE,blank=True,null=True)    

    # create time of comment
    created_at = models.DateTimeField(auto_now_add=True)

    # update time of comment
    updated_at = models.DateTimeField(auto_now=True)

    # verification status of comments
    verification = models.BooleanField('نمایش داده شود ؟ ' , default=False)

    # show title of comment (in django admin instead show object name (machine readable))
    def __str__(self):
        return self.title


