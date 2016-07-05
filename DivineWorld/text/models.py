

# Create your models here.

from django.db import models  
from django.utils import timezone
from django.core.urlresolvers import reverse

class Religion(models.Model):
    religionID = models.CharField(max_length=10, primary_key=True)
    religionName = models.CharField(max_length=200)
    religionHistory = models.TextField(default="No Content")

    def __str__(self):
        return self.religionName

class Arti(models.Model):
    religionID = models.ForeignKey(Religion, on_delete=models.CASCADE)
    artiID = models.CharField(max_length=5, unique=True)
    artiName = models.CharField(max_length=200)
    artiText = models.TextField()
    class Meta:
        unique_together = (('religionID', 'artiID'),)

    def __str__(self):
        return self.artiName
        
class Mantra(models.Model):
    religionID = models.ForeignKey(Religion, on_delete=models.CASCADE)
    mantraID = models.CharField(max_length=5, unique=True)
    mantraName = models.CharField(max_length=200)
    mantraText = models.TextField()
    class Meta:
        unique_together = (('religionID', 'mantraID'),)

    def __str__(self):
        return self.mantraName

class Hits(models.Model):
    contentID = models.ForeignKey(Mantra, Arti)
    created = models.DateTimeField(default=timezone.now())
    count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.contentID

class Post(models.Model):
    title = models.CharField(max_length=500)
    content = models.TextField()
    updates = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    def _str_(self):
        return self.title   

   # def get_absolute_url(self):
    #    return reverse("blog:detail", kwargs={"id": self.id})
        #return "/posts/detail/%s/" %(self.id)
