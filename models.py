from _future_ import unicode_literals

# Create your models here.
from django.db import models





# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_date = models.DateTimeField(auto_now_add=False, auto_now=True)
   
  
  
    def _unicode_(self):
        return self.title

    def _str_(self):
        return self.title

