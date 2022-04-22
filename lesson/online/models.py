from django.db import models

class Regions(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.id} | {self.name}"

class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.id} | {self.name}"

class News(models.Model):
    region = models.ForeignKey(Regions, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=150)
    image = models.ImageField(upload_to='media/news',null=True, blank=True)
    description = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)

    @property
    def imageURL(self):
        try:
            return self.image.url
        except:
            pass
    def __str__(self):
        return f"{self.id} | {self.title} | {self.created_time}"
