from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Todo(models.Model):

    title = models.CharField(max_length=255)
    description = models.TextField()
    completed = models.BooleanField(default=False)
    user = models.ForeignKey(User,default=False,on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_date']

    def __str__(self):

        return self.title
