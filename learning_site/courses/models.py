from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Course(models.Model): #extends Model class
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    
    def __str__(self):
        return self.title

#foreign key used - each course has many steps

class Step(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    content = models.TextField(blank=True, default='') #additional step adding default to resolve migrations errors
    order = models.IntegerField(default=0)
    course = models.ForeignKey(Course)

    class Meta:#ADDED FOR REORDERING CHECK as per the order entered in admin
        ordering = ['order',]
    
    def __str__(self):
        return self.title