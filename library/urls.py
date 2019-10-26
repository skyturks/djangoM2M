from django.contrib import admin
from django.urls import path, include
from . import views

app_name = "library"

urlpatterns = [
    path('library/', views.Libraries.as_view(), name="libraries"),
    path('library/add/', views.LibraryCreate.as_view(), name="library-create"),
    path('library/<int:pk>', views.LibraryShow.as_view(), name="library-show"),
]
