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


class Certificate(models.Model):
    
    class Meta:
        ordering = ['date']
    
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=300)
    issued_from = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    document = models.FileField(upload_to='document')
    date = models.DateField(blank=True, null=True)
    grade = models.FloatField()
    link = models.URLField(blank=True)
    
    def __str__(self):
        return self.name
    