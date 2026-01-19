from django.db import models
import uuid 

class Wallet(models.Model):
    wallet_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    balance = models.FloatField()
    timestamp = models.TimeField(auto_now_add=True)

class TransactionLogs(models.Model):
    type = models.CharField(max_length=100)
    wallet_id = models.ForeignKey(
        Wallet,
        to_field='wallet_id',
        on_delete=models.CASCADE,
        related_name='logs'
    )
    transaction_uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    amount = models.FloatField()
    status = models.CharField(choices=[('PENDING','PENDING'), ('COMPLETED','COMPLETED'), ('FAILED','FAILED')], default='PENDING')
    timestamp = models.TimeField(auto_now_add=True)


