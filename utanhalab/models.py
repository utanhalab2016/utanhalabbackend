from django.db import models
class PrincipalModel(models.Model):
    calendario = models.CharField(max_length=200)
    quantidade =  models.IntegerField()

    def __str__(self):
        return self.calendario

