from django.db import models
from django.urls import reverse


class Job(models.Model):
    image = models.ImageField(upload_to='images/', height_field=None, width_field=None, max_length=None)
    summary = models.CharField(max_length=200)
    

    class Meta:
        verbose_name = ("Job")
        verbose_name_plural = ("Jobs")

    def __str__(self):
        return self.summary

    def get_absolute_url(self):
        return reverse("Job_detail", kwargs={"pk": self.pk})

