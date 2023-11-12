from django.db import models

# Create your models here.
# Create model for Post.
class Post(models.Model): # create model
    text = models.TextField() # Define attribute text (means that all posts will have attribute text)

    def __str__(self):
        return self.text[:50]
