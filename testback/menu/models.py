from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=15)
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='link_parent')
    level = models.IntegerField(default=1)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('get_id', kwargs={"id": self.pk})

    def get_children(self):
        return Category.objects.filter(parent__id=self.pk)

    def is_have_parent(self):
        return self.parent

    def is_have_children(self):
        return Category.objects.filter(parent__id=self.id)
