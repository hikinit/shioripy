from uuid import uuid4

from django.db import models
from django_countries.fields import CountryField


class MediaType(models.TextChoices):
    WEB_NOVEL = "Web Novel"
    LIGHT_NOVEL = "Light Novel"
    COMIC = "Comic"
    CARTOON = "Cartoon"


MEDIA_LOCALIZATION = {
    MediaType.CARTOON: {
        "JP": "Anime",
    },
    MediaType.COMIC: {
        "JP": "Manga",
        "KR": "Manhwa",
    },
}


class Series(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    title = models.CharField(max_length=200)
    media = models.CharField(choices=MediaType.choices, max_length=30)
    origin = CountryField()

    def __str__(self):
        return f"{self.title} ({self.media_l10n})"

    @property
    def media_l10n(self):
        return MEDIA_LOCALIZATION.get(self.media).get(self.origin, self.media)
