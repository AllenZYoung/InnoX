from django.db import models


# Create your models here.

class MovieBase(models.Model):
    name = models.CharField(max_length=100, null=False)
    doubanurl = models.CharField(max_length=100, null=False, primary_key=True)
    director = models.CharField(max_length=30, null=False)
    commenturl = models.CharField(max_length=150, null=False)

    class Meta:
        db_table = 'moviebase'

    # tostring
    def __str__(self):
        return 'moviename: %s' % (self.name)
