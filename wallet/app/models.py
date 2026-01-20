from django.db import models
import uuid 

class WalletModel(models.Model):
    wallet_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    balance = models.FloatField()
    timestamp = models.TimeField(auto_now_add=True)