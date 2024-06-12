from django.db import models

#SiteSettings
class SiteSettings(models.Model):
    banner = models.ImageField(upload_to= 'media/site/')
    caption = models.TextField()