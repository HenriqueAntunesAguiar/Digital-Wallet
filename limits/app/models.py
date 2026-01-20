from django.db import models
import uuid 

class WalletLimits(models.Model):
    wallet_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    daily_limit = models.FloatField()
    daily_limit_used = models.FloatField()
    monthly_limit = models.FloatField()
    monthly_limit_used = models.FloatField()