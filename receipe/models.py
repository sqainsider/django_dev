from django.db import models

# Create your models here.


class receipe(models.Model):

    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField()
    youtube = models.ImageField()

    def __str__(self):
        return self.title

    # def get_absolute_url(self):
    #     return reverse("_detail", kwargs={"pk": self.pk})
