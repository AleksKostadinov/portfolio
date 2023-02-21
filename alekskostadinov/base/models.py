from django.db import models
from django.utils.text import slugify


class Work(models.Model):
    headline = models.CharField(max_length=50)
    text = models.TextField(max_length=200, null=True, blank=True)
    image = models.ImageField(upload_to='images')
    active = models.BooleanField(default=False)
    slug = models.SlugField(null=True, blank=True)
    link = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.headline

    def save(self, *args, **kwargs):

        if self.slug is None:
            slug = slugify(self.headline)

            has_slug = Work.objects.filter(slug=slug).exists()
            count = 1
            while has_slug:
                count += 1
                slug = slugify(self.headline) + '-' + str(count)
                has_slug = Work.objects.filter(slug=slug).exists()

            self.slug = slug

        super().save(*args, **kwargs)
