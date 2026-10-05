from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),

    path(
        "product/<int:id>/",
        views.product_detail,
        name="product_detail"
    ),

    path(
        "add-to-cart/<int:id>/",
        views.add_to_cart,
        name="add_to_cart"
    ),

    path(
        "cart/",
        views.cart,
        name="cart"
    ),

    path(
        "remove-from-cart/<int:id>/",
        views.remove_from_cart,
        name="remove_from_cart"
    ),

    # CHECKOUT
    path(
        "checkout/",
        views.checkout,
        name="checkout"
    ),

    # ORDER SUCCESS
    path(
        "order-success/<int:order_id>/",
        views.order_success,
        name="order_success"
    ),
]