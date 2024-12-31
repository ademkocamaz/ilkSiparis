from django.shortcuts import render

# Create your views here.
from django.contrib.auth.decorators import login_required
from order._model.order import Order

@login_required(login_url="user/login/")
def index(request):
    order_count = Order.objects.count()
    context = {
        "order_count": order_count,
    }
    return render(request=request, template_name="index.html", context=context)
