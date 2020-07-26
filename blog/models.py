import uuid
from django.db import models
from django.urls import reverse


class Blog(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    title = models.CharField(max_length=255)
    pub_date = models.DateTimeField(auto_now=False, auto_now_add=False)
    body = models.TextField()
    image = models.ImageField(
        upload_to="images/", 
        height_field=None, 
        width_field=None, 
        max_length=None
        )

    class Meta:
        indexes = [
            models.Index(fields=['id'], name='id_index'),
        ]
        verbose_name = ("Blog")
        verbose_name_plural = ("Blogs")

    def summary(self):
        return self.body[:100]

    def pretty_pub_date(self):
        return self.pub_date.strftime("%d %b, %Y")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("blog_detail", kwargs={"pk": self.pk})

