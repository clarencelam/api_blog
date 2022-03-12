from django.db import models
from datetime import datetime
from django.template.defaultfilters import slugify

class Categories(models.TextChoices):
    INVESTING = 'investing'
    SAVING = 'saving'
    EARNING = 'earning'
    MISC = 'misc'


class BlogPost(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField()
    category = models.CharField(max_length=50, choices=Categories.choices, default=Categories.MISC) 
    thumbnail = models.ImageField(upload_to='photos/%Y/%m/%d/')
    excerpt = models.CharField(max_length=50) # Description that appears on preview
    month = models.CharField(max_length=3)
    day = models.CharField(max_length=2)
    content = models.TextField()
    featured = models.BooleanField(default=False)
    date_created = models.DateTimeField(default=datetime.now, blank=True)

    def save(self, *args, **kwargs):
        original_slug = slugify(self.title) #slugify function we imported will turn title into slug
        
        # Following code is to ensure all slugs are original 
        queryset = BlogPost.objects.all().filter(slug__iexect=original_slug).count() 
        count = 1
        slug = original_slug
        while(queryset):
            slug = original_slug + '-' + str(count)
            count += 1
            # gets slug name first-blog-post-1
            queryset = BlogPost.objects.all().filter(slug__iexect=slug).count()
            # if name exists already, tries next slug name first-blog-post-2
        self.slug = slug

        if self.featured:
            try:
                 temp = BlogPost.objects.get(featured=True)
                 if self!= temp:
                     temp.featured = False
                     temp.save()
            except BlogPost.DoesNotExist:
                pass
        super(BlogPost, self).save(*args, **kwargs)

    def __str__(self):
        return self.title