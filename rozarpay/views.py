import razorpay
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.conf import settings
from rozarpay.models import Payment
@require_POST
@csrf_exempt
def create_razorpay_order(request):
    client = razorpay.Client(auth=(settings.RAZORPAY_API_KEY, settings.RAZORPAY_API_SECRET))
    
    amount = 1000  # Replace with the actual payment amount in paise
    
    order = client.order.create({
        'amount': amount,
        'currency': 'INR',
        'payment_capture': 1  # Auto-capture the payment
    })
    
    payment = Payment.objects.create(
        razorpay_order_id=order['id'],
        amount=amount / 100  # Convert amount from paise to rupees
    )
    
    return JsonResponse(order)

@require_POST
@csrf_exempt
def razorpay_payment_success(request):
    data = request.POST
    client = razorpay.Client(auth=(settings.RAZORPAY_API_KEY, settings.RAZORPAY_API_SECRET))
    
    try:
        client.utility.verify_webhook_signature(data, request.META.get('HTTP_X_RAZORPAY_SIGNATURE'), request.body.decode('utf-8'))
        payment = Payment.objects.get(razorpay_order_id=data['payload']['order']['entity']['id'])
        payment.status = 'success'
        payment.save()
    except Exception as e:
        # Handle any exceptions or errors
        pass
    
    return JsonResponse({'status': 'success'})