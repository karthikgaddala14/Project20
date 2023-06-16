from django.db import models

# Create your models here.
class jobs(models.Model):
    jid:models.IntegerField(primary_key=True)
    Tittle:models.CharField(max_length=20)
    Skills:models.CharField(max_length=200)
    Disprestion:models.IntegerField(max_length=200)
