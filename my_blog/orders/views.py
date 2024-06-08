from django.shortcuts import render
from .models import OrderItem
from .forms import OrderCreateForm
from .tasks import order_created
from cart.cart import Cart
from django.contrib.auth.decorators import login_required


@login_required
def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order,
                                        product=item['product'],
                                        price=item['price'],
                                        quantity=item['quantity'])
            # clear the cart
            cart.clear()
            # launch asynchronous task
            #order_created.delay(order.id)
            return render(request,
                          'orders/order/created.html',
                          {'order': order})
    else:
        if request.user.is_authenticated:
            initial_data = {
                'first_name': request.user.first_name,
                'last_name': request.user.last_name,
                'email': request.user.email,
            }
            form = OrderCreateForm(initial=initial_data)
        else:
            pass
    return render(request,
                  'orders/order/create.html',
                  {'cart': cart, 'form': form})