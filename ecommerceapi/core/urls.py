from django.urls import path

from ecommerceapi.core.views import DomainViewSet

app_name = "core"

urlpatterns = [
    path("domain/", DomainViewSet.as_view({"get": "list", "post": "create"}), name="domain"),
    path("domain/<int:pk>", DomainViewSet.as_view({"get": "retrieve", "put": "retrieve", "delete": "destroy"})),
]
