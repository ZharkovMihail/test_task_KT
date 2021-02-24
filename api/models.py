from django.db import models


class Picture(models.Model):
    upload = models.ImageField(upload_to='uploads/')
    tags = models.ManyToManyField('Tag', blank=True, related_name='tag_list')

    def __str__(self):
        return '{}'.format(self.pk)


class Tag(models.Model):
    title = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return '{}'.format(self.title)
