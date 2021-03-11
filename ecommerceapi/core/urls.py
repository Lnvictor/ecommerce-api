from django.urls import path

from ecommerceapi.core.views import DomainViewSet, ProductViewSet, CsvFileViews

app_name = "core"

urlpatterns = [
    # Domain
    path(
        "domain/",
        DomainViewSet.as_view({"get": "list", "post": "create"}),
        name="domain",
    ),
    path(
        "domain/<int:pk>/",
        DomainViewSet.as_view(
            {"get": "retrieve", "put": "update", "delete": "destroy"}
        ),
        name="domain_by_id",
    ),
    # Products
    path("products-domain/<int:pk>/", DomainViewSet.as_view({"get": "get_products"})),
    path(
        "product/",
        ProductViewSet.as_view({"get": "list", "post": "create"}),
        name="product",
    ),
    path(
        "product/<int:pk>/",
        ProductViewSet.as_view(
            {"get": "retrieve", "put": "update", "delete": "destroy"}
        ),
        name="product_by_id",
    ),
    # Product from provider
    path(
        "product-from-provider/<int:pk>",
        ProductViewSet.as_view({"get": "get_products_from_provider"}),
        name="get_from_provider",
    ),

    path("upload-from-csv", CsvFileViews().parse_csv, name="upload_csv")
]
