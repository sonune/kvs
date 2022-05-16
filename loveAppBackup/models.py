from django.db import models

# Create your models here.

class Reply_of_Massage(models.Model):
    name = models.CharField(max_length=122, default="unable to retrive", null=True, blank=True)
    date = models.CharField(max_length=122, default="unable to retrive",)
    mymassage = models.TextField()
    replay = models.TextField( null= True, blank=True)

    def register(self):
        return self.save()
    def __str__(self):
        return self.name
    



