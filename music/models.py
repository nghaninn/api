from django.db import models


class Songs(models.Model):
    # song id
    id = models.AutoField(primary_key=True)
    # song title
    title = models.CharField(max_length=255, null=False)
    # name of artist or group/band
    artist = models.CharField(max_length=255, null=False)
    # description of song
    description = models.CharField(max_length=255, null=True, default="")

    # owner = models.ForeignKey('auth.User', related_name='snippets', on_delete=models.CASCADE)

    def __str__(self):
        return "{} : {} - {} --> {}".format(self.id, self.title, self.artist, self.description)
