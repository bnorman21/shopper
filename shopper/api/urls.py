from django.urls import path
from .views import StoreView

urlpatterns = [
    path('home', StoreView.as_view())
]