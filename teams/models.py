from django.db import models

# Create your models here.

class Team(models.Model):
    team_name = models.CharField("This is the eSports team name", max_length=250)
    team_abbreviation = models.CharField("The abbreviation of the team name", max_length=3)
    team_owner = models.CharField("The team owners name", max_length=250)
    team_url = models.CharField("Team's website address", max_length=255)
    team_logo = models.CharField("The team's logo", max_length=255)
    game = (
        ('LOL', 'League of Legends'),
        ('DOTA2', 'Defense of the Ancients'),
    )

