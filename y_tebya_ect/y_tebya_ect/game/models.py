from django.db import models

from ..users.models import User

class Game(models.Model):
    player1 = models.ForeignKey(User,
                                related_name="%(app_label)s_%(class)s_player1")
    player2 = models.ForeignKey(User,
                                related_name="%(app_label)s_%(class)s_player2")
    player1_score = models.IntegerField(default=0)
    player2_score = models.IntegerField(default=0)
    completed = models.BooleanField(default=False)
