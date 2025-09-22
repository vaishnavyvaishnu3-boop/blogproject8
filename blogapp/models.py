from django.db import models

class  register(models.Model):
    name=models.CharField(max_length=200)
    age=models.IntegerField()

    def __str__(self):
        return '{}'.format(self.name)

class logindata(models.Model):
    username=models.CharField(max_length=200)
    email=models.EmailField(max_length=200)
    password=models.IntegerField()

    def __str__(self):
        return '{}'.format(self.username)

class resetpassword(models.Model):
    new_password=models.IntegerField()
    username=models.CharField(max_length=200)

    def __str__(self):
        return '{}'.format(self.new_password)

class profiledata(models.Model):
    First_name=models.CharField(max_length=200)
    Last_name=models.CharField(max_length=200)
    username=models.CharField(max_length=200)
    email=models.EmailField(max_length=200)
    contact_number=models.IntegerField()
    Nationality=models.CharField(max_length=200)
    Pincode=models.IntegerField()
    password=models.IntegerField()

    def __str__(self):
        return '{}'.format(self.First_name)

class correctpassword(models.Model):
    username=models.CharField(max_length=200)
    repassword=models.IntegerField()

    def __str__(self):
        return '{}'.format(self.username)

class profilepicture(models.Model):
    username=models.CharField(max_length=200)
    profile_pic=models.ImageField(upload_to='profilepics/')

    def __str__(self):
        return '{}'.format(self.username)

class postitem(models.Model):
    title=models.CharField(max_length=200)
    content=models.TextField(max_length=5000)
    postimage=models.ImageField(upload_to='postimages/')
    caption=models.CharField(max_length=200)

    def __str__(self):
        return '{}'.format(self.title)

class commentdata(models.Model):
    name=models.CharField(max_length=200)
    email=models.EmailField(max_length=200)
    content=models.TextField(max_length=2000)


    def __str__(self):
        return '{}'.format(self.name)