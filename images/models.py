from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.contrib.auth import get_user_model

User = get_user_model()


# Create your models here.

class Image(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='images_created')
    title = models.CharField(max_length=225)
    slug = models.SlugField(blank=True)
    url = models.URLField()  # original pic link
    image = models.ImageField(upload_to='images/%Y/%m/%d/')
    description = models.TextField(blank=True)
    users_like = models.ManyToManyField(User, related_name='images_liked', blank=True)
    total_likes = models.PositiveIntegerField(db_index=True, default=0)
    created = models.DateField(auto_now_add=True, db_index=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Image, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('images:detail', args=[self.id, self.slug])

    def __str__(self):
        return self.title
