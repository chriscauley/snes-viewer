from django.conf import settings
from django.db import models
from .dread import process_screenshot

import os

_choices = lambda l: zip(l,l)

class World(models.Model):
  name = models.CharField(max_length=128)
  slug = models.CharField(max_length=128)
  __str__ = lambda self: self.name


def default_data():
  return { 'world': { 'xy': [0, 0] } }


class Zone(models.Model):
  class Meta:
    ordering = ('name',)
  __str__ = lambda self: self.name
  name = models.CharField(max_length=128)
  slug = models.CharField(max_length=128)
  world = models.ForeignKey(World, models.CASCADE)

  data = models.JSONField(default=default_data, blank=True)

  def get_image_path(self, ext='png'):
    return os.path.join(settings.MEDIA_ROOT, f'dread_zones/{self.id}-{self.slug}.{ext}')
  def get_image_url(self, ext='png'):
    return os.path.join(settings.MEDIA_URL, f'dread_zones/{self.id}-{self.slug}.{ext}')


class Room(models.Model):
  world = models.ForeignKey(World, models.SET_NULL, null=True, blank=True)
  zone = models.ForeignKey(Zone, models.SET_NULL, null=True, blank=True)
  name = models.CharField(max_length=128, null=True, blank=True)
  key = models.CharField(max_length=128, null=True, blank=True)
  sprite_ids = models.JSONField(default=list, blank=True)
  data = models.JSONField(default=dict, blank=True)
  __str__ = lambda self: f'{self.name or "unnamed"} - ({self.key})'


class Item(models.Model):
  room = models.ForeignKey(Room, models.CASCADE)
  zone = models.ForeignKey(Zone, models.SET_NULL, null=True, blank=True)
  data = models.JSONField(default=dict, blank=True)

class Character(models.Model):
  letter = models.CharField(max_length=1, blank=True, default='')
  image = models.ImageField(upload_to="smile_characters")


class Sprite(models.Model):
  """
  A sprite from the smile imports used to match various blocks.
  """
  TYPES = _choices(['item', 'map', 'unknown'])
  layers = models.JSONField(default=list)
  worlds = models.ManyToManyField(World)
  name = models.CharField(max_length=32, null=True, blank=True)
  # TODO is dhash always a number? if so might be better as big int
  dhash = models.CharField(max_length=24)
  image = models.ImageField(upload_to="smile_sprites")
  type = models.CharField(max_length=16, choices=TYPES, default='unknown')


class Entity(models.Model):
  TYPES = _choices(['item', 'environment', 'enemy', 'door', 'station', 'unknown'])


class Screenshot(models.Model):
  world = models.ForeignKey(World, models.SET_NULL, null=True, blank=True)
  zone = models.ForeignKey(Zone, models.SET_NULL, null=True, blank=True)
  original = models.ImageField(upload_to="screenshots")
  output = models.ImageField(upload_to="output", null=True, blank=True)
  data = models.JSONField(default=dict, blank=True)

  @property
  def original_url(self):
    return self.original and self.original.url

  def save(self, *args, **kwargs):
    super().save(*args, **kwargs)
    if self.id and not self.output and self.original:
      process_screenshot(self)

  def reprocess(self):
    self.output = None
    self.save()


class Channel(models.Model):
  SOURCES = _choices(['youtube'])
  source = models.CharField(max_length=16, choices=SOURCES, default="youtube")
  external_id = models.CharField(max_length=24)
  name = models.CharField(max_length=30)
  icon = models.ImageField(upload_to="channel_icons")
  __str__ = lambda self: self.name


class Video(models.Model):
  class Meta:
    ordering = ('order',)
  SOURCES = _choices(['youtube'])
  source = models.CharField(max_length=16, choices=SOURCES, default="youtube")
  thumbnail = models.ImageField(upload_to="video_thumbnails")
  external_id = models.CharField(max_length=24)
  title = models.CharField(max_length=255)
  label = models.CharField(max_length=64)
  channel = models.ForeignKey(Channel, models.CASCADE)
  data = models.JSONField(default=dict, blank=True)
  world = models.ForeignKey(World, models.CASCADE)
  order = models.IntegerField(default=0)
  __str__ = lambda self: self.title

  @property
  def channel_name(self):
    return self.channel.name

  @property
  def channel_icon(self):
    return self.channel.icon.url

  @property
  def thumbnail_url(self):
    return self.thumbnail.url