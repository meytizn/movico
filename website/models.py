from django.db import models

class Contact(models.Model):
  name=models.CharField( max_length=80 , blank=True ,null=True)
  email=models.EmailField( max_length=254, blank=False ,null=False)
  subject=models.CharField( max_length=255 , blank=True ,null=True)
  message=models.TextField()
  updated_time=models.DateTimeField( auto_now=True, auto_now_add=False)
  created_time=models.DateTimeField( auto_now=False, auto_now_add=True)

  def __str__(self):
      return self.email

  class Meta:
    ordering=['-created_time',]
  
 
  
