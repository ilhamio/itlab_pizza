from django.contrib.auth.models import User, AbstractUser
from django.db import models

RANK_CHOICES = ((1, 'Cook'), (2, 'Waiter'), (3, 'Administrator'))


class User(AbstractUser):

    def get_rank(self):
        try:
            rank = self.staff.get_rank
            return rank
        except:
            return 0

    class Meta(AbstractUser.Meta):
        swappable = "AUTH_USER_MODEL"


class Staff(models.Model):
    user = models.OneToOneField(User, related_name='staff', on_delete=models.CASCADE)
    rank = models.IntegerField(choices=RANK_CHOICES, verbose_name='rank')

    @property
    def get_rank(self):
        return self.rank if self.rank else 0
