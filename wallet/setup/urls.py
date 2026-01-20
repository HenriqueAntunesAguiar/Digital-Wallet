from django.contrib import admin
from django.urls import path
from app.views import WalletController, CreateWallet

urlpatterns = [
    path('admin/', admin.site.urls),
    path('/', WalletController, name='WalletController'),
    path('create-wallets/', CreateWallet, name='CreateWallet')
]
