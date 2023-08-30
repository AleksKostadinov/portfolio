from django.db import models
from django.utils.text import slugify
from ckeditor_uploader.fields import RichTextUploadingField


class Work(models.Model):
    headline = models.CharField(max_length=50)
    sub_headline = models.CharField(max_length=100, null=True, blank=True)
    text = models.CharField(max_length=100, null=True, blank=True)
    image = models.ImageField(upload_to='images', null=True, blank=True)
    active = models.BooleanField(default=False)
    slug = models.SlugField(null=True, blank=True)
    link = models.URLField(null=True, blank=True)
    favourite = models.BooleanField(default=True)
    thumbnail = models.ImageField(null=True, blank=True, upload_to="images")
    body = RichTextUploadingField(null=True, blank=True)

    def __str__(self):
        return self.headline

    def save(self, *args, **kwargs):

        if self.slug is None:
            slug = slugify(self.headline)

            has_slug = Work.objects.filter(slug=slug).exists()
            count = 0
            while has_slug:
                count += 1
                slug = slugify(self.headline) + '-' + str(count)
                has_slug = Work.objects.filter(slug=slug).exists()

            self.slug = slug

        super().save(*args, **kwargs)


class Certificate(models.Model):
    class Meta:
        ordering = ['date']

    name = models.CharField(max_length=50)
    description = models.CharField(max_length=300)
    issued_from = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    document = models.FileField(upload_to='certificates/')
    date = models.DateField(blank=True, null=True)
    grade = models.FloatField()
    link = models.URLField(blank=True)

    def __str__(self):
        return self.name
