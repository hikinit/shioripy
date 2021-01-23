from django.db import models


class MediaType(models.TextChoices):
    WEB_NOVEL = "Web Novel"
    LIGHT_NOVEL = "Light Novel"
    COMIC = "Comic"
    CARTOON = "Cartoon"


class Series(models.Model):
    title = models.CharField(max_length=200)
    media = models.CharField(choices=MediaType.choices, max_length=30)

    def __str__(self):
        return f"{self.title} ({self.media.value})"
