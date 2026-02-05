from django.contrib import admin
from django.urls import path
from app.views import MakeTransaction, CreateClientRegister

urlpatterns = [
    path('admin/', admin.site.urls),
    path('make-transaction/', MakeTransaction, name='make_transaction'),
    path('create-wallet/',CreateClientRegister, name='create-wallet'),
]
