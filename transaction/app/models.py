from django.db import models
import uuid 

class TransactionLogs(models.Model):
    wallet_from = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    wallet_to = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    transaction_uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    amount = models.FloatField()
    status = models.CharField(choices=[('PENDING','PENDING'), ('COMPLETED','COMPLETED'), ('FAILED','FAILED')], default='PENDING')
    timestamp = models.TimeField(auto_now_add=True)