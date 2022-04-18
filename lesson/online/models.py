from django.db import models

class News(models.Model):
    title = models.CharField(max_length=150)
    image = models.ImageField(upload_to='media/news')
    description = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.id} | {self.title} | {self.created_time}"
