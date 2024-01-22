from django.db import models
from django.contrib.auth.models import User
#User model takes care of all the user information and this is how django by default handles the authentication

# Create your models here.

class Task(models.Model):
    #One to many relation (one user can have many items) which can be set with the foreign key model
    #cascade: on deleting the user, the task would also delete
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    title = models.CharField(max_length=200)
    description = models.TextField(null=True,blank=True)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['complete']