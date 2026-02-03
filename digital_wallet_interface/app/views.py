from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
def MakeTransaction(request):

    return JsonResponse(200,{'msg':'solicitação de transação feita'})
