from email.policy import default
from pickle import FALSE
from unicodedata import name
from django.contrib.auth.models import BaseUserManager, AbstractUser
from django.db import models

# Create your models here.


class SocialUserManager(BaseUserManager):

    def create_user(self, email, password=None, **kwargs):
        user = self.model(email=email, is_leader=True, **kwargs)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **kwargs):
        user = self.model(email=email, is_staff=True,
                          is_superuser=True, **kwargs)
        user.set_password(password)
        user.save()
        return user


class Deparment(models.Model):
    name = models.CharField(max_length=45)


class Municipality(models.Model):
    name = models.CharField(max_length=45)
    deparment = models.ForeignKey(
        Deparment, related_name='deparment_municipalities', on_delete=models.CASCADE)


class Commune(models.Model):
    name = models.CharField(max_length=45)
    municipality = models.ForeignKey(
        Municipality, related_name="municipality_communes", on_delete=models.CASCADE)


class Neighborhood(models.Model):
    name = models.CharField(max_length=45)
    commune = models.ForeignKey(
        Commune, related_name="commune_neighborhoods", on_delete=models.CASCADE)


class BasicData(AbstractUser):
    username = None
    email = models.EmailField('email address',  unique=True, db_index=True)
    phone = models.CharField(max_length=12, blank=True, null=True)
    document = models, models.CharField(max_length=15)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = SocialUserManager()

    def __str__(self):
        return self.email


class Admin(models.Model):
    name = models.CharField(max_length=25)
    basic_data = models.OneToOneField(BasicData,  on_delete=models.CASCADE)


class Leader(models.Model):
    admin = models.ForeignKey(
        Admin, related_name="admin_leaders", on_delete=models.CASCADE)
    image = models.CharField(max_length=500)
    basic_data = models.OneToOneField(BasicData,  on_delete=models.CASCADE)

class PollingStation(models.Model):
    name = models.CharField(max_length=45)
    address = models.CharField(max_length=50, blank=True, null=True)
    municipality = models.ForeignKey(
        Municipality, related_name="municipality_polling_stations", on_delete=models.CASCADE)


class Voter(models.Model):
    polling_station = models.ForeignKey(
        PollingStation, related_name="polling_station_voters", on_delete=models.CASCADE)
    basic_data = models.OneToOneField(BasicData,  on_delete=models.CASCADE)
    leader = models.ForeignKey(Leader, related_name="leader_voters", on_delete=models.CASCADE)
    neighborhood = models.ForeignKey(
        Leader, related_name="neighborhood_voters", on_delete=models.CASCADE)
    address = models.CharField(max_length=50, blank=True, null=True)
