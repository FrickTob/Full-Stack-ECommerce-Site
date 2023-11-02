from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path("", views.getProducts, name="all_products"),
    path("<int:pk>/", views.getProduct, name="product_detailed"),
    path("<int:pk>/remove/", views.removeProduct, name="remove_products"),
    path("<int:pk>/add/", views.addProduct, name="add_products")
]