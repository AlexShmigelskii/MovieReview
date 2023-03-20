from django.urls import path

from .views import add_review, index

urlpatterns = [
    path('', index, name='index'),
    path('add_review/', add_review, name='add_review'),
]

