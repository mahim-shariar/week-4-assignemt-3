from django.db import models



class Category(models.Model):
    category_title = models.CharField(max_length=100)



    def __str__(self):
        return self.category_title