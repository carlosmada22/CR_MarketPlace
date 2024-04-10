from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        # the comma , is bc is an iterable template
        ordering = ('name', )
        verbose_name_plural = 'Categories'
    
    def __str__(self) -> str:
        return self.name

class Item(models.Model):
    #CASCADE: when we delete a category, all the items of that category will be deleted
    category = models.ForeignKey(Category, related_name='items', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    #null=True in case the user doesn't wat to provide description for the product
    description = models.TextField(blank=True, null=True)
    price = models.FloatField()
    image = models.ImageField(upload_to='item_images', blank=True, null=True)
    is_sold = models.BooleanField(default=False)
    #link in the db between this item and the user in user table
    created_by = models.ForeignKey(User, related_name='items', on_delete=models.CASCADE) #'items' so we can access the list of items for user.
    #CASCADE: when we delete an user, all the items of that user will be deleted
    created_at = models.DateTimeField(auto_now_add=True) #auto now date and time

    class Meta:
        # the comma , is bc is an iterable template
        ordering = ('name', )

    def __str__(self) -> str:
        return self.name