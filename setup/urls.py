from django.contrib import admin
from django.urls import path
from app.views import WalletController

urlpatterns = [
    path('admin/', admin.site.urls),
    path('make-transaction/', WalletController, name='WalletController'),
]
