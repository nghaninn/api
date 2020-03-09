from rest_framework import serializers
from .models import Songs
import logging


class SongsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Songs
        fields = ("id", "title", "artist", "description")
        read_only_fields = ["id"]
        # read_only_fields = ["title", "artist"]

    def validate(self, value, *args, **kwargs):
        logger = logging.getLogger(__name__)
        logger.info('Goodbye, cruel world!(i)')
        logger.debug("Hey there it works!!(d)")
        logger.info("Hey there it works!!(i)")
        logger.warn("Hey there it works!!(w)")
        logger.error("Hey there it works!!(e)")

        logger.warn(value)
        logger.warn(args)
        logger.warn(kwargs)

        qs1 = Songs.objects.filter(title__iexact=value["title"])
        qs2 = Songs.objects.filter(artist__iexact=value["artist"])

        if self.instance:
            logger.warn("self")
            qs1 = qs1.exclude(id = self.instance.id)
            # qs2 = qs2.exclude(id = self.instance.id)

        if qs1.exists() & qs2.exists():
            raise serializers.ValidationError("{} - {} already exist"
                                              .format(value["title"], value["artist"]))

        return value
