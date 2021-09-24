from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=200, help_text='maqola, video, diser, prezin')
    slug = models.CharField(max_length=100, help_text='root')

    def __str__(self):
        return self.title


class Material(models.Model):
    category = models.ForeignKey(Category, blank=False, null=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=200, help_text='maqola nomi')
    file = models.FileField(upload_to='files/', help_text='faylni tanlang')
    description = models.TextField(help_text='bu fay haqida')
    price = models.PositiveIntegerField(null=True)
    slug = models.CharField(max_length=100, blank=False, null=False, help_text='root')

    def __str__(self):
        return self.title


class Customer(models.Model):
    full_name = models.CharField(max_length=100, blank=False, null=True)
    job = models.CharField(max_length=200, blank=False)
    message = models.TextField()
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.full_name


class GetInTouch(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone_number = models.CharField(max_length=13, null=True)
    message = models.TextField()

    def __str__(self):
        return self.name