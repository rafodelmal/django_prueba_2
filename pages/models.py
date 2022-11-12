from django.db import models

# Create your models here.

class Block(models.Model):
    index = models.CharField(max_length = 100)
    timestamp = models.DateTimeField(auto_now_add = True, auto_now = False, blank = False)
    proof = models.CharField(max_length = 100)
    previous_hash = models.CharField(max_length = 200) 

    def __str__(self):
        return self.previous_hash
