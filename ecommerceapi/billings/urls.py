from django.urls import path

from .views import CarViewSet, OrderViewSet, add_product

app_name = 'billings'

urlpatterns = [

    # Car endpoints...
    path(
        "car/",
        CarViewSet.as_view(
            {"get": "list", "post": "create"}
        ),
        name = "cars"
    ),

    path(
        "car/<int:pk>",
        CarViewSet.as_view(
            {"get": "retrieve"}
        ),
        name = 'car'
    ),

    path("car/add_product/<int:c_pk>/<int:pk>", add_product, name="add_product"),

    # Order endpoints
    path(
        'order/',
        OrderViewSet.as_view(
            {"get": "list"}
        ),
        name = "orders"
    ),
    path(
        'order/<int:pk>/',
        OrderViewSet.as_view(
            {"get": "retrieve", "post": "transaction"}
        ),
        name = "order"
    ),
    path(
        'order/finalize/<int:pk>',
        OrderViewSet.as_view(
            {"post": "finalize"}
        ),
        name="finalize_order"
    )
]
