from django.db import models


class Profile(models.Model):
    full_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=13)
    age = models.PositiveIntegerField()
    country = models.CharField(max_length=255, default="Uganda")
    location = models.CharField(max_length=255, default="Kampala")
    experience = models.PositiveIntegerField(default=3)


class Skill(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
