from django.http import JsonResponse
from app.scripts.limits_application_service import LimitsApplicationService
import json

def CheckLimits(request):

    body_request = json.loads(request.body)
    wallet_to_debit_id = body_request.get('wallet_to_debit_id')
    amount = body_request.get('amount')
    application_limits = LimitsApplicationService(wallet_id=wallet_to_debit_id)

    try:
        
        application_limits.GetDatasOfWallet(amount)
        return JsonResponse({'allowed':True}, status=200)
    
    except Exception as e:
        # regra de negócio
        if str(e) in ["Daily Limit Exceeded", "Monthly Limit Exceeded"]:
            return JsonResponse(
                {
                    "allowed": False,
                    "reason": str(e)
                },
                status=200
            )

        # erro técnico
        return JsonResponse(
            {"error": "INTERNAL_ERROR"},
            status=500
        )