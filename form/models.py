from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=100)
    # name.widget.attrs.update({'class' : 'name'})
    email = models.EmailField(max_length=100)  
    text = models.TextField(max_length=10000)
     
    def __str__(self):
        return self.name + ' ' + 'said ' + self.text 
