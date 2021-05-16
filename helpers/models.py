#
from django.db import models


class TrackingModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        # abstract true means this model can only be inherited from and can't be use to create new model
        abstract = True
        ordering = ('-created_at',)

