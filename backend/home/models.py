from django.db import models

class BlogPost(models.Model):
    title = models.CharField(max_length=255)  
    description = models.TextField(blank=True) # Optional description field 
    image = models.ImageField(default=" ") # Cover Photo for album 
    # Featured check box 
    featured = models.BooleanField(help_text="Check this box if you want the images to render in the featured work carousel.") 

    def __str__(self):
        return self.title

class Image(models.Model):
    caption = models.CharField(max_length=255, blank=True) # Optional captions 
    posts = models.ForeignKey(BlogPost, default='', related_name='images_post', on_delete=models.CASCADE)
    images = models.FileField(upload_to='images/')

    def __str__(self):
        return self.posts.title # Blog post title, not post caption

