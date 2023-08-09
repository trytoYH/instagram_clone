from django.urls import path
from .views import Login, Join, LogOut, UploadProfile

urlpatterns = [
    path('login', Login.as_view()),
    path('join', Join.as_view()),
    path('logout', LogOut.as_view()),
    path('profile/upload', UploadProfile.as_view())
]