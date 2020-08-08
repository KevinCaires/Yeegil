from django.db import models


class EmailList(models.Model):
    email = models.EmailField(
        null=False,
        blank=False,
        default='Unknow.'
    )
