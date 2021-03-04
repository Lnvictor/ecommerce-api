from django.urls import path

from ecommerceapi.core.views import DomainViewSet, ProductViewSet

app_name = "core"

urlpatterns = [
    path("domain/", DomainViewSet.as_view({"get": "list", "post": "create"}), name="domain"),
    path("domain/<int:pk>/", DomainViewSet.as_view({"get": "retrieve", "put": "update", "delete": "destroy"})),
    path("products-domain/<int:pk>/", DomainViewSet.as_view({"get": "get_products"})),
    path("product/", ProductViewSet.as_view({"get": "list", "post": "create"}), name="product"),
    path("product/int:pk/", ProductViewSet.as_view({"get": "retrieve", "put": "update", "delete":"destroy"}))
]
