from django.contrib.auth.models import User 
from django.db import models
from item.models import Item

# Create your models here.

class Conservation(models.Model):
    item = models.ForeignKey(Item, related_name='conservation', on_delete= models.CASCADE)
    members = models.ManyToManyField(User, related_name="conservation")
    created_at = models.DateTimeField(auto_now=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-modified_at',)


class ConversationMessage(models.Model):
    conversation = models.ForeignKey(Conservation, related_name='messages', on_delete= models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, related_name= 'created_message', on_delete= models.CASCADE)