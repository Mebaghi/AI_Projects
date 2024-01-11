from django.db import models


class book(models.Model):
    onvan = models.CharField(max_length=128)
    nevisande = models.CharField(max_length=128)
    tedade_safahat = models.CharField(max_length=128)
    tozih = models.TextField()
    
    def __str__(self) -> str:
        return self.onvan