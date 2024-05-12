from django.db import models

class Contact_info(models.Model):
    location = models.CharField(max_length=500, default='UZB')
    name = models.CharField(max_length=100)
    email = models.EmailField()
    number = models.CharField(max_length=100)


class Picture(models.Model):
    image = models.ImageField(upload_to='picture/')
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)

class Result(models.Model):
    complated = models.IntegerField()
    customer = models.IntegerField()
    awward = models.IntegerField()
    experince = models.IntegerField()

class Offer(models.Model):
    icon = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    discription = models.TextField()

class About(models.Model):
    image = models.ImageField(upload_to='about_img/')
    name = models.CharField(max_length=100)
    discription = models.TextField()
    link = models.URLField()

class Servies(models.Model):
    icon = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    discription = models.TextField()

class Projcet (models.Model):
    image = models.ImageField(upload_to='project_img/')
    title = models.CharField(max_length=100)
    types = models.CharField(max_length=100)

class Position(models.Model):
    name = models.CharField(max_length=100)

class Register(models.Model):
    full_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    position = models.ForeignKey(Position, on_delete=models.PROTECT, default='.')
    message = models.CharField(max_length=100)
    select = models.CharField(max_length=100, default='.')
    
class Blog (models.Model):
    title = models.CharField(max_length=100)
    published_at = models.DateField(auto_now=True)
    poster = models.ImageField(upload_to='blog_img/')
    author = models.CharField(max_length=100)
    discription = models.TextField()

class Feedback(models.Model):
    poster = models.ImageField(upload_to='feedback_img/')
    discription = models.TextField()
    author = models.CharField(max_length=100)
    position = models.ForeignKey(Position, on_delete=models.PROTECT)

class Enter(models.Model):
    herader = models.CharField(max_length=100)
    discription = models.TextField()

    def __str__(self) -> str:
        return self.herader

class AboutUs(models.Model):
    video = models.FileField(upload_to='videos', null=True)
    header = models.CharField(max_length=100)
    discription = models.TextField()

    def __str__(self) -> str:
        return self.header
