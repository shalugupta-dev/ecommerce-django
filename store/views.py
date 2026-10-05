from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Cart
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Product, Cart, Order, OrderItem

def home(request):
    products = Product.objects.all()

    return render(
        request,
        "store/home.html",
        {"products": products}
    )


def product_detail(request, id):
    product = get_object_or_404(Product, id=id)

    return render(
        request,
        "store/product_detail.html",
        {"product": product}
    )


def add_to_cart(request, id):
    product = get_object_or_404(Product, id=id)

    cart_item, created = Cart.objects.get_or_create(
        product=product
    )

    if not created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect("cart")


def cart(request):
    cart_items = Cart.objects.select_related("product").all()

    total = sum(
        item.product.price * item.quantity
        for item in cart_items
    )

    return render(
        request,
        "store/cart.html",
        {
            "cart_items": cart_items,
            "total": total
        }
    )
@login_required
def checkout(request):
    cart_items = Cart.objects.select_related("product").all()

    if not cart_items:
        return redirect("cart")

    total = sum(
        item.product.price * item.quantity
        for item in cart_items
    )

    if request.method == "POST":

        order = Order.objects.create(
            user=request.user,
            total_amount=total
        )

        for item in cart_items:
            OrderItem.objects.create(
                order=order,
                product=item.product,
                quantity=item.quantity,
                price=item.product.price
            )

        cart_items.delete()

        return redirect("order_success", order_id=order.id)

    return render(
        request,
        "store/checkout.html",
        {
            "cart_items": cart_items,
            "total": total
        }
    )


@login_required
def order_success(request, order_id):
    order = get_object_or_404(
        Order,
        id=order_id,
        user=request.user
    )

    return render(
        request,
        "store/order_success.html",
        {"order": order}
    )
def remove_from_cart(request, id):
    cart_item = get_object_or_404(Cart, id=id)
    cart_item.delete()

    return redirect("cart")

def remove_from_cart(request, id):
    cart_item = get_object_or_404(Cart, id=id)
    cart_item.delete()

    return redirect("cart")