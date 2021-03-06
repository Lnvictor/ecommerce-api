from django.urls import path

from ecommerceapi.providers.views import ProviderViewSet

app_name = "providers"

urlpatterns = [
    path(
        "",
        ProviderViewSet.as_view({"post": "create", "get": "list"}),
        name="provider",
    ),

    path(
        "<int:pk>/",
        ProviderViewSet.as_view(
            {"get": "retrieve", "put": "update", "delete": "destroy"}
        ),
        name="provider_by_id",
    ),
]
